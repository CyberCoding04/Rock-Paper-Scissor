import random
userpoints = 0
comppoints = 0
while True:
	userchoice = input("Enter Your Choice(Rock, Paper, Scissor or any Other to EXIT): ").lower()

	if userchoice == 'rock' or userchoice == 'paper' or userchoice == 'scissor':
		'''If user enter any of the choice'''
		compchoice = random.choice(['rock', 'paper', 'scissor'])
		if userchoice == compchoice:
			print("Match Tie") #Here Match Would Be tie as Both have same choice.
		elif (userchoice == 'paper' and compchoice == 'rock') or (userchoice == 'rock' and compchoice == 'scissor') or (userchoice == 'scissor' and compchoice == 'paper'):
			print("Hurrah! You Wins")
			userpoints +=1 # Adding one to user points
		elif (compchoice == 'paper' and userchoice == 'rock') or (compchoice == 'rock' and userchoice == 'scissor') or (compchoice == 'scissor' and userchoice == 'paper'):
			print("Sorry! Computer Wins")
			comppoints += 1 # Adding one point to computer points

		# Now Printing computer choice and points.
		print(f"Computer:  {compchoice} ")
		print(f"Your Points: {userpoints}    ||    Computer Points: {comppoints}")
	else:
		print("Bye")
		break
