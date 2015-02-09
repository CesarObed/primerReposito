import random
generated = random.randint(1,21)
print generated
number = input("insert number:")
if generated < number:
	print "your number is higher than generated, try again"
elif generated > number:
	print "your number is lower than generated, try again"
elif generated == number:
	print "you win"