from devices import Light, Fan

# Create devices
light = Light()
fan = Fan()

def show_status():
    print("\n--- Device Status ---")
    print("Light:", light.state)
    print("Fan:", fan.state)

def menu():
    while True:
        print("\nSMART HOME ORCHESTRATOR")
        print("1. Turn ON Light")
        print("2. Turn OFF Light")
        print("3. Turn ON Fan")
        print("4. Turn OFF Fan")
        print("5. Show Status")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            light.turn_on()
            print("Light turned ON")

        elif choice == "2":
            light.turn_off()
            print("Light turned OFF")

        elif choice == "3":
            fan.turn_on()
            print("Fan turned ON")

        elif choice == "4":
            fan.turn_off()
            print("Fan turned OFF")

        elif choice == "5":
            show_status()

        elif choice == "6":
            print("Exiting Smart Home System")
            break

        else:
            print("Invalid choice")

menu()
