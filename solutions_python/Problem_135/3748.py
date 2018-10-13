import unittest
from magic_trick import MagicTrick, MultipleSolutionsException,\
    InvalidAnswerException


class Test(unittest.TestCase):

    def test_dumy(self):
        assert True

    def test_card_found(self):
        trick = MagicTrick()
        arrangement1 = [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]
        ]
        trick.set_first_arrangement(arrangement1)
        trick.set_card_first_row(2)

        arrangement2 = [
                        [1, 2, 5, 4],
                        [3, 11, 6, 15],
                        [9, 10, 7, 12],
                        [13, 14, 8, 16]
        ]
        trick.set_second_arrangement(arrangement2)
        trick.set_card_second_row(3)

        card = trick.get_chosen_card()

        self.assertEquals(card, 7)

    def test_multiple_solutions(self):
        trick = MagicTrick()
        arrangement1 = [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]
        ]
        trick.set_first_arrangement(arrangement1)
        trick.set_card_first_row(2)

        arrangement2 = [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]
        ]
        trick.set_second_arrangement(arrangement2)
        trick.set_card_second_row(2)

        self.assertRaises(MultipleSolutionsException, trick.get_chosen_card)

    def test_invalid_answer(self):
        trick = MagicTrick()
        arrangement1 = [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]
        ]
        trick.set_first_arrangement(arrangement1)
        trick.set_card_first_row(2)

        arrangement2 = [
                        [1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]
        ]
        trick.set_second_arrangement(arrangement2)
        trick.set_card_second_row(3)

        self.assertRaises(InvalidAnswerException, trick.get_chosen_card)