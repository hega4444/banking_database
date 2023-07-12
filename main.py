import demo as banking
from demo import ERROR

def main():
    while True:
        print('\n1. Add new client')
        print('2. Update existing client')
        print('3. Delete client')
        print('4. Display client')
        print('5. Display total')
        print('6. Make a transfer')
        print('7. Make VIP')
        print('8. Exit')

        option = int(input('\nSelect an option: '))
        
        if option == 1:
            name    = input("Enter new client name: ")
            dob     = input("Enter new client DOB (YYYY-MM-DD): ")
            balance = float(input("Enter client balance: "))
            banking.add_client(banking.load_clients(), name, dob, balance)
            print("Client added successfully.")
        elif option == 2:
            client_id = int(input("Enter client ID: "))
            name = input("Enter new client name (leave empty to keep current): ")
            dob = input("Enter new client DOB (YYYY-MM-DD) (leave empty to keep current): ")
            balance = input("Enter new client balance (leave empty to keep current): ")

            if banking.update_client(banking.load_clients(), client_id, name, dob, balance) != banking.ERROR:
                print("Client updated successfully.")

        elif option == 3:
            id = int(input('Enter client ID: '))

            if banking.delete_client(banking.load_clients(), id) != banking.ERROR:
                print("Client deleted successfully.")

        elif option == 4:
            id = int(input('Enter client ID: '))
            banking.display_client(banking.load_clients(), id)
        elif option == 5:
            banking.display_total(banking.load_clients())
        elif option == 6:
            client_id_from = int(input("Enter source client ID: "))
            client_id_to = int(input("Enter destination client ID: "))
            amount = int(input("Enter amount of transfer: "))

            banking.make_transfer(banking.load_clients(), client_id_from, client_id_to, amount) 

        elif option == 7:
            count = banking.make_vip(banking.load_clients())
            if count:
                print(f'{count} customers were changed to VIP.')
            else:
                print('No VIP customers identified.')

        elif option == 8:
            break
        else:
            print('Invalid option. Please try again.')

main()