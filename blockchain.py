# Initializing blockchain list
blockchain = []


def get_last_blockcain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    """" Append a new value as well as the last blockchain value
       :transaction_amount: The amount that should be added.
       :last_transaction: The last blockchain transaction (default(1))
    """
    if (last_transaction) == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input('Your transaction amount: '))
    return user_input


def get_user_choice():
    user_input = input('Your choise: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)




while True:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('q: Quit')
    user_choise = get_user_choice()
    if user_choise == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockcain_value())
    elif user_choise == '2':
        print_blockchain_elements()
    elif user_choise == 'q':
        break
    else:
        print('Input is invalid')
    print('Choise registred')

print('Done!')
