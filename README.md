# Scholarship Rule Learning System

A Python CLI mini project that uses the **Sequential Covering Algorithm** to learn scholarship eligibility rules from student data and predict whether a new student is eligible for a scholarship.

## Project Overview

This project demonstrates how a machine learning rule-learning algorithm can learn simple decision rules from a dataset.

The system analyzes student information such as:

* CGPA
* Attendance
* Family Income
* Backlogs
* Scholarship status

It learns rules from students whose scholarship status is already known and uses those rules to predict the scholarship status of a new student.

## Algorithm Used

**Sequential Covering Algorithm**

Sequential Covering learns classification rules one by one.

In this project, the algorithm:

1. Finds eligible students.
2. Creates a possible rule.
3. Checks wrongly covered students.
4. Selects a better rule.
5. Removes students already covered.
6. Learns another rule for remaining students.
7. Uses the learned rules for prediction.

## Example Learned Rules

The program learns rules similar to:

```text
If CGPA >= 7.3 AND Backlogs = 0
THEN Scholarship = Eligible
```

and:

```text
If CGPA >= 7.3 AND Attendance >= 87
THEN Scholarship = Eligible
```

The exact rules depend on the dataset.

## Technologies Used

* Python
* Pandas
* CSV Dataset
* Command Line Interface (CLI)

## Project Structure

```text
scholarship/
│
├── scholarship_predictor.py
├── dataset.csv
└── README.md
```

### `scholarship_predictor.py`

Contains the main Python program, Sequential Covering algorithm, rule learning and scholarship prediction.

### `dataset.csv`

Contains the student records used for learning the scholarship rules.

### `README.md`

Contains the documentation of the project.

## How to Run

### 1. Install Pandas

Open the terminal and run:

```bash
pip install pandas
```

### 2. Run the program

```bash
python scholarship_predictor.py
```

## Program Menu

```text
1. Learn Scholarship Rules
2. Predict Scholarship
3. Exit
```

### Option 1: Learn Scholarship Rules

The program analyzes the dataset and learns scholarship eligibility rules.

### Option 2: Predict Scholarship

The user enters:

* CGPA
* Attendance
* Number of Backlogs

The program checks the learned rules and displays:

```text
Scholarship: Eligible
```

or:

```text
Scholarship: Not eligible
```

### Option 3: Exit

Closes the program.

## Sample Prediction

Input:

```text
Enter your CGPA: 7.5
Enter your attendance: 90
Enter your number of backlogs: 1
```

Output:

```text
Scholarship: Eligible
```

## Learning Process

The project follows this basic process:

```text
Student Dataset
      ↓
Separate Eligible / Not Eligible
      ↓
Generate Rule
      ↓
Check Wrongly Covered Students
      ↓
Select Better Rule
      ↓
Remove Covered Students
      ↓
Learn Next Rule
      ↓
Store Learned Rules
      ↓
Predict New Student
```

## Objective

The main objective of this project is to understand and implement the **Sequential Covering Algorithm** through a simple real-world scholarship prediction problem.

## Future Improvements

The project can be extended by:

* Adding more student attributes
* Learning more rules automatically
* Adding a graphical user interface
* Adding more rule evaluation measures
* Using a larger dataset

## Author

**Preetham K P**

AIML Student
