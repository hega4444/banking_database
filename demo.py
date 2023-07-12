import json
import datetime

ERROR = -1

# Function toload clients from the json file
def load_clients():
    # open file (in read mode by default)
    with open('clients.json') as file:
        #load JSON data from the file
        data = json.load(file)
    return data['clients']

# Function save clients to the json file
def save_clients(clients):
    # open the file in write mode
    with open("clients.json","w") as file:
        # Dump (write) the clients to the json file
        json.dump({'clients': clients}, file)

def customer_exists(clients, client_id):
    #checks if the client_id is valid
    found = False
    for client in clients:
        if client['client_id'] == client_id:
            found = True
            break
    return found

def get_age(dob):
    # convert the dob from string to datetime object
    date_of_birth = datetime.datetime.strptime(dob, '%Y-%m-%d')
    # get current date
    today = datetime.datetime.today()
    #calculcation of age
    age = today.year - date_of_birth.year
    return age

def add_client(clients, name, dob, balance):
    # determining id of last client
    client_id = clients[-1]["client_id"] + 1
    # adding new client
    clients.append({
        "client_id":client_id,
        "name":name,
        "dob":dob,
        "balance":balance
    })
    #saving updated clients list to JSON file
    save_clients(clients)

def update_client(clients, client_id, name=None, dob=None, balance=None):
    # loop through client list

    if not customer_exists(clients, client_id):
        print('The client ID does not exist. Please check your input.')
        return ERROR

    for client in clients:
        # select client by id
        if client['client_id'] == client_id:
            # if name is provided, update clients name
            if name:
                client['name'] = name
            # if dob is provided, update clients dob
            if dob:
                client['dob'] = dob
            # if balance is provided, update clients balance
            if balance:
                client['balance'] = balance
            break
    # save updated clients list to JSON file
    save_clients(clients)

def delete_client(clients, client_id):
    # loop through client list

    if not customer_exists(clients, client_id):
        print('The client ID does not exist. Please check your input.')
        return ERROR

    for client in clients:
        # select client by id
        if client['client_id'] == client_id:
            # delete client
            del client
            # end loop to avoid unnecessary looping
            break
    # save updated client list to JSON
    save_clients(clients)

def display_client(clients, client_id):
    # looping through clients (list of dicts loaded from JSON file)

    if not customer_exists(clients, client_id):
        print('The client ID does not exist. Please check your input.')
        return ERROR

    for client in clients:
        # select client by id
        if client['client_id'] == client_id:
            # print client information
            print(f'Client ID {client["client_id"]}')
            print(f'Client Name {client["name"]}')
            print(f'Client DOB {client["dob"]}')
            print(f'Client Age {get_age(client["dob"])}')
            print(f'Client Balance {client["balance"]}')

# Function to display the total amount of money in the bank
def display_total(clients):
    # Calculate the total balance by adding up the balance of each client
    total = sum(client['balance'] for client in clients)
    # Print the total balance
    print('Total bank balance:', total)

def get_balance(clients, client_id):
    #get the current balance of a client
    if not customer_exists(clients, client_id):
        print('The client ID does not exist. Please check your input.')
        return ERROR

    balance = 0
    for client in clients:
        if client['client_id'] == client_id:
            balance = client['balance']
            break
    return balance


def make_transfer(clients, client_id_from, client_id_to, amount):

    #Execute a transfer between two accounts

    if not customer_exists(clients, client_id_from):
        print('The source account does not exist. Please check your input.')
        return ERROR
    if not customer_exists(clients, client_id_to):
        print('The destination account does not exist. Please check your input.')
        return ERROR
    if client_id_to == client_id_from:
        print('Source and destination are the same. Check your input.')
        return ERROR
    balance_source = get_balance(clients, client_id_from)
    if  balance_source < amount:
        print('Scource account has not enough funds. Please check your input.')
        return ERROR
    
    balance_source = balance_source - amount
    balance_destination = get_balance(clients, client_id_to) + amount

    update_client(clients, client_id_from, balance = balance_source)
    update_client(clients, client_id_to, balance = balance_destination)

    print('Transaction executed sucsessfully.')
    return 0

def make_vip(clients):
    #make customer VIP if balance is over 10000
    count_vip = 0
    for client in clients:
        if int(client['balance']) > 10000:
            client['VIP'] = True
            count_vip += 1

    save_clients(clients)
    return count_vip


