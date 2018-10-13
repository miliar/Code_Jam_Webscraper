def _game_helper(gaps, people):
    """
    This is a helper function for the game. Returns the
    max and min of the gap in stalls.
    """
    # base case 1: when there are only gaps of 1,
    # there are no gaps after putting in a person
    if (1,) * len(gaps) == gaps:
        return (0, 0)

    else:

        # get the max of the gaps
        max_of_gap = max(gaps)

        # remove from tuple
        max_index = gaps.index(max_of_gap)
        gaps = gaps[:max_index] + gaps[max_index + 1:]

        # divide by 2
        middle = max_of_gap // 2

        # if even
        if max_of_gap % 2 == 0:

            # ready to output if people - 1 == 0
            if people - 1 == 0:
                gaps = gaps + (middle, middle - 1)
                return (middle, middle - 1)

            # if still need to put people in
            else:
                if middle - 1 != 0:
                    gaps = gaps + (middle, middle - 1)
                else:
                    gaps = gaps + (middle,)
                return _game_helper(gaps, people - 1)

        # if odd
        else:
            gaps += (middle, middle)
            # ready to output
            if people - 1 == 0:
                return (middle, middle)
            else:
                return _game_helper(gaps, people - 1)


def game(stalls, people):
    """ (int, int) -> tuple of (int, int)
    Given stalls and the number of people,
    return a tuple of the maximum of the gap between
    two occupied seats on the left and right,
    and the minimum of the gap between two occupied seats
    on the left and right.

    REQ: stalls >= people
    REQ: people > 0

    Examples
    ========

    These are the examples given in the Google Codejam
    handout.

    >>> game(4, 2)
    (1, 0)
    >>> game(5, 2)
    (1, 0)

    Steps:
    xoooooox
    xooxooox
    xooxoxox
    >>> game(6, 2)
    (1, 1)
    >>> game(1000, 1000)
    (0, 0)
    >>> game(1000, 1)
    (500, 499)

    Furthermore, if more stalls and people are used

    Config:
    xooooxooooox
    Output:
    >>> game(10, 1)
    (5, 4)

    Config:
    xooooxooxoox
    >>> game(10, 2)
    (2, 2)

    Config:
    xoxooxooxoox
    >>> game(10, 3)
    (2, 1)

    Config:
    xoxxoxooxoox
    >>> game(10, 4)
    (1, 0)

    Config:
    xoxxoxxoxoox
    >>> game(10, 5)
    (1, 0)
    """
    # stalls is equal to the number of people, then there
    # are nothing left
    if stalls == people:
        return (0, 0)
    else:
        middle_left = stalls // 2

        # if stalls are even
        if stalls % 2 == 0:
            max_min = (middle_left, middle_left - 1)

        # if stalls are odd
        else:
            max_min = (middle_left, middle_left)

        # if the number of people is greater than 1
        if people - 1 > 0:
            max_min = _game_helper(max_min, people - 1)

    # return the result
    return max_min



if __name__ == "__main__":
    t = int(input())
    for i in range(1, t + 1):
        stalls, people = [int(s) for s in input().split(" ")]
        max_gap, min_gap = game(stalls, people)
        print("Case #{}: {} {}".format(i, max_gap, min_gap))
