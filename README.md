# Student Result Analysis Dashboard

This project performs analysis on student performance data using Python.  
It focuses on marks in **Maths**, **Physics**, and **Chemistry**, and generates:

- Overall performance statistics  
- Top and low performers  
- Subject-wise difficulty  
- Pass/Fail distribution  
- Visual graphs and insights  

An optional **Streamlit dashboard** is included for interactive analysis.

---

## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Dataset Description](#dataset-description)  
4. [Project Structure](#project-structure)  
5. [Setup and Installation](#setup-and-installation)  
6. [How to Run](#how-to-run)  
    - [Run Analysis Script](#run-analysis-script)  
    - [Run Streamlit Dashboard (Optional)](#run-streamlit-dashboard-optional)  
7. [Technologies Used](#technologies-used)  
8. [Future Enhancements](#future-enhancements)  
9. [Author](#author)

---

## Project Overview

The **Student Result Analysis Dashboard** is a Python-based data analysis project that reads student marks from a CSV file (`Student.csv`) and generates useful insights.

The project is designed to help:

- Understand overall class performance  
- Identify top and low-performing students  
- Detect difficult subjects based on average marks and fail rates  
- Visualize performance trends using charts  

This can be used for academic decision making, remedial planning, and performance tracking.

---

## Features

### Data Processing

- Reads data from `Student.csv`
- Computes:
  - Total marks
  - Percentage
  - Pass/Fail status
  - Simple student ID

### Analysis

- Overall summary statistics (mean, min, max, etc.)
- Subject-wise:
  - Average marks
  - Minimum and maximum marks
- Top 5 and bottom 5 students (overall and subject-wise)
- Subject difficulty based on:
  - Average marks
  - Fail count and fail rate

### Visualizations

- Bar chart: Average marks per subject  
- Histogram: Percentage distribution  
- Boxplot: Subject-wise marks distribution  
- Heatmap: Correlation between subjects and overall performance  
- Bar chart: Pass vs Fail count  

### Optional: Streamlit Dashboard

- Filter by:
  - Percentage range
  - Pass/Fail status
- KPIs:
  - Average percentage
  - Pass count
  - Fail count
- Subject difficulty table
- Top & low performers view
- Percentage distribution chart

---

## Dataset Description

**File:** `Student.csv`

The dataset contains the following columns:

| Column    | Description                            |
|-----------|----------------------------------------|
| Maths     | Marks in Mathematics (0–100)           |
| Physics   | Marks in Physics (0–100)               |
| Chemistry | Marks in Chemistry (0–100)             |
| Result    | Overall result (1 = Pass, 0 = Fail)    |

You can extend this file with more rows to increase the dataset size.

---
---

## Project Structure

```text
Student-Result-Analysis/
│
├── Student.csv          # Input dataset
├── analysis.py          # Python script for data analysis + visualizations
├── app.py               # Streamlit dashboard (optional)
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies

---

## Setup and Installation

The project can be set up by cloning the repository into your system and preparing the environment for execution.  
A virtual environment may be created to keep the dependencies separate, and the required Python libraries must be installed to enable data processing, analysis, and visualization.  
Once the environment is ready and the dataset is available, the project is ready to be executed either through the analysis script or the optional Streamlit dashboard.

---

## How to Run

### Run Analysis Script

The analysis script processes the dataset, computes performance metrics such as total marks and percentages, identifies top and low performers, evaluates subject difficulty, and generates multiple visual insights.  
All results are displayed either in the console or through graphical windows, depending on the environment.  
This script provides the complete analytical summary of the student performance dataset.

### Run Streamlit Dashboard (Optional)

The optional Streamlit dashboard offers an interactive interface for exploring student performance.  
It allows users to apply filters, view KPIs, analyze subject difficulty, and explore top and low performers dynamically.  
The dashboard also includes visual charts, making it easier to interpret class-wide performance trends in a user-friendly environment.

---

## Technologies Used

The project is developed using Python and relies on key libraries from the data analysis ecosystem.  
Pandas and NumPy handle data loading and numerical operations, Matplotlib and Seaborn create rich visualizations, and Streamlit provides an interactive dashboard interface.  
Together, these tools enable fast, reliable, and visually clear performance analysis.

---

## Future Enhancements

Several improvements can be made to expand the capabilities of the system:

- Adding student names, roll numbers, class, and section information  
- Including more subjects or semester-wise analysis  
- Replacing CSV storage with a database (e.g., MySQL)  
- Implementing user authentication for teachers or administrators  
- Applying machine learning models to predict at-risk or low-performing students  

These additions would make the system more extensible, scalable, and suitable for real academic environments.

---

## Author

**Harshvardhan Misal**  
Diploma in Computer Engineering  

This project is open for enhancements, and contributions or forks are encouraged.

---

