class ClientManagementSystem:
    def __init__(self):
        self.client_profiles = {}  # Dictionary to store client profiles

    def log_referral(self, name, location, gp_details):
        if name not in self.client_profiles:
            self.client_profiles[name] = {
                "location": location,
                "gp_details": gp_details,
                "case_folder": [],
                "waiting_list": []
            }
            print(f"New profile created for {name}")
        else:
            print(f"Profile for {name} already exists. Referral not logged as a duplicate.")

    def create_case_folder(self, name, alternative_name):
        if name in self.client_profiles:
            self.client_profiles[name]["case_folder"].append({
                "alternative_name": alternative_name
            })
            print(f"Case folder created for {name} with alternative name: {alternative_name}")
        else:
            print(f"Client profile for {name} does not exist.")

    def add_to_waiting_list(self, name):
        if name in self.client_profiles:
            self.client_profiles[name]["waiting_list"].append(name)
            print(f"{name} added to the waiting list for clinical triage.")
        else:
            print(f"Client profile for {name} does not exist.")

    def print_client_profiles(self):
        print("Client Profiles:")
        for name, profile in self.client_profiles.items():
            print(f"Name: {name}")
            print(f"Location: {profile['location']}")
            print(f"GP Details: {profile['gp_details']}")
            print(f"Case Folder: {profile['case_folder']}")
            print(f"Waiting List: {profile['waiting_list']}")
            print("------------------------")


if __name__ == "__main__":
    client_system = ClientManagementSystem()

    while True:
        print("\nOptions:")
        print("1. Log Referral")
        print("2. Create Case Folder")
        print("3. Add to Waiting List")
        print("4. View Client Profiles")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter client's name: ")
            location = input("Enter client's location: ")
            gp_details = input("Enter GP details: ")
            client_system.log_referral(name, location, gp_details)

        elif choice == "2":
            name = input("Enter client's name: ")
            alternative_name = input("Enter alternative name: ")
            client_system.create_case_folder(name, alternative_name)

        elif choice == "3":
            name = input("Enter client's name: ")
            client_system.add_to_waiting_list(name)

        elif choice == "4":
            client_system.print_client_profiles()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please choose a valid option.")
