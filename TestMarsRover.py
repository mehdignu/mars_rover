import unittest
from Rover import Rover
class TestMarsRover(unittest.TestCase):

    def test_rotate_left(self):
        rover = Rover('1 2 N')
        rover.rotate_left()
        self.assertEqual("W", rover.cardinalDirection)

    def test_rotate_right(self):
        rover = Rover('1 2 N')
        rover.rotate_right()
        self.assertEqual("E", rover.cardinalDirection)


    def test_move_forward(self):
        rover = Rover('1 2 N')
        rover.move_forward()
        self.assertEqual(3, rover.currentYpos)


    def test_move_forward(self):
        rover = Rover('1 2 N')
        rover.move_forward()
        self.assertEqual("1 3 N", str(rover.currentXpos) + " " + str(rover.currentYpos) + " " + rover.cardinalDirection)

    def test_move_forward(self):
        rover = Rover('1 2 N')
        rover.Move_to_location("LMLMLMLMM")
        self.assertEqual("1 3 N", str(rover.currentXpos) + " " + str(rover.currentYpos) + " " + rover.cardinalDirection)


    def test_move_forward_2(self):
        rover = Rover('3 3 E')
        rover.Move_to_location("MMRMMRMRRM")
        self.assertEqual("5 1 E", str(rover.currentXpos) + " " + str(rover.currentYpos) + " " + rover.cardinalDirection)


if __name__ == '__main__':
    unittest.main()