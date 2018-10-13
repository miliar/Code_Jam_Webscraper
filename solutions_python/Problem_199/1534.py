class Pancake:

    def __init__(self, state):
        assert state in {"+", "-"}, "Invalid pancake state: {}".format(state)
        self.is_face_up = state == "+"

    def __repr__(self):
        return "+" if self.is_face_up else "-"

    def flip(self):
        self.is_face_up = not self.is_face_up


class PancakeRow:

    def __init__(self, sequence, flipper_width):
        self.pancakes = [Pancake(s) for s in sequence]
        self.flipper_width = flipper_width
        self.number_of_flips = 0

    def __repr__(self):
        return "Pancakes({})".format(self.sequence())

    def sequence(self):
        return "".join([str(p) for p in self.pancakes])

    def reduce(self):
        """
        Reduce the pancakes list, eliminating all of the pancakes at the
        edges that are already the right way up. We don't need to worry about
        these, since an edge pancake the correct way up would have to be flipped
        twice, making the flip redundant.
        """
        first = self._index_of_first_upside_down_pancake(self.pancakes)
        if first is not None:
            last = (
                self._number_of_pancakes() -
                self._index_of_first_upside_down_pancake(reversed(self.pancakes))
            )
            self.pancakes = self.pancakes[first:last]
        else:
            # No pancakes are upside-down
            self.pancakes = []

    def flip_left(self):
        """
        Flip the left hand flipper_width pancakes. Error if there are not enough
        pancakes in the stack.
        """
        assert self._number_of_pancakes() >= self.flipper_width, \
            "Not enough pancakes in stack to flip"
        self.number_of_flips += 1
        for pancake in self.pancakes[:self.flipper_width]:
            pancake.flip()

    def correct_pancakes(self):
        """
        :return: Iterate through the pancakes, reducing the problem, and then
        flipping the outermost pancakes as far as possible
        """
        self.reduce()
        while self._number_of_pancakes() >= self.flipper_width:
            self.flip_left()
            self.reduce()

    def solution(self):
        """
        :return: Either None if no solution is possible, or the number of flips
        required to put all pancakes the correct way up
        """
        self.correct_pancakes()
        if self._number_of_pancakes() == 0:
            return self.number_of_flips
        else:
            # No solution could be found
            return None

    def output_solution(self):
        """
        :return: The output string that should communicate the solution
        """
        solution = self.solution()
        if solution is None:
            return "IMPOSSIBLE"
        else:
            return str(solution)

    # Helper functions
    # ~~~~~~~~~~~~~~~~

    def _number_of_pancakes(self):
        return len(self.pancakes)

    @staticmethod
    def _index_of_first_upside_down_pancake(pancakes):
        """
        :param pancakes: An iterable of pancakes
        :return: The index of the first pancake that is the wrong way up
        """
        try:
            return next(i for i, p in enumerate(pancakes) if not p.is_face_up)
        except StopIteration:
            return None


num_lines = int(input())
for i in range(1, num_lines + 1):
    sequence, width_str = input().split(" ")
    pancake_row = PancakeRow(sequence, int(width_str))
    print("Case #{}: {}".format(i, pancake_row.output_solution()))
