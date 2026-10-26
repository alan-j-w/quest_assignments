import csv
import os

def validate_record(name, date, status):

    if name == "":
        return False

    if len(date) != 10:
        return False

    if date[4] != "-" or date[7] != "-":
        return False

    year = date[0:4]
    month = date[5:7]
    day = date[8:10]

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if month < 1 or month > 12:
        return False

    if day < 1 or day > 31:
        return False

    if status != "Present" and status != "Absent":
        return False

    return True


def read_attendance():

    records = []

    if os.path.exists("attendance.csv") == False:

        print("Warning: attendance.csv was not found.")
        print("Please create the file and try again.")

        return records

    with open("attendance.csv", "r", newline="") as file:

        reader = csv.reader(file)

        header = next(reader, None)

        row_number = 1

        for row in reader:

            row_number = row_number + 1

            if len(row) != 3:

                print("Warning: Row", row_number, "has missing fields.")

                continue

            name = row[0].strip()
            date = row[1].strip()
            status = row[2].strip()

            if validate_record(name, date, status):

                record = {
                    "employee_name": name,
                    "date": date,
                    "status": status
                }

                records.append(record)

            else:

                print("Warning: Row", row_number, "is invalid.")

    return records


def calculate_attendance(records):

    attendance = {}

    for record in records:

        name = record["employee_name"]
        status = record["status"]

        if name not in attendance:

            attendance[name] = {
                "present": 0,
                "absent": 0,
                "total": 0,
                "percentage": 0
            }

        if status == "Present":

            attendance[name]["present"] = attendance[name]["present"] + 1

        elif status == "Absent":

            attendance[name]["absent"] = attendance[name]["absent"] + 1

        attendance[name]["total"] = attendance[name]["total"] + 1

    for name in attendance:

        present = attendance[name]["present"]
        total = attendance[name]["total"]

        if total > 0:

            percentage = (present / total) * 100

        else:

            percentage = 0

        attendance[name]["percentage"] = percentage

    return attendance


def identify_low_attendance(attendance):

    low_attendance = []

    for name in attendance:

        percentage = attendance[name]["percentage"]

        if percentage < 75:

            low_attendance.append(name)

    return low_attendance


def display_attendance(attendance):

    print("\n========== EMPLOYEE ATTENDANCE SUMMARY ==========")

    print("-" * 60)

    print("Employee\tPresent\tAbsent\tTotal\tAttendance")

    for name in attendance:

        present = attendance[name]["present"]
        absent = attendance[name]["absent"]
        total = attendance[name]["total"]
        percentage = attendance[name]["percentage"]

        print(
            name,
            "\t",
            present,
            "\t",
            absent,
            "\t",
            total,
            "\t",
            format(percentage, ".2f") + "%"
        )

    low_attendance = identify_low_attendance(attendance)

    print("\nEmployees below 75% attendance:")

    if len(low_attendance) == 0:

        print("No employees below 75%.")

    else:

        for name in low_attendance:

            percentage = attendance[name]["percentage"]

            print(name, "-", format(percentage, ".2f") + "%")

def generate_report(attendance):

    with open("attendance_report.txt", "w") as file:

        file.write("EMPLOYEE ATTENDANCE REPORT\n")

        file.write("=" * 40 + "\n\n")

        for name in attendance:

            present = attendance[name]["present"]
            absent = attendance[name]["absent"]
            total = attendance[name]["total"]
            percentage = attendance[name]["percentage"]

            file.write("Employee: " + name + "\n")

            file.write("Present days: " + str(present) + "\n")

            file.write("Absent days: " + str(absent) + "\n")

            file.write("Total recorded days: " + str(total) + "\n")

            file.write(
                "Attendance percentage: "
                + format(percentage, ".2f")
                + "%\n"
            )

            if percentage < 75:

                file.write("Status: BELOW 75%\n")

            else:

                file.write("Status: Meets attendance threshold\n")

            file.write("\n")

        low_attendance = identify_low_attendance(attendance)

        file.write(
            "Employees below 75% attendance: "
            + str(len(low_attendance))
            + "\n"
        )

    print("Attendance report generated successfully.")


def append_attendance():

    name = input("Employee name: ").strip()

    date = input("Date (YYYY-MM-DD): ").strip()

    status = input("Status (Present/Absent): ").strip()

    if status.lower() == "present":

        status = "Present"

    elif status.lower() == "absent":

        status = "Absent"

    else:

        print("Invalid status. Enter Present or Absent.")

        return

    if validate_record(name, date, status):

        file_exists = os.path.exists("attendance.csv")

        with open("attendance.csv", "a", newline="") as file:

            writer = csv.writer(file)

            if file_exists == False:

                writer.writerow(["employee_name", "date", "status"])

            writer.writerow([name, date, status])

        print("Attendance record added successfully.")

        print("Existing records have been preserved.")

    else:

        print("Invalid attendance record.")

        print("Please check the employee name and date.")


def analyze_attendance():

    records = read_attendance()

    if len(records) == 0:

        print("No valid attendance records found.")

    else:

        attendance = calculate_attendance(records)

        display_attendance(attendance)


while True:

    print("\n========== EMPLOYEE ATTENDANCE SYSTEM ==========")

    print("1. Analyze Attendance")

    print("2. Add Attendance Record")

    print("3. Generate Report")

    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        analyze_attendance()

    elif choice == "2":

        append_attendance()

    elif choice == "3":

        records = read_attendance()

        if len(records) == 0:

            print("No valid attendance records found.")

        else:

            attendance = calculate_attendance(records)

            generate_report(attendance)

    elif choice == "4":

        print("Thank you for using the Employee Attendance System.")

        break

    else:

        print("Invalid choice. Please select 1, 2, 3, or 4.")