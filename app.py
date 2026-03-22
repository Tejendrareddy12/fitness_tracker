fitness_data = []

def add_activity():
    name = input("Enter activity (Running, Walking, etc): ")
    duration = int(input("Enter duration (minutes): "))
    calories = float(input("Enter calories burned: "))

    activity = {
        "Activity": name,
        "Duration": duration,
        "Calories": calories
    }

    fitness_data.append(activity)
    print("Activity added successfully!\n")

def view_activities():
    if fitness_data == []:
        print("No activities recorded.\n")
        return

    print("\nYour Activities:")
    for activity in fitness_data:
        print(activity)

# CALL FUNCTIONS
add_activity()
view_activities()
