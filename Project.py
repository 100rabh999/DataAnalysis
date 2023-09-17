#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

# Load your dataset into a DataFrame (assuming it's in a CSV file)
df = pd.read_csv('C:\\Users\\madan\\Downloads\\da.csv')

# 1. How many unique students are included in the dataset?
unique_students = df['Email ID'].nunique()
print("Unique Students:", unique_students)

# 2. What is the average Quantity (number of events attended) of the students?
average_quantity = df['Quantity'].mean()
print("Average Quantity:", average_quantity)

# 3. What is the distribution of students across different Events?
event_distribution = df['Events'].value_counts()
print("Distribution of Events:")
print(event_distribution)

# 4. What is the distribution of Attendee Status?
attendee_status_distribution = df['Attendee Status'].value_counts()
print("Distribution of Attendee Status:")
print(attendee_status_distribution)

# 5. What is the distribution of students across different Colleges?
college_distribution = df['College Name'].value_counts()
print("Distribution of Colleges:")
print(college_distribution)

# 6. How did students come to know about the event? (Top 5)
promotion_channel_counts = df['How did you come to know about this event?'].value_counts().head(5)
print("Top 5 Promotion Channels:")
print(promotion_channel_counts)

# 7. What is the distribution of Designations among students?
designation_distribution = df['Designation'].value_counts()
print("Distribution of Designations:")
print(designation_distribution)

# 8. What is the distribution of Year of Graduation among students?
graduation_year_distribution = df['Year of Graduation'].value_counts()
print("Distribution of Graduation Years:")
print(graduation_year_distribution)

# 9. What is the distribution of students across different Cities?
city_distribution = df['City'].value_counts()
print("Distribution of Cities:")
print(city_distribution)

# 10. How does the expected salary vary based on factors like 'CGPA', 'Experience with python (Months)', 'Family Income'?
salary_vs_factors = df[['CGPA', 'Experience with python (Months)', 'Family Income', 'Expected salary (Lac)']]
correlation_matrix = salary_vs_factors.corr()
print("Correlation Matrix:")
print(correlation_matrix)

# 11. Which event tends to attract more students from specific Designations?
event_vs_designation = df.groupby('Designation')['Events'].value_counts().unstack()
most_popular_events_by_designation = event_vs_designation.idxmax(axis=1)
print("Most Popular Event by Designation:")
print(most_popular_events_by_designation)

# 12. Do students with leadership skills tend to have higher CGPA or better expected salary?
leadership_students = df[df['Leadership- skills'] == 'Yes']
non_leadership_students = df[df['Leadership- skills'] == 'No']

# Compare CGPA
avg_cgpa_leadership = leadership_students['CGPA'].mean()
avg_cgpa_non_leadership = non_leadership_students['CGPA'].mean()

# Compare Expected Salary
avg_salary_leadership = leadership_students['Expected salary (Lac)'].mean()
avg_salary_non_leadership = non_leadership_students['Expected salary (Lac)'].mean()

print("Average CGPA for Leadership Students:", avg_cgpa_leadership)
print("Average CGPA for Non-Leadership Students:", avg_cgpa_non_leadership)
print("Average Expected Salary for Leadership Students:", avg_salary_leadership)
print("Average Expected Salary for Non-Leadership Students:", avg_salary_non_leadership)


# 13. Is there a correlation between leadership skills and expected salary of the students?
# Calculate the correlation between leadership skills and expected salary.

# 14. How many students are graduating by the end of a specific year (e.g., 2024)?
graduating_students_2024 = df[df['Year of Graduation'] <= 2024]
total_graduating_students = len(graduating_students_2024)
print("Total Students Graduating by the End of 2024:", total_graduating_students)

# 15. Which promotion channel brings in more student participations for the event?
promotion_channel_counts = df['How did you come to know about this event?'].value_counts()
print("Promotion Channel with Most Student Participations:")
print(promotion_channel_counts.idxmax())

# 16. Find the total number of students who attended events related to a specific topic (e.g., Data Science).
data_science_events = df[df['Events'].str.contains('Data Science', case=False)]
total_data_science_attendees = len(data_science_events)
print("Total Students Attending Data Science Events:", total_data_science_attendees)

# 17. Do students with high CGPA and more Python experience tend to have higher expected salaries on average?
high_cgpa_python_experience = df[(df['CGPA'] >= 3.5) & (df['Experience with python (Months)'] >= 12)]

# Calculate the average expected salary for students with high CGPA and Python experience
avg_salary_high_cgpa_python = high_cgpa_python_experience['Expected salary (Lac)'].mean()
print("Average Expected Salary for Students with High CGPA and Python Experience:", avg_salary_high_cgpa_python)


# 18. How many students came to know about the event from their colleges? Which are the top 5 colleges?
college_promotion_counts = df[df['How did you come to know about this event?'] == 'College']['College Name'].value_counts().head(5)
print("Top 5 Colleges with Students Knowing About the Event from Their Colleges:")
print(college_promotion_counts)


# In[9]:


# 12. Do students with leadership skills tend to have higher CGPA or better expected salary?
leadership_students = df[df['Leadership- skills'] == 'Yes']
non_leadership_students = df[df['Leadership- skills'] == 'No']

# Compare CGPA
avg_cgpa_leadership = leadership_students['CGPA'].mean()
avg_cgpa_non_leadership = non_leadership_students['CGPA'].mean()

# Compare Expected Salary
avg_salary_leadership = leadership_students['Expected salary (Lac)'].mean()
avg_salary_non_leadership = non_leadership_students['Expected salary (Lac)'].mean()

print("Average CGPA for Leadership Students:", avg_cgpa_leadership)
print("Average CGPA for Non-Leadership Students:", avg_cgpa_non_leadership)
print("Average Expected Salary for Leadership Students:", avg_salary_leadership)
print("Average Expected Salary for Non-Leadership Students:", avg_salary_non_leadership)


# In[5]:


# 12. Do students with leadership skills tend to have higher CGPA or better expected salary?
leadership_students = df[df['Leadership- skills'] == 'Yes']
non_leadership_students = df[df['Leadership- skills'] == 'No']

# Compare CGPA
avg_cgpa_leadership = leadership_students['CGPA'].mean()
avg_cgpa_non_leadership = non_leadership_students['CGPA'].mean()

# Compare Expected Salary
avg_salary_leadership = leadership_students['Expected salary (Lac)'].mean()
avg_salary_non_leadership = non_leadership_students['Expected salary (Lac)'].mean()

print("Average CGPA for Leadership Students:", avg_cgpa_leadership)
print("Average CGPA for Non-Leadership Students:", avg_cgpa_non_leadership)
print("Average Expected Salary for Leadership Students:", avg_salary_leadership)
print("Average Expected Salary for Non-Leadership Students:", avg_salary_non_leadership)


# In[6]:


# 17. Do students with high CGPA and more Python experience tend to have higher expected salaries on average?
high_cgpa_python_experience = df[(df['CGPA'] >= 3.5) & (df['Experience with python (Months)'] >= 12)]

# Calculate the average expected salary for students with high CGPA and Python experience
avg_salary_high_cgpa_python = high_cgpa_python_experience['Expected salary (Lac)'].mean()
print("Average Expected Salary for Students with High CGPA and Python Experience:", avg_salary_high_cgpa_python)


# In[ ]:




