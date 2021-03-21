#
# Lenworth Taylor
# This program is meant to help keep people, specfically women, safe at nights/days with the assistance of people in their neighbourhood and the police.

print("Hello! Welcome to Eagle Eye!\nThis program is here to help make you feel safer through the assistance of people and the police.")
print()
print("Here's an explanation of how this works.")
print()
print("Whenever you're in a situation where you feel uncomfortable coming home alone at night or daytime, you can active the app that lets the eagle watchers know that you're in the area and to keep an eye out.")
print("Eagle watchers are those who sign up to assist those who feels unsafe at night or day when going home. Once you active eagle eye and turn on your locator, eagle viewers in the area will be notified and they can choose to assist you or not. \nYou can choose to be an eagle watcher or an eagle whenever you open the program.")
print("If they do decide to assist you, a request will be sent for you to approve or deny. There must be two eagle watchers at all times to prevent targeting. The police is also connected and will know the identity of the eagle watchers who were assigned to you.")
print("Once you are home and you feel safe, you must end the transaction by pressing 'Eagle Landed' and entering the 5 digit passcode that you will set up later on. \nIf you forget to do this after a certain amount of time, the police will be alerted and will give you a call.")
print("If after a few attempts there is no response, the police will active your locator and proceed to your location.")
print("If you don't feel comfortable having strangers being your eagle watcher, you can add your friends in the area and then set your locator to private. This way only your added friends will get notified and only they can watch out for you.")

print()
print("To get started, please fill out the information below. \nPlease note that any information provided will be kept private and will not be shared with anyone.")
print()








# This code is to get the information of the user.

na_me= input("Name: ")
age= int(input("Age: "))
gen_der= input("Gender: ")
addr_ess= input("Address: ")
print()
if age >= 18:
    print ("Status: Adult")
else:
    print("Status: Minor")

print()

# This line of code is to gather emergency contact information
emergency = 2
print("Please provide us with two emergency contact information")
for x in range(emergency):
    em_contactname = input("Enter emergency contact name: ")
    em_contactnum = int(input("Number: "))

print("Thank you!")

print()

#These code are to create and account and passcode for the user.
print("Hello",(na_me)+'!')
print("Let's go ahead and set up an account and passcode for you.")
print()
email= input("Enter your email: ")
user_name= input("Enter a username: ")
pass_word= input("Enter a password: ")
pass_word2= input("Enter password again: ")
#This code is to verify that the user entered the password that they wanted to and didn't make any errors that could cause then issues in the future.
print(pass_word==pass_word2)
print()
print("Congratulations! You have successfully created an account. \nNow create a passcode.")
print()

#This code is to create a passcode for the user.

pass_code= int(input("Please enter a passcode.(Only use numbers): "))
pass_code2= int(input("Enter passcode again: "))
#This code is to ensure that the user entered the passcode that they wanted correctly.
print(pass_code==pass_code2)
print()
print()
print("Great!. Use this code to enable and disable each Eagle Eye transaction!")
print("Try not to share your code with anyone. This way only you can disable or enable your locator.")
print()

#These line of codes is to start a free trial for the user.
print("New members of Eagle Eye are awarded a free 3 month membership. After the trial is up, you will be charged $10 monthly. If you wish to start your free trial now, please enter you card information below.")
print()
Card_number = int(input("Card Number: "))
exp_date = input("Valid Thru: ")
name_oncard = input("Name on card: ")
bill_address = input("Billing address: ")
print()

#This determine if the users is qualified to recieve the student discount
set_price = (10.00)
discount = (0.50)
college_status = input("Are you currently a college student? Please type yes or no: ")
if college_status == 'yes':
    discounted_price = set_price * discount
    print("Congrats! You've are eligible for the student discount. Your monthly bill will now be $", format(discounted_price, "0.2f"), sep='')
elif college_status == 'no':
    print(" You're monthly bill is $ ", format(set_price, "0.2f"), sep='')




print("Your free trial with Eagle Eye begins now and ends in 3 months! If you cancel the trial anytime before then, you will not be charged.")
print()
print("Welcome to EAGLE EYE",(na_me)+'! Stay safe!')
print()
print()

print("This following line of code is to do calculations for the owner of the program.")
print()

price = float(input("Enter cost per user: "))
num_ofusers = int(input("Number of users: "))
expenses = float(input("Enter expenses: "))
interest_per = float(input("Enter interest expense percentage (use decimals): "))
tax_per = float(input("Enter taxes percentage (use decimals): "))
#calculation formulas
sales = price * num_ofusers
profit = sales - expenses
profit_mar = profit / sales
interest_exp = profit * interest_per
tax_exp = (profit - interest_exp) * tax_per
net_income = profit - interest_exp - tax_exp
# The '*' is used to multiply the price and total number of members to get the sales.
print()
print("Sales= Price * Number of Users")
print("Number of members=",num_ofusers)
print("Price per user= $",(price), sep='')
print("Sales= $", format(sales,"0.2f"), sep='')
print()

#Next lines of code is to calculate profit
print("Profit= Sales - Expenses")
print("Revenue= $", format(sales,"0.2f"), sep='')
print("Expenses= $",(expenses), sep='')
print("Profit= $", format(profit,"0.2f"), sep='')
print()

#These lines of code is to calculate the Net Income
print("Net Income= Profit - Interest Expense - Tax")
print("Profit= $",(profit), sep='')
print("Interest expense= $",(interest_exp), sep='')
print("Taxes= $",format(tax_exp,"0.2f"), sep='')
print("Net income= $", format(net_income,"0.2f"), sep='')
print()

#This line of code is used to calculate the profit margin
print("Profit Margin= Profit / Sales")
print("Profit= $",(profit), sep='')
print("Sales= $",(sales), sep='')
print("Profit margin= $", format(profit_mar, "0.2f"), sep='')
print()
print("Goodbye for now!")

# Codes we need to add to the program

#This line of code is for customer to rate their experience with the eagle watcher
eagle_ratings = float(input("Enter eagle rating ranging from 1 - 10: "))
valid_rating = False
while valid_rating == False:
    if eagle_ratings <=10 and eagle_ratings>=8:
        print("Excellent Eagle Watcher!")
        valid_rating = True
    elif eagle_ratings <8 and eagle_ratings>=6:
        print("Great Eagle Watcher.")
        valid_rating = True
    elif eagle_ratings <6 and eagle_ratings>=4:
        print("Good Eagle Watcher.")
        valid_rating = True
    elif eagle_ratings <4 and eagle_ratings>=0:
        print("Poor Eagle Watcher.")
        valid_rating = True
    else:
        eagle_ratings = float(input("Rating is out of range. Please try again: "))

# This line of code creates a function to tell if an account needs to be suspended
num_ofreports = 0
def eagle_report(num1):
    if num1 >= 3:
        print("This eagle account will be suspended until further notice")
#This line of code reports a user
report = input("Would you like to report this eagle? press 'y' for yes and 'n' for no.")
valid_input = True
while valid_input == True:
    if report == 'y':
        num_ofreports += 1
        suspend_acc = eagle_report(num_ofreports)
        print("Thanks for letting us know.")

        valid_input = False

    elif report == 'n':
        print("Okay!")
        valid_input = False
    else:
        if report != 'y' or report != 'n':
            report = input("Invalid selection. Please try again by pressing 'y' for yes and 'n' for no")



























