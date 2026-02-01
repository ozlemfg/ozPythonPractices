# Create an Account with user name and password
# user name is alphanumeric and between 5-10 char
# password is min 6 max 10 char, contains at least 1 capital letter and 1 digital
# login attempt is max 3

def set_username():
	return input("define your user name: ")

# check if the set username is valid
def valid_username():
	while True:
		userName = set_username()
		valid = True

		if not (5 <= len(userName) <= 10):
			print("X Username must be 5-10 characters long")
			valid = False

		if not userName.isalnum():
			print("X Username must be alphanumeric!")
			valid = False

		if valid:
			print("Username accepted")
			return userName


def set_password():
	password = input("set your password: ")
	return password

# check if the set pwd is valid
def check_password():

	while True:
		pwd = set_password()
		valid = True


		if  not 6 <= len(pwd) <= 10:
			print("pwd must be 6-10 char length")
			valid = False

		if not any(char.isdigit() for char in pwd):
			print("pwd should contain at least 1 digit")
			valid = False

		if not any(char.isupper() for char in pwd):
			print("should contain at least 1 capital letter")
			valid = False

		if valid:
			print("Password set successfully:")
			return pwd

def login(stored_username, stored_pwd):
	attempts = 3

	while attempts > 0:
		user = input("enter your username: ")
		pwd = input("enter your password: ")

		if user == stored_username and pwd == stored_pwd:
			print("Login successful :) ")
			return

		attempts = attempts -1
		print(f"Wrong credentials! you have {attempts} left to login. ")

	print("Account locked")

your_user_name = valid_username()
your_password = check_password()

print(f"your username is: {your_user_name} and your password is: {your_password}")

print("LOGIN WITH YOUR CREDENTIALS")
login(your_user_name, your_password)


