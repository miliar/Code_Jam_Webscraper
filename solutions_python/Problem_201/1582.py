from math import log


class StallProblem:
    """
    The people can be split up into levels, where each level contains a
    successive power of 2 people, so the first level contains 1, the second 2,
    the third 4 and so on.
    """

    def __init__(self, n_stalls, n_people):
        self.n_stalls = n_stalls
        self.n_people = n_people

    def level_of_last_person(self):
        return int(log(self.n_people, 2) + 1)

    def size_of_last_level(self):
        """
        :return: The size of the level of the last person (N.B. This could be
        more than the number of people available), it is just the level size
        """
        return 2 ** (self.level_of_last_person() - 1)

    def n_people_before_last_level(self):
        return self.size_of_last_level() - 1

    def average_spaces_per_gap_at_last_level(self):
        # The number of people at cubicles once the last level joins
        last_level_size = self.size_of_last_level()
        return (self.n_stalls - self.n_people_before_last_level()) / \
            last_level_size

    def gap_size_for_last_joiner(self):
        avg_gap_size = self.average_spaces_per_gap_at_last_level()
        smaller_space = int(avg_gap_size)
        if smaller_space == avg_gap_size:
            # All gaps at this level are the same size
            space = avg_gap_size
        else:
            larger_space = smaller_space + 1
            n_larger = (avg_gap_size - smaller_space) * self.size_of_last_level()
            if self.n_people - self.n_people_before_last_level() > n_larger:
                space = smaller_space
            else:
                space = larger_space
        return space

    def adjacent_spaces(self):
        gap_size = self.gap_size_for_last_joiner()
        average_gap = (gap_size - 1) / 2
        lower_gap = int(average_gap)
        if lower_gap == average_gap:
            return [lower_gap, lower_gap]
        else:
            return [lower_gap + 1, lower_gap]

    def output_solution(self):
        spaces = self.adjacent_spaces()
        return "{} {}".format(*spaces)


num_lines = int(input())
for i in range(1, num_lines + 1):
    n_stalls, n_people = [int(x) for x in input().split(" ")]
    stalls = StallProblem(n_stalls, n_people)
    print("Case #{}: {}".format(i, stalls.output_solution()))
