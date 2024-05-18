MINING_REWARD = 10

# Initializing blockchain list
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]
    return amount_recieved - amount_sent

def get_last_blockcain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """" Append a new value as well as the last blockchain value

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
        """
    transaction = {'sender': sender,
                   'recipient': recipient,
                   'amount': amount
                   }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    block = {
            'previous_hash': 'XYZ',
             'index': len(blockchain),
             'transactions': open_transactions
             }
    blockchain.append(block)
    return True


def get_transaction_value():
    tx_recipient = input('Enter the recipient of the trnsaction: ')
    tx_amount = float(input('Your transaction amount: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choise: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    for (index, block) in enumerate(blockchain):
       if index == 0:
           continue
       if block['previous hash'] != hash_block(blockchain[index - 1]):
           return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choise = get_user_choice()
    if user_choise == '1':
        tx_data = get_transaction_value()
        recipeint, amount = tx_data
        # Add the transaction amount to the blockchain
        if add_transaction(recipeint, amount=amount):
            print('Added transaction')
        else:
            print('Transaction failed')
        print(open_transactions)
    elif user_choise == '2':
        if mine_block():
            open_transactions = []
    elif user_choise == '3':
        print_blockchain_elements()
    elif user_choise == '4':
        print(participants)
    elif user_choise == 'q':
        waiting_for_input = False
    elif user_choise == 'h':
        # Make sure you don't try to hack the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    else:
        print('Input is invalid')
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print('Invalid blockchain')
    #     break
    print(get_balance('Max'))
else:
    print('User left')

print('Done!')
