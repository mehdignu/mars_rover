class Rover:
    """Rover class"""
    
    def __init__(self, location):
        self.currentXpos = int(location.split()[0])
        self.currentYpos = int(location.split()[1])
        self.cardinalDirection = location.split()[2]
    
    def rotate_left(self):
        if (self.cardinalDirection == "N"):
            self.cardinalDirection = "W"
            return

        if (self.cardinalDirection == "E"):
            self.cardinalDirection = "N"
            return

        if (self.cardinalDirection == "S"):
            self.cardinalDirection = "E"
            return
        
        if (self.cardinalDirection == "W"):
            self.cardinalDirection = "S"
            return


    def rotate_right(self):
        if (self.cardinalDirection == "N"):
            self.cardinalDirection = "E"
            return

        if (self.cardinalDirection == "E"):
            self.cardinalDirection = "S"
            return

        if (self.cardinalDirection == "S"):
            self.cardinalDirection = "W"
            return
        
        if (self.cardinalDirection == "W"):
            self.cardinalDirection = "N"
            return

    def move_forward(self):
        if (self.cardinalDirection == "N"):
            self.currentYpos += 1
            return

        if (self.cardinalDirection == "E"):
            self.currentXpos += 1
            return

        if (self.cardinalDirection == "S"):
            self.currentYpos -= 1
            return
        
        if (self.cardinalDirection == "W"):
            self.currentXpos -= 1
            return

    def Move_to_location(self, instructions):
        commands = list(instructions)
        
        for command in commands:
            if (command == "L"):
                self.rotate_left()

            if (command == "R"):
                self.rotate_right()

            if (command == "M"):
                self.move_forward()