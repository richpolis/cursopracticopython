import sys

clients = [
    {
        'name': 'Pablo', 
        'company': 'Google', 
        'email': 'pablo@gmail.com', 
        'position': 'Software enginner'
    }, 
    {
        'name': 'Ricardo', 
        'company': 'Facebook', 
        'email': 'ricardo@garagecoders.net', 
        'position': 'Data engineer'
    }
]

welcome_client = True

def create_client(client_email: str = None) -> bool:
    global clients

    assert client_email, f'Client email is required'

    if not search_client(client_email):
        client = {
            'name': _get_client_field('name'), 
            'company': _get_client_field('company'), 
            'email': client_email, 
            'position': _get_client_field('position')
        }
        clients.append(client)
    else:
        print('Client email alredy is in the client\'s list')
        return False
    return True


def list_clients() -> None:
    global clients 

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
                uid=idx, 
                name=client['name'], 
                company=client['company'], 
                email=client['email'], 
                position=client['position']
            ))


def update_client(client_email:str = None) -> bool:
    global clients 
    
    assert client_email, f'Client email is required'

    if search_client(client_value=client_email):
        index = _get_index_client(client_email)
        client = clients[index]
        updated_client = {
            'name': _get_client_field('name', client['name']), 
            'company': _get_client_field('company', client['company']), 
            'email': _get_client_field('email', client['email']), 
            'position': _get_client_field('position', client['position'])    
        }
        clients[index] = updated_client
    else:
        print('Client email is not in client list')
        return False
    return True


def delete_client(client_email: str = None) -> bool:
    global clients

    assert client_email, f'Client email is required'

    if search_client(client_value=client_email):
        index = _get_index_client(client_email)
        del clients[index]
    else:
        print('Client email is not in client list')
        return False 
    return True


def search_client(client_value: str = None, field_search:str = 'email') -> bool:
    global clients
    
    assert client_value, f'Client {field_search} is required'
    
    for client in clients:
        if client[field_search] != client_value:
            continue
        else:
            return True
    return False


def _print_welcome():
    global welcome_client

    if welcome_client:
        print('\n')
        print('WELCOME TO PLATZI VENTAS')
        print('*' * 50)
        print('What would you like to do today? ')
        welcome_client = False
    else:
        print('\n')
        print('*' * 50)
        print('What is the next action? ')
    print('\n')
    print('[C]reate client')
    print('[R]ead clients')
    print('[U]pdate client')
    print('[D]elete client')
    print('*' * 50)
    print('[S]earch client')
    print('*' * 50)
    print('[E]xit program')


def _is_valid_email(client_email: str) -> bool:
    return len(client_email) > 0 and client_email != 'exit'
        

def _get_client_email() -> str:
    client_email = None

    while not client_email:
        client_email = input('What is the client email?: ')

        if client_email == 'exit':
            client_email == None
            break

    if not client_email:
        sys.exit()

    return client_email


def _get_index_client(client_value: str, field_search: str = 'email') -> int:
    global clients

    for index, client in enumerate(clients):
        if client[field_search] == client_value:
            return index
    return -1



def _get_client_field(field_name:str, current_value: str = '') -> str:
    field = None 

    while not field:
        field = input('What is the client {field_name} {default}? '.format(
                field_name=field_name, 
                default='' if len(current_value) == 0 else f'({current_value}) '
            ))
        if not field and len(current_value) > 0:
            field = current_value

    return field



if __name__ == '__main__':
    
    while True:
        _print_welcome()
        command = input()
        command = command.upper()
        client_email = ''
        
        # todos piden el email, para hacer el proceso
        if command in ['C', 'U', 'D', 'S']:    
            client_email = _get_client_email()

        if _is_valid_email(client_email=client_email):
            if command == 'C': 
                if create_client(client_email=client_email):
                    list_clients()
            elif command == 'U':
                if update_client(client_email=client_email):
                    list_clients()
            elif command == 'D':
                if delete_client(client_email=client_email):
                    list_clients()
            elif command == 'S':
                found = search_client(client_value=client_email)
                if found:
                    print('The client is in the client\'s list')
                else:
                    print(f'The client with email: {client_email} is not in our client\'s list')
            else:
                print('Error')
        elif command == 'R':
            list_clients()
        elif command == 'E':
            print('Exit to the program')
            break



