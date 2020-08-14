# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import RoomItems
class Player:
    def __init__(self,current_room):
        self.current_room = current_room
    def __str__(self):
        return f"{self.current_room}"
    def canMove(self,direction):
        if direction == "n" and self.current_room.n_to is not None:
            return True
        if direction == "e" and self.current_room.e_to is not None:
            return True
        if direction == "w" and self.current_room.w_to is not None:
            return True
        if direction == "s" and self.current_room.s_to is not None:
            return True
        else:
            return False

    def movePlayer(self,direction):
        if self.canMove(direction):
            if direction == "n":
                self.current_room = self.current_room.n_to
                print(f"You moved to {self.current_room}\n")
            elif direction == "e":
                self.current_room = self.current_room.e_to
                print(f"You moved to {self.current_room}\n")
            elif direction == "w":
                self.current_room = self.current_room.w_to   
                print(f"You moved to {self.current_room}\n") 
            elif direction == "s":
                self.current_room = self.current_room.s_to    
                print(f"You moved to {self.current_room}\n") 
        else:
            print("\n-----No room in that location \n")