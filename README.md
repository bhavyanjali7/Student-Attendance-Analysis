# Student-Attendance-Analysis
🎓 Student Attendance Analytics Dashboard (Power BI)
📊 Project Overview
This project presents a Student Attendance Analytics Dashboard built using Power BI to analyze attendance patterns, identify irregular students, and evaluate academic performance trends.
The dashboard enables interactive exploration of subject-wise attendance, student attendance status, exam results, and attendance gaps, helping educators identify students who require attention.
The project follows a Star Schema data model and integrates data cleaning, transformation, and modeling techniques to create an efficient analytics system.


📈 Dashboard Features
The dashboard includes several interactive visualizations:
KPI Cards
Total Students
Average Attendance
Regular Students
Irregular Students

Visualizations
📌 Attendance Status Distribution
Donut chart showing proportion of Regular vs Irregular students.

📌 Subject-wise Attendance
Clustered column chart comparing average attendance across subjects.

📌 Exam Results vs Attendance
Stacked column chart showing Pass/Fail distribution based on attendance status.

📌 Attendance vs Academic Performance
Scatter plot showing correlation between attendance and marks.

📌 Students Needing Extra Classes
Bar chart highlighting students needing additional hours to reach 75% attendance.

🎛 Interactive Filters
The dashboard contains dynamic slicers:
Subject
Attendance Status
Exam Result
These filters allow users to explore the data interactively.

🧹 Data Preparation Process
The data pipeline includes:
Data Cleaning
Performed using Power Query Editor.

Steps included:
Removing duplicates
Handling missing values
Standardizing column types
Creating calculated columns
Data Transformation

Additional calculated fields were created:
AttendanceGap
HoursNeededFor75
AttendanceCategory
Data Modeling
Implemented Star Schema modeling to improve:
Query performance
Dashboard responsiveness
Data organization

🛠 Tools Used
Power BI
Power Query Editor
Python (for transformations)
Data Modeling (Star Schema)

🚀 Key Insights
The dashboard helps identify:
Students with low attendance
Subjects with lower attendance rates
Correlation between attendance and exam results
Students needing extra classes to reach 75% attendance
