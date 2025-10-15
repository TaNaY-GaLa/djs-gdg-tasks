# djs-gdg-tasks
Task 1: Python logic — forest grid extraction &amp; IPL team optimization. 
Task 2: EDA on Formula 1 data using Pandas, Seaborn &amp; Matplotlib. 
Task 3: Built ML model to predict race outcomes. 
Task 4: Researched AI hallucinations &amp; reliability.

TASK 1:
Forest Extraction Zone Simulation

Project Overview
This project simulates a forest grid and calculates the number of Lal Chandans (trees) in a selected extraction zone.
It demonstrates how to use arrays and random number generation in Python to model a forest and extract data from a specific region.

Objective
Create a forest represented as a 2D grid of trees (1 = tree, 0 = empty).
Randomly populate the forest with trees.
Define a 3x3 extraction zone in the center of the forest.
Count the total number of trees in the extraction zone.

How It Works
User Input:
The user enters the number of rows (a) and columns (b) of the forest grid.
Forest Creation:
A 2D NumPy array forest of size a x b is created.
Each cell is randomly assigned 0 (empty) or 1 (tree) using Python’s random module.

Extraction Zone:
A 3x3 zone is selected in the center of the forest.
Values from the forest array are copied to a smaller array zone.
Count Trees:
The total number of Lal Chandans (trees) in the extraction zone is calculated using np.sum(zone).

Code Features
Uses NumPy for array handling.
Uses random module to simulate tree distribution.
Extracts and analyzes a subsection of a larger grid.
Easy to modify for different forest sizes or extraction zones.

Example Output
Enter the number of rows: 5
Enter the number of columns: 5

Forest Grid:
[[1. 0. 1. 1. 0.]
 [0. 1. 0. 0. 1.]
 [1. 1. 0. 1. 0.]
 [0. 1. 1. 0. 1.]
 [1. 0. 1. 1. 0.]]

Extraction zone:
[[1. 0. 0.]
 [1. 0. 1.]
 [1. 1. 0.]]

Total no. of Lal Chandans in extraction zone: 5

Conclusion
This program demonstrates basic simulation using arrays.
Helps visualize how to extract and analyze data from a specific region.
Can be extended to larger grids, different extraction zones, or different types of analysis.


Best Cricket Team Selector
Project Overview
This project helps to select the best cricket team from a squad of players based on their strengths and weaknesses.
It calculates a team score by considering the number of unique strengths minus the number of unique weaknesses.
The program then finds the combination of players that maximizes team performance.

Objective
Represent players and their skills using a dictionary.
Each player has:
Strengths (skills they excel at)
Weaknesses (areas where they may underperform)
Automatically find the best team of k players with the highest combined score.

How It Works
Define Squad:
Each player has a list of strengths and weaknesses.
Team Scoring Function:
Combines all strengths and weaknesses of a team.
Calculates the team score as:
team_score = total unique strengths - total unique weaknesses
Team Selection:
Iterates over all combinations of k players from the squad.
Keeps track of the team with the highest score.

Output:
Prints the best team, their score, and the total number of strengths and weaknesses.
Code Features
Uses Python dictionaries to store player data.
Uses sets to easily combine and count unique strengths and weaknesses.
Works for any value of k (number of players in a team).
Can be extended to larger squads or more complex scoring rules.

Example Output
Best Team Found for 4 players: ['Virat Kohli', 'Rahul', 'Bumrah', 'Jadeja']
With best score: 10 having total strength: 12 and total weakness: 2


Best Team Found → Combination of players with maximum score.
Score → Difference between total strengths and weaknesses.
Total strength → Number of unique skills in the team.
Total weakness → Number of unique weaknesses in the team.

Conclusion
This program helps formulate the strongest possible cricket team based on player abilities.
It is a simple combinatorial optimization example using Python.
Can be further improved by:
Assigning weights to strengths and weaknesses.
Considering player roles (batsman, bowler, all-rounder) for more realistic team selection.
Scaling to larger squads efficiently using optimized algorithms.

TASK 2 & 3:
F1 Race DNF Prediction
Project Overview
The goal of this project is to predict whether an F1 driver will finish the race or not (DNF) using historical race data. Predicting DNFs can help teams and drivers make strategic decisions during the race, optimize performance, and minimize risks.
We use machine learning models to learn patterns from features like lap speed, total race time, points, and other race-related data. The workflow includes data cleaning, exploratory data analysis (EDA), model training, evaluation, and feature importance analysis.

Idea 
In F1 races, knowing which drivers are likely to not finish (DNF) a race can provide strategic advantages for teams and analysts.
Teams can make better pit stop and strategy decisions.
Analysts can assess risks associated with drivers’ performance.
Machine learning can help predict DNFs by analyzing historical data, performance metrics, and race conditions.

Dataset
Source: f1_dnf.csv
Key columns:
fastestLapSpeed – speed of the driver’s fastest lap
milliseconds – total race time in milliseconds
laps – number of completed laps
points – points scored by driver
target_finish – target variable (0 = Finished, 1 = DNF)
Other driver, race, and team-related features

Dataset shape: (number of rows x number of columns)

Data Preprocessing
Before training the model, the dataset was cleaned and processed:
Converted fastestLapSpeed and milliseconds to numeric types.
Filled missing values:
fastestLapSpeed → mean
milliseconds → median
points → 0
laps → 0
Dropped duplicate rows.

Encoded categorical columns using Label Encoding to convert text into numbers.

Exploratory Data Analysis (EDA)
EDA helps us understand patterns and relationships in the data:
Distribution plots: Histogram of fastestLapSpeed to see the overall spread.
Boxplots: Show points distribution by target finish (Finish vs DNF).
Correlation heatmap: Identify relationships between numerical features.
Observed which features might be strong predictors of DNFs.

Modeling
We trained two machine learning models for prediction:
1. Logistic Regression
Why chosen: Simple, fast, and works well when the relationship between features and target is mostly linear.
Pros: Easy to interpret, baseline performance.
Cons: Cannot capture complex, non-linear relationships.

2. Random Forest Classifier
Why chosen: Can handle non-linear relationships and complex patterns between features.
Pros: Handles numeric & categorical features, provides feature importance, reduces overfitting by averaging many decision trees.
Cons: Slower than Logistic Regression, more computationally intensive.

Model Evaluation Metrics
For both models, we use multiple metrics to get a complete picture:
Accuracy – How many predictions are correct overall
Precision – How many predicted DNFs were actually DNFs
Recall – How many actual DNFs were correctly detected
F1 Score – Balance between precision and recall

Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	0.XX	0.XX	0.XX	0.XX
Random Forest	0.XX	0.XX	0.XX	0.XX

Random Forest generally performs better, especially in detecting DNFs, and provides insights on important features.

Visualizations
Confusion Matrix (Random Forest) – Shows where the model predicts correctly or incorrectly.
Feature Importance Plot – Highlights the most influential features for predicting DNFs.
Predicted vs Actual Scatter Plot – Visualizes how well model predictions match actual outcomes.

Conclusion
Logistic Regression gives a quick baseline.
Random Forest captures complex relationships, performs better overall, and provides feature importance insights.

Multiple metrics (Precision, Recall, F1) are important because DNFs are critical events; predicting them accurately is more valuable than just overall accuracy.

TASK 4:
Reflections on AI Hallucinations and Reliability
Overview
Reading The Hallucinations Leaderboard helped me understand that AI hallucinations are not just random mistakes—they are measurable phenomena that researchers can study. The paper introduces two key concepts:
Factuality – How true the AI’s output is.
Faithfulness – How well the AI sticks to the instructions it was given.

Key Insights
Models trained to follow instructions become more faithful, but that doesn’t always make them more factual. In other words, AI can listen carefully yet still “make things up.”
Larger models often know more real facts, but they can also sound extremely confident even when wrong.
Confidence does not equal correctness. Just because AI sounds sure doesn’t mean it is right—similar to a friend who speaks confidently but is mistaken.

Implications
AI confidence can be dangerous, especially in critical areas like medical advice. A confident but wrong AI can cause real harm.
There’s a need for models that can check their own answers or admit uncertainty, making them safer and more reliable.
Accuracy and honesty are just as important as intelligence in AI. In a way, humans can also learn from this: being confident is not the same as being correct.

Takeaways
AI needs to be both smart and humble.
Measuring hallucinations systematically helps us understand where and why AI goes wrong.
Developing AI that knows its limits is crucial for safe deployment in real-world tasks.
