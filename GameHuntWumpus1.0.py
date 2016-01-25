# -*- coding: UTF-8 -*-


"""

First Version of Game Hunt Wumpus 

"""

from random import choice


# Set up cave

cave_numbers = range(1,21)
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)

while player_location == wumpus_location:
	player_location = choice(cave_numbers)

# Welcome Player

print "Welcome to Hunt the Wumpus"
print "You can see",len(cave_numbers)," caves"
print "To play, just type the number"
print "of the cave you wish to enter next"


# Main Game Loop

while True:
	print "You are in cave",player_location
	# Warn if wumpus is nearby
	if (player_location == wumpus_location - 1 or
		player_location == wumpus_location + 1):
		print "I smell wumpus !!!!!"

	# Ask player to pick a cave
	print "Which cave next?"
	player_input = raw_input(">")
	if (not player_input.isdigit() or
		int(player_input) not in cave_numbers):
		print  player_input, "is not a cave"

	else:
		player_location = int(player_input)
		if player_location == wumpus_location:
			print "Aargh!!! You got eaten by a wumpus"
			break

