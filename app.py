import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Student Result Analysis", layout="wide")
plt.style.use("ggplot")

@st.cache_data
def load_data():
    df = pd.read_csv("Student.csv")
    subjects = ["Maths", "Physics", "Chemistry"]
    df["total_marks"] = df[subjects].sum(axis=1)
    df["percentage"] = df["total_marks"] / (len(subjects) * 100) * 100
    df["status"] = df["Result"].map({1: "Pass", 0: "Fail"})
    df["student_id"] = np.arange(1, len(df) + 1)
    return df, subjects

df, subjects = load_data()

st.title("📊 Student Result Analysis Dashboard")

# ---- Filters ----
st.sidebar.header("Filters")
min_per, max_per = st.sidebar.slider(
    "Percentage Range",
    min_value=0,
    max_value=100,
    value=(0, 100),
    step=5
)
status_filter = st.sidebar.multiselect(
    "Status",
    options=["Pass", "Fail"],
    default=["Pass", "Fail"]
)

filtered_df = df[
    (df["percentage"].between(min_per, max_per)) &
    (df["status"].isin(status_filter))
]

st.write(f"Showing **{len(filtered_df)}** students after filters.")

# ---- KPIs ----
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Average Percentage", f"{filtered_df['percentage'].mean():.2f}%")
with col2:
    st.metric("Pass Count", int((filtered_df['status'] == 'Pass').sum()))
with col3:
    st.metric("Fail Count", int((filtered_df['status'] == 'Fail').sum()))

st.markdown("---")

# ---- Subject-wise Average ----
difficulty_data = []
for subj in subjects:
    avg = filtered_df[subj].mean()
    fail_count = (filtered_df[subj] < 40).sum()
    pass_count = (filtered_df[subj] >= 40).sum()
    difficulty_data.append({
        "subject": subj,
        "avg_marks": avg,
        "fail_count": fail_count,
        "pass_count": pass_count
    })

difficulty_df = pd.DataFrame(difficulty_data)
difficulty_df["fail_rate_%"] = difficulty_df["fail_count"] / (difficulty_df["fail_count"] + difficulty_df["pass_count"]) * 100

col_chart, col_table = st.columns([2, 1])

with col_chart:
    fig, ax = plt.subplots(figsize=(5, 3))
    sns.barplot(x="subject", y="avg_marks", data=difficulty_df, ax=ax)
    ax.set_ylim(0, 100)
    ax.set_title("Average Marks per Subject")
    st.pyplot(fig)

with col_table:
    st.dataframe(difficulty_df.sort_values(by=["avg_marks", "fail_rate_%"],
                                           ascending=[True, False]))

st.markdown("---")

# ---- Top & Low performers ----
st.subheader("🏅 Top & Low Performers")
selected_subject = st.selectbox("Mode", ["Overall"] + subjects)

if selected_subject == "Overall":
    top_n = filtered_df.sort_values(by="percentage", ascending=False).head(5)
    low_n = filtered_df.sort_values(by="percentage", ascending=True).head(5)
else:
    subj = selected_subject
    top_n = filtered_df.sort_values(by=subj, ascending=False).head(5)
    low_n = filtered_df.sort_values(by=subj, ascending=True).head(5)

colA, colB = st.columns(2)
with colA:
    st.markdown("### 🔝 Top 5")
    st.dataframe(top_n[["student_id"] + subjects + ["percentage", "status"]])
with colB:
    st.markdown("### 🔻 Bottom 5")
    st.dataframe(low_n[["student_id"] + subjects + ["percentage", "status"]])

st.markdown("---")

# ---- Percentage distribution ----
st.subheader("📈 Percentage Distribution")
fig2, ax2 = plt.subplots(figsize=(5, 3))
ax2.hist(filtered_df["percentage"], bins=10, edgecolor="black")
ax2.set_xlabel("Percentage")
ax2.set_ylabel("Number of Students")
ax2.set_title("Percentage Distribution")
st.pyplot(fig2)
