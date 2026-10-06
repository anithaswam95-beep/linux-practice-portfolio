# 🐧 Linux Practice Portfolio — anithaswam95-beep

Linux command line, shell scripting, and Python data analysis practice on Ubuntu (WSL).

---

## 📁 Repository Structure

```
linux-practice-portfolio/
├── shell-scripts/
│   └── my_script.sh              # Bash shell script practice
├── data_project/
│   ├── airtravel.csv             # Airline passenger dataset (1958-1960)
│   └── airtravel_analysis.py     # Python data analysis with Pandas & Matplotlib
├── school/
│   ├── testfile.txt              # File creation & editing practice
│   └── testfile2.txt             # Text manipulation practice
├── sql-course/
│   ├── SQL_Basics_and_Advanced.ipynb  # SQL basics → advanced + DAX-to-SQL (194 cells)
│   ├── Flash_Project_Employee_Analytics.ipynb  # SQL capstone: employee analytics dashboard
│   ├── flash_project.md          # Project summary and learning goals
│   └── README.md                 # SQL course portfolio overview
├── bash_history_reference.txt    # Linux commands practiced (reference)
└── README.md
```

---

## 🔗 Featured SQL Projects

### 1) SQL Basics and Advanced
A hands-on SQL learning notebook covering fundamentals through advanced topics, including:
- SELECT, WHERE, JOINs, GROUP BY, HAVING
- subqueries, CTEs, window functions
- JSON/VARIANT, recursive queries, and DAX-to-SQL translations

View it here: [SQL_Basics_and_Advanced.ipynb](sql-course/SQL_Basics_and_Advanced.ipynb)

### 2) SQL Flash Project: Employee Analytics
A capstone project focused on employee performance and department analysis using SQL.
This project demonstrates:
- joins and data modeling
- department-level aggregation
- window functions for ranking
- CASE WHEN salary tier analysis
- business-style reporting queries

View it here: [Flash_Project_Employee_Analytics.ipynb](sql-course/Flash_Project_Employee_Analytics.ipynb)

### 3) Project Summary
A short summary explaining the business scenario, learning goals, and next steps for the SQL capstone.

View it here: [flash_project.md](sql-course/flash_project.md)

---

## 🛠️ Skills Demonstrated

### Linux / Bash
- File & directory management (`ls`, `cd`, `mkdir`, `rmdir`, `chmod`)
- Shell scripting (`#!/bin/bash`, `echo`, script execution)
- Environment variables (`$HOME`, `$USER`, `$SHELL`, `$PATH`)
- Text editors (`nano`, `vim`)
- File permissions (`chmod +x`)
- Package management (`pip install`, `sudo apt`)

### Python Data Analysis
- **Pandas** — CSV loading, data cleaning, column renaming, type conversion
- **Matplotlib** — Line charts, multi-series plotting, chart export
- **Data Wrangling** — Summary statistics, aggregation, finding max values
- **File I/O** — Reading/writing CSV files, saving charts as PNG

### MySQL
- MySQL server installation and configuration on Ubuntu
- `sudo mysql` — Database administration
- `mysql_secure_installation` — Security hardening

### SQL (Databricks)
- Basics → advanced: SELECT, JOINs, GROUP BY/HAVING, subqueries, CTEs, window functions
- Expert: recursive CTEs, PIVOT/UNPIVOT, JSON/VARIANT, Delta Lake time travel, views
- DAX-to-SQL translations (CALCULATE, RANKX, TOPN, SAMEPERIODLASTYEAR, etc.)
- See [sql-course/SQL_Basics_and_Advanced.ipynb](sql-course/SQL_Basics_and_Advanced.ipynb)

---

## 📊 Data Project: Airline Passengers Analysis

Analyzes monthly airline passenger data from 1958-1960:
- Loads and cleans CSV data with Pandas
- Calculates total passengers per month across all years
- Identifies the busiest travel month
- Generates a line chart comparing year-over-year trends
- Exports cleaned data and summary statistics

---

## 🖥️ Environment

- **OS**: Ubuntu on WSL2 (Windows Subsystem for Linux)
- **Python**: 3.x with Pandas, Matplotlib
- **Database**: MySQL
- **Shell**: Bash

---

## 👤 Author

**anithaswam95-beep**
- GitHub: [https://github.com/anithaswam95-beep](https://github.com/anithaswam95-beep)
