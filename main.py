# TODO: 01
# Get information from the user:
from art import logo
print(logo)
names_bids = {}
more_person = True
while more_person:
    name = input("What's you name? \n").capitalize()
    bid = int(input('Enter your bid: $'))
    any_other = input('Is there any body else: ').upper()
    names_bids[name] = bid

    if any_other == 'NO':

        more_person = False
        big_bid = 0
        winner = ''
        for key in names_bids:
            bid_amount = names_bids[key]
            if big_bid < bid_amount:
                big_bid = bid_amount
                winner = key
        print(f"The winner is {winner} with bid ${big_bid}")
