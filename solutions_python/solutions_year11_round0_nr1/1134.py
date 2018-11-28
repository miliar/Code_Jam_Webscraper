import unittest

from robots import Robot, seconds_required, next_orange_sequence_index, next_blue_sequence_index, parse_line

class RobotTestCase(unittest.TestCase):

    def test_can_create_a_robot(self):
        orange = Robot()

    def test_robot_can_starts_at_button_1(self):
        self.assertEqual(1, Robot().position)

    def test_robot_forward_should_change_robot_position_to_next_position(self):
        robot = Robot()
        robot.forward()
        self.assertEqual(2, robot.position)

    def test_robot_back_should_change_robot_position_to_after_position(self):
        robot = Robot()
        robot.position = 2
        robot.back()
        self.assertEqual(1, robot.position)

    def test_robot_move_to_should_move_robot_step_by_step(self):
        robot = Robot()
        for i in range(9):
            robot.move_to(10)

        self.assertEqual(10, robot.position)

class SecondsRequiredTestCase(unittest.TestCase):

    def test_forO2B8O1B8O7B6O10B8O4B10_required_28_seconds(self):
        self.assertEqual(28, seconds_required(sequence=['O 2', 'B 8', 'O 1', 'B 8', 'O 7', 'B 6', 'O 10', 'B 8', 'O 4', 'B 10']))
    def test_for_O_1_is_required_1_second(self):
        self.assertEqual(1, seconds_required(sequence=['O 1',]))

    def test_for_O_2_is_required_2_seconds(self):
        self.assertEqual(2, seconds_required(sequence=['O 2',]))

    def test_for_O_1_O_1_is_required_2_seconds(self):
        self.assertEqual(2, seconds_required(sequence=['O 1', 'O 1']))

    def test_for_O_14_is_required_14_seconds(self):
        self.assertEqual(14, seconds_required(sequence=['O 14',]))

    def test_for_B_14_is_required_14_seconds(self):
        self.assertEqual(14, seconds_required(sequence=['B 14',]))

    def test_for_B_1_is_required_1_second(self):
        self.assertEqual(1, seconds_required(sequence=['B 1',]))

    def test_for_B_2_is_required_2_seconds(self):
        self.assertEqual(2, seconds_required(sequence=['B 2',]))

    def test_for_O_2_B_1_B_2_O_4_is_required_6_seconds(self):
        self.assertEqual(6, seconds_required(sequence=['O 2', 'B 1', 'B 2', 'O 4']))

    def test_for_B_2_B_1_is_required_4_seconds(self):
        self.assertEqual(4, seconds_required(sequence=['B 2', 'B 1']))

    def test_for_O_5_O_8_B_100_required_seconds(self):
        self.assertEqual(100, seconds_required(sequence=['O 5', 'O 8', 'B 100']))

class NextOrangeSequenceTestCase(unittest.TestCase):

    def test_next_orange_sequence_index_should_be_0(self):
        self.assertEqual(0, next_orange_sequence_index(['O 2', 'B 1']))

class NextBlueSequenceTestCase(unittest.TestCase):

    def test_next_blue_sequence_index_should_be_0(self):
        self.assertEqual(1, next_blue_sequence_index(['O 2', 'B 1']))


class ParseLineTestCase(unittest.TestCase):

    def test_parse_can_returns_a_sequence(self):
        self.assertEqual(['O 2', 'B 1', 'B 2', 'O 4'], parse_line('4 O 2 B 1 B 2 O 4'))

unittest.main()
