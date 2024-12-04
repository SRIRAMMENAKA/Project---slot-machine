import random

name=input("Enter Your Name : ")
UPPER_NAME=name.upper()
print("="*50)
print(f"Hi {UPPER_NAME}!, Welcome To The Slot Machine")
print("HOW TO PLAY:")
print("1. Deposit money to start playing.")
print("2. Choose the number of lines to bet on (1-3).")
print("3. Enter the amount you want to bet per line.")
print("4. Spin the slot machine!")
print("5. Match symbols in a line to win.")
print("6. Winning symbols have different values")
print("="*50)
BET_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLOUM=3


spin_values={
    "A":3,
    "B":3,
    "C":5,
    "D":4,
}
spin_value={
    "A":5,
    "B":2,
    "C":3,
    "D":2, 
}
def check_winning(slots,line,bets,values):
    winnigs=0
    winnig_line=[]
    for lines in range(line):
        symbol=slots[0][lines]
        for win in slots:
            symbol_to_check=win[lines]
            if symbol != symbol_to_check:
                break
        else:
            winnigs+=winnigs+values[symbol]*bets
            winnig_line.append(lines+1)
    return(winnigs,winnig_line)

def spin_of_slot_machine(spinn):
    all_column=[]
    value=[]
    for symbol,count in spinn.items():
        for _ in range(count):
            value.append(symbol)
    
    for _ in range(3):
        new_column=[]
        repeated_column=value[:]
        for _ in range(3):
            value2=random.choice(repeated_column)
            new_column.append(value2)
            repeated_column.remove(value2)
        all_column.append(new_column)
    
    return (all_column)


def prinnt_all_column(all_coloumn):
    for i in range(len(all_coloumn[0])):
        for j in all_coloumn:
            if (i != len(all_coloumn)-i):
                print(j[i],end=" | ")
            else:
                print(j[i],end='')
        print()
        
        
def get_deposit ():   
    while True:                 
        amount=input(f"{UPPER_NAME} let's get started! Please deposite some money to play $: ")
        if amount.isdigit():
            deposit=int(amount)
         
            if deposit > 0:
                break
            else:
                print(f"{UPPER_NAME} your amount will be greater than 0.")
        else:
            print("Enter The Deposit Amount in Numbers : ")
    return deposit

def get_bet ():
    while True:
        bet=input(f"How many lines would you like to bet on? you can bet on  1 to {BET_LINES} lines : ")
        if bet.isdigit():
            bet_value=int(bet)
            if ( 1 <= bet_value <= BET_LINES) :
                break
            else:
                print(f"The Total Lines are {BET_LINES} your Bet is within it.")
        else:
            print("Enter The line value in Numbers.")
    return bet_value
    
def bet_amount():
    while True:
        bet_ammount=input(f"Enter the amount you want to bet on each line (${MIN_BET}-${MAX_BET}) : ")
        if bet_ammount.isdigit():
            bet_ammmount=int(bet_ammount)
            if (MIN_BET <= bet_ammmount <=MAX_BET):
                break
            else:
                print("The Bet Amount Exceeds Your deposit Amount ")
        else:
            print("Enter The line value in Numbers.")        
    return bet_ammmount


def game(moneey,a):
   
    bet_lines=get_bet()
       
    while True:
        betamount=bet_amount()
        spin=spin_of_slot_machine(spin_values)
        wins,win_line=check_winning(spin,bet_lines,betamount,spin_value) 
        total_amount=betamount*bet_lines
        if (total_amount >moneey):
            print(f"you dont have enough money for this bet$ {betamount},your deposited amount is $ {moneey}")
            
        else:
            break       
          
    print(f"The amount You deposited is ${a[0]}",f"The Number of lines you Betted is {bet_lines}",f"The Total Betted Money is {total_amount}",sep="\n")
    print("Spinning the reels... Good luck!!")
    spinned=prinnt_all_column(spin)
    if wins != 0:
        print(f"congratulations, {UPPER_NAME}! You won ${wins}!")
        print(f"You won on the following lines",*win_line)
    else:
        print("Better luck next time!")
    return moneey - total_amount


def main():
    a=[]
    money=get_deposit()
    a.append(money)
    while True:
        balance=game(money,a)
        print(f"your current balance is ${balance}", f"of ${a[0]}")
        user_ans=input('To Continue Press Enter - (To Quit Press "Q" )')
        if (user_ans == ("q")) or (balance==0):
            print(f"Thank you for playing, {UPPER_NAME}! Your final balance is ${balance}.")
            print("Come back soon for more spins!")
            print("="*50)
            break
        else:
            money=balance


       
         
main()        
