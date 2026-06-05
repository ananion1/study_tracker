# Study Tracker

study_data = []

def add_session():
    subject_name = input("Enter subject name: ")

    try:
        hours = float(input("Enter hours studied: "))
    except ValueError:
        print("Please enter a valid number!")
        return

    session = {
        "subject": subject_name,
        "hours": hours
    }

    study_data.append(session)
    print("Session added successfully!\n")


def view_sessions():
   if len(study_data) == 0:
      print("No study sessions found.\n")
      return


print("Your Study Sessions:")

for session in study_data:
    print(f"Subject: {session['subject']} , Hours: {session['hours']}")

print()


def total_hours():
    total = 0


for session in study_data:
    total += session["hours"]

print(f"\nTotal Hours Studied: {total}\n")


def subject_analysis():
    if len(study_data) == 0:
      print("No data available.\n")
      return


subject_hours = {}

for session in study_data:
    subject = session["subject"]
    hours = session["hours"]

    if subject in subject_hours:
        subject_hours[subject] += hours
    else:
        subject_hours[subject] = hours

print("\nSubject-wise Analysis:")

for subject, hours in subject_hours.items():
    print(f"{subject}: {hours} hours")

print()


while True:
    print("===== STUDY TRACKER =====")
    print("1. Add Study Session")
    print("2. View Sessions")
    print("3. Total Hours")
    print("4. Subject Analysis")
    print("5. Exit")


    choice = input("Choose an option: ")

    if choice == "1":
      add_session()

    elif choice == "2":
      view_sessions()

    elif choice == "3":
      total_hours()

    elif choice == "4":
      subject_analysis()

    elif choice == "5":
      print("Thanks for using Study Tracker!")
    break

else:
    print("Invalid option. Try again.\n")

