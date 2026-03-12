import pandas as pd

# Power BI sends the table as 'dataset'
df = dataset.copy()

# group subjects by student
student = df.groupby(["StudentID","Name"]).agg(
    TotalHeld=('HeldHours','sum'),
    TotalAttended=('AttendedHours','sum')
).reset_index()

# calculate overall attendance percentage
student["OverallAttendance"] = (
    student["TotalAttended"] / student["TotalHeld"]
) * 100

# classify students
student["AttendanceStatus"] = student["OverallAttendance"].apply(
    lambda x: "Regular" if x >= 75 else "Irregular"
)

student
