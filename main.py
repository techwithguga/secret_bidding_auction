from replit import clear
import art

print(art.logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    #{"Guga": 123, "Jaja": 321}}
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

    
while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    print(bids)
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        #from replit module to clear the console
        clear()

