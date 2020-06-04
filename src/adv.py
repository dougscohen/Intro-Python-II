from room import Room
from player import Player
import textwrap

wrapper = textwrap.TextWrapper(width=50) 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = input("Please select your player name: ")
print('\n')
player_1 = Player(new_player, room['outside'])

# Write a loop that:
while (True):
# * Prints the current room name
    current_room = player_1.current_room
    print(f"\nCurrent Room: {current_room.name}")

# * Prints the current description (the textwrap module might be useful here).
    word_list = wrapper.wrap(text = current_room.description)
    [print(line) for line in word_list]
    print('----------------------------------')

# * Waits for user input and decides what to do.
    selection = input("Which direction would you like to move?\nnorth - south - east - west\n")
    direction = selection.lower()[0]

# If the user enters a cardinal direction, attempt to move to the room there.
    if direction in ['n', 's', 'e', 'w']:
        player_1.move_player(direction)

    # If the user enters "q", quit the game.
    elif selection in ['quit', 'q', 'exit']:
        print("Thanks for playing!")
        break
    else:
        print("*** Not a valid input. You remain in current room ***")
        print("Please select a direction or quit the game (q)")

