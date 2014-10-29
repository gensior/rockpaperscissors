import random

CHOICES = ('R','P','S')
wins = 0
losses = 0

def main():
	games = 0
	print("Let's play rock paper scissors.")
	print("Enter rock(R), paper(P), or scissors(S)")
	user = input("or (Q) to exit:")
	while(True):
		user = user.upper()
		if(user == "R" or user == "P" or user == "S"):
			print("You selected:", fulltext(user))
			comp = computer()
			print("The computer selected:", fulltext(comp))
			games += 1
			game = compare(user, comp)
			result = results(game)
			print(result)
			user = input("Play again (R/P/S/Q)?:")
			continue
		elif(user == "Q"):
			print("Thanks for playing!")
			print("In", games, "game(s)...")
			print("You won", wins, "time(s)")
			print("You lost", losses, "time(s)")
			break
		user = input("Try again (R/P/S/Q):")

def computer():
	return random.choice(CHOICES)

def fulltext(choice):
	output = ""
	if (choice == "R"):
		output = "Rock"
	if (choice == "P"):
		output = "Paper"
	if (choice == "S"):
		output = "Scissors"
	return output

def compare(user, comp):
	# If the user selects 'Rock'
	if (user == "R"):
		# Rock beats scissors
		if (comp == "S"):
			return 1
		# Paper beats rock
		elif (comp == "P"):
			return -1
 	# If the user selects 'Paper'
	if (user == "P"):
		# Paper beats rock
		if (comp == "R"):
			return 1
		# Scissors beat paper
		elif (comp == "S"):
			return -1
	# If the user selects 'Scissors'
	if (user == "S"):
		# Scissors beats paper
		if (comp == "P"):
			return 1
		# Rock beas scissors
		elif (comp == "R"):
			return -1
	# Otherwise it's a tie
	return 0

def results(result):
	global wins
	global losses
	if (result == 1):
		wins += 1
		return ("You win!!")
	elif (result == -1):
		losses += 1
		return ("You lose :(")
	else:
		return ("You tied.")

if __name__ == '__main__':
    main()