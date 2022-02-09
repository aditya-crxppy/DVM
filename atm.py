import logging

logging.basicConfig(filename = 'atm_log.log',
	level = logging.DEBUG,
	format = '%(asctime)s : %(levelname)s : %(message)s')



#creating the ATM class
class ATM:

	def __init__(self, card_no, name, pin, balance):
		self.card_no = card_no
		self.name = name
		self.pin = pin
		self.balance = balance

	def get_name(self):
		return self.name

	def get_card_no(self):
		return self.card_no

	def get_pin(self):
		return self.pin

	def get_balance(self):
		return self.balance

	def get_all(self):
		print("""Name: {}
Card Number: {}
Balance: {}""".format(ATM.get_name(self), ATM.get_card_no(self), ATM.get_balance(self)))
		return 0

	def deposit(self, amount):
		self.balance = str(int(self.balance) + int(amount))
		print("Money deposited, remaining balance is {}".format(ATM.get_balance(self)))
		logging.info("{} deposited, new balance : {}, cardID : {}".format(amount, ATM.get_balance(self), ATM.get_card_no(self)))

	def withdraw(self, amount):
		if amount > self.balance:
			print("Insufficient balance")
		else:
			self.balance = str(int(self.balance) - int(amount))
			print("Money withdrawn, remaining balance is {}".format(ATM.get_balance(user)))
			logging.info("{} withdrawn, new balance : {}, cardID : {}".format(amount, ATM.get_balance(self), ATM.get_card_no(self)))	

	#class method to add user to the .txt file
	def add_user(self):
			file = open("user_list.txt","a+")
			file.write(self.get_card_no() + "\t" + self.get_name() + "\t" + self.get_pin() + "\t" + self.get_balance() + "\n")
			file.close()

	#class method to retrieve user info from the .txt file and store it in an instance 'user'
	def search(temp_card_no):
		get_lines = []
		words = []
		i = 0

		try:
			file = open("user_list.txt","r+")
			for line in file:
				get_lines.append(line)
			file.seek(0, 0)
		
			for line in get_lines:
				words = line.split("\t")
				if temp_card_no == words[0]:
					global user
					user = ATM(temp_card_no, words[1], words[2], words[3])
					i = 1
				else:
					file.write(line)
			file.truncate()
			file.close()
		except:
			pass

		if i == 0:
			return False



print("""******************
WELCOME TO THE ATM
******************""")

#Since we can't actually insert a card, we are using card number instead
#We create a while loop to check if the card number entered is numerical

j = 0
while j == 0:
	temp_card_no = input("Please enter your card number to begin: ")
	if temp_card_no.isdigit():
		j = 1
	else:
		print("Invalid entry")



#This class method searches if user already exists. If user doesn't exist, gives a prompt to create a new account
while ATM.search(temp_card_no) == False:
	print("""\nYour card number is not registered, please select an option:
	1. Re-enter card number
	2. Register new account""")
	choice = input("Enter your choice: ")

	if choice == "1":
		temp_card_no = input("\nRe-enter your card number: ")

	elif choice == "2":	
		temp_name = input("\nEnter full name: ")
		j=0
		while j==0:
			temp_pin = input("Enter a 4-digit pin: ")
			if temp_pin.isdigit() and len(temp_pin) == 4:
				j=1
			else:
				print("Invalid Entry")
		user = ATM(temp_card_no, temp_name, temp_pin, "0")
		print("Account Created\n{}".format(ATM.get_all(user)))
		logging.info("New account created cardID : {}".format(ATM.get_card_no(user)))
		ATM.add_user(user)


#adding the user info to the instance
ATM.search(temp_card_no)

temp_pin=input("Please enter your pin:")


#Checks if the users pin is correct and proceeds to the main UI
if temp_pin == ATM.get_pin(user):
	logging.info("User has logged in, cardID : {}".format(ATM.get_card_no(user)))

	while True:
		choice = input("""\nWelcome {}, please select an option:
	1. View Balance
	2. Deposit Money
	3. Withdraw Money
	4. View Account Details
	5. Exit\n""".format(user.name))
		
		if choice == "1":
			print("\nYour account balance is {}".format(ATM.get_balance(user)))
		
		elif choice == "2":
			i = 0	
			while i == 0:
				amount = input("\nEnter the amount of money to deposit: ")
				if amount.isdigit():
					i = 1
				else:
					print("Invalid Entry")
			ATM.deposit(user,amount)
		
		elif choice == "3":
			i = 0
			while i == 0:
				amount = input("\nEnter the amount of money to withdraw: ")
				if amount.isdigit():
					i = 1
				else:
					print("Invalid Entry")
			ATM.withdraw(user,amount)
		
		elif choice == "4":
			ATM.get_all(user)
		
		elif choice == "5":
			logging.info("User has logged out, cardID : {}\n".format(ATM.get_card_no(user)))
			break
		
		else:
			print("Invalid Entry\n")


else:
	print("Invalid pin, process suspended")
ATM.add_user(user)


print("""\n\n***************************
THANK YOU FOR USING THE ATM
***************************""")
