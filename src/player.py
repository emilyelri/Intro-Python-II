# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print("You cannot move in that direction.")
