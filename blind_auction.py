logo = """       
       _______
      /       \
     |         |
     |  _______|
     | |       
     | |       
     | |       
     | |   ___
    _|_|__|   |________
   |                   |
   |    Gavel           |
   |___________________|
"""

print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Optional: Implementing a clear function for clearing the console.
def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))  # Convert input to integer
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
