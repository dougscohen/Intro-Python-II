# Write a class to hold player information, e.g. what room they are in
# currently.

from exceptions import MoveError

class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"Player '{self.name}' is currently in {self.current_room}."

    def move_player(self, direction):
        
        try:
            future_room = getattr(self.current_room, '{}_to'.format(direction))
            
            if future_room == None:
                raise MoveError(self.current_room, direction)

            self.current_room = future_room

        except MoveError as e:
            print('Oops! Not permitted to move that direction at this time.')

    # def add_item(self):


if __name__ == "__main__":
    
    player1 = Player("SNOOP doug", "foyer")

    print(player1)