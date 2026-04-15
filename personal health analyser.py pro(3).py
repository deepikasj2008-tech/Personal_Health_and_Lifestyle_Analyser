daily_data = [] 

def add_daily_log(): 

    print("\n=== Add Daily Log ===") 

    day = input("Day: ") 

    sleep = float(input("Hours of sleep: ")) 

    water = int(input("Cups of water: ")) 

    steps = int(input("Steps walked: ")) 

    screen = float(input("Screen time (hours): ")) 

    meals = int(input("Number of meals: ")) 

    daily_data.append({"day": day, "sleep": sleep, "water": water, "steps": steps, "screen": screen, "meals": meals}) 

    print(f"{day} log added.") 

def health_score(log): 

    score = 0 

    score += 2 if 7 <= log["sleep"] <= 9 else 1 

    score += 2 if log["water"] >= 8 else 1 

    score += 3 if log["steps"] >= 10000 else 2 if log["steps"] >= 5000 else 1 

    score += 2 if log["screen"] <= 2 else 1 

    score += 2 if 3 <= log["meals"] <= 5 else 1 

    return score 

def daily_summary(): 

    if not daily_data: print("No logs yet."); return 

    print("\n=== Daily Summary ===") 

    for log in daily_data: 

        print(f"{log['day']}: Health Score = {health_score(log)}/11") 

def weekly_summary(): 

    if not daily_data: print("No logs yet."); return 

    n = len(daily_data) 

    total_sleep = sum(d["sleep"] for d in daily_data) 

    total_water = sum(d["water"] for d in daily_data) 

    total_steps = sum(d["steps"] for d in daily_data) 

    total_screen = sum(d["screen"] for d in daily_data) 

    total_meals = sum(d["meals"] for d in daily_data) 

    print("\n=== Weekly Summary ===") 

    print(f"Avg Sleep: {total_sleep/n:.1f}, Water: {total_water/n:.1f}, Steps: {total_steps/n}, Screen: {total_screen/n:.1f}, Meals: {total_meals/n:.1f}") 

    if total_sleep/n < 7: print("Sleep less, improve rest!") 

    if total_water/n < 8: print("Drink more water!") 

    if total_steps/n < 5000: print("Walk more daily!") 

    if total_screen/n > 2: print("Reduce screen time!") 

def main(): 

    print("=== Personal Health & Lifestyle Analyzer ===") 

    while True: 

        print("\n1. Add Daily Log\n2. Daily Summary\n3. Weekly Summary\n4. Exit") 

        choice = input("Enter choice: ") 

        if choice == "1": add_daily_log() 

        elif choice == "2": daily_summary() 

        elif choice == "3": weekly_summary() 

        elif choice == "4": break 

        else: print("Invalid choice!") 

if __name__ == "__main__": 

    main()
