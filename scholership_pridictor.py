import pandas as pd


# Load student dataset
df = pd.read_csv("dataset.csv")


# ---------------------------------------------------------
# Sequential Covering Algorithm
# ---------------------------------------------------------
def sequential_covering(df):

    # Separate eligible and not eligible students
    eligible_students = df[df["Scholarship"] == "Eligible"]
    not_eligible_students = df[df["Scholarship"] == "Not Eligible"]

    # Find minimum CGPA among eligible students
    min_cgpa = eligible_students["CGPA"].min()

    # Store learned rules
    rules = []

    # -----------------------------------------------------
    # Rule 1: CGPA only
    # -----------------------------------------------------
    rule1 = "If CGPA >= " + str(min_cgpa) + \
            " THEN Scholarship = Eligible"

    # Find not eligible students wrongly covered by Rule 1
    wrongly_covered = not_eligible_students[
        not_eligible_students["CGPA"] >= min_cgpa
    ]

    print("\nWrongly covered by Rule 1:")
    print(wrongly_covered)

    print("\nNumber of wrongly covered:", len(wrongly_covered))

    # -----------------------------------------------------
    # Rule 2: CGPA + Backlogs
    # -----------------------------------------------------
    rule2 = "If CGPA >= " + str(min_cgpa) + \
            " AND Backlogs = 0 THEN Scholarship = Eligible"

    # Check wrongly covered students by Rule 2
    wrongly_covered2 = not_eligible_students[
        (not_eligible_students["CGPA"] >= min_cgpa) &
        (not_eligible_students["Backlogs"] == 0)
    ]

    print("\nWrongly covered by Rule 2:")
    print(wrongly_covered2)

    print("\nNumber of wrongly covered:", len(wrongly_covered2))

    # Select the rule with fewer wrongly covered students
    if len(wrongly_covered2) < len(wrongly_covered):
        selected_rule = rule2
    else:
        selected_rule = rule1

    rules.append(selected_rule)

    print("\nSelected Rule:")
    print(selected_rule)

    # -----------------------------------------------------
    # Find eligible students covered by selected rule
    # -----------------------------------------------------
    if "Backlogs = 0" in selected_rule:

        covered_students = eligible_students[
            (eligible_students["CGPA"] >= min_cgpa) &
            (eligible_students["Backlogs"] == 0)
        ]

    else:

        covered_students = eligible_students[
            eligible_students["CGPA"] >= min_cgpa
        ]

    print("\nNumber of students covered:", len(covered_students))

    # Remove already covered students
    remaining_students = eligible_students.drop(
        covered_students.index
    )

    print("\nRemaining eligible students:")
    print(remaining_students)

    # -----------------------------------------------------
    # Learn another rule if students are still remaining
    # -----------------------------------------------------
    if len(remaining_students) > 0:

        print("\nMore rules are required.")

        remaining_students = learn_next_rule(
            remaining_students,
            rules
        )

    # Check whether all eligible students are covered
    if len(remaining_students) == 0:

        print("\nAll eligible students are covered.")
        print("No more rules are required.")

    # Display all learned rules
    print("\nLearned Rules:")

    for i, rule in enumerate(rules, start=1):
        print(i, ".", rule)

    return min_cgpa, rules


# ---------------------------------------------------------
# Learn the next rule
# ---------------------------------------------------------
def learn_next_rule(remaining_students, rules):

    print("\nLearning next rule...")

    # Find minimum CGPA and attendance
    min_cgpa_next = remaining_students["CGPA"].min()
    min_attendance = remaining_students["Attendance"].min()

    # Create Rule 3
    rule3 = (
        "If CGPA >= " + str(min_cgpa_next) +
        " AND Attendance >= " + str(min_attendance) +
        " THEN Scholarship = Eligible"
    )

    print("\nNew Rule:")
    print(rule3)

    # Get not eligible students
    not_eligible_students = df[
        df["Scholarship"] == "Not Eligible"
    ]

    # Check wrongly covered students
    wrongly_covered3 = not_eligible_students[
        (not_eligible_students["CGPA"] >= min_cgpa_next) &
        (not_eligible_students["Attendance"] >= min_attendance)
    ]

    print("\nWrongly covered by Rule 3:")
    print(wrongly_covered3)

    print(
        "\nNumber of wrongly covered:",
        len(wrongly_covered3)
    )

    # Find remaining eligible students covered by Rule 3
    covered_by_rule3 = remaining_students[
        (remaining_students["CGPA"] >= min_cgpa_next) &
        (remaining_students["Attendance"] >= min_attendance)
    ]

    print(
        "\nNumber of students covered by Rule 3:",
        len(covered_by_rule3)
    )

    # Add Rule 3 to learned rules
    rules.append(rule3)

    # Remove covered students
    remaining_students = remaining_students.drop(
        covered_by_rule3.index
    )

    print("\nRemaining students after Rule 3:")
    print(remaining_students)

    return remaining_students


# ---------------------------------------------------------
# Predict scholarship for a new student
# ---------------------------------------------------------
def predict_scholarship(
    cgpa,
    attendance,
    backlogs,
    min_cgpa,
    rules
):

    # Check each learned rule
    for rule in rules:

        # Check Rule 1 / Rule 2
        if "Backlogs = 0" in rule:

            if cgpa >= min_cgpa and backlogs == 0:
                return "Eligible"

        # Check CGPA + Attendance rule
        elif "CGPA >=" in rule and "Attendance >=" in rule:

            # Get CGPA threshold from the rule
            cgpa_part = rule.split("CGPA >=")[1]
            rule_cgpa = float(
                cgpa_part.split("AND")[0].strip()
            )

            # Get Attendance threshold from the rule
            attendance_part = rule.split("Attendance >=")[1]
            rule_attendance = float(
                attendance_part.split("THEN")[0].strip()
            )

            # Check whether student satisfies the rule
            if (
                cgpa >= rule_cgpa
                and attendance >= rule_attendance
            ):
                return "Eligible"

    # If no rule matches
    return "Not eligible"


# ---------------------------------------------------------
# Main CLI Program
# ---------------------------------------------------------
def main():

    print("\n========================================")
    print("   SCHOLARSHIP RULE LEARNING SYSTEM")
    print("========================================")

    # Variables to store learned information
    min_cgpa = None
    rules = None

    while True:

        print("\n1. Learn Scholarship Rules")
        print("2. Predict Scholarship")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        # ---------------------------------------------
        # Option 1: Learn rules
        # ---------------------------------------------
        if choice == "1":

            print("\nLearning Scholarship Rules...")

            min_cgpa, rules = sequential_covering(df)

        # ---------------------------------------------
        # Option 2: Predict scholarship
        # ---------------------------------------------
        elif choice == "2":

            # Rules must be learned first
            if rules is None:

                print(
                    "\nPlease learn the scholarship "
                    "rules first."
                )

            else:

                cgpa = float(
                    input("Enter your CGPA: ")
                )

                attendance = float(
                    input("Enter your attendance: ")
                )

                backlogs = int(
                    input("Enter your number of backlogs: ")
                )

                result = predict_scholarship(
                    cgpa,
                    attendance,
                    backlogs,
                    min_cgpa,
                    rules
                )

                print("\nScholarship:", result)

        # ---------------------------------------------
        # Option 3: Exit
        # ---------------------------------------------
        elif choice == "3":

            print(
                "\nThank you for using "
                "Scholarship Rule Learning System."
            )

            break

        # ---------------------------------------------
        # Invalid option
        # ---------------------------------------------
        else:

            print(
                "\nInvalid choice. "
                "Please enter 1, 2, or 3."
            )


# Start the program
main()

