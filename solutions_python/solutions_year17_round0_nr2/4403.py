def is_tidy(number):
    """
    Given a number, makes sure each digit is >= the previous.
    """
    number = str(number)
    last_seen = number[0]

    for digit in number[1:]:
        if digit < last_seen:
            return False
        last_seen = digit

    return True


def last_tidy(num):
    """
    In order to pass the big case, I think I need to use recrusive backtracking.

    I'm not sure that I want to take that on, I'm sort of lazy, but I can get
    more test cases by solving the easy set first. =)
    """
    while not is_tidy(num):
        num -= 1

    return num


def run():
    # ---- Marshall input/output
    cases = int(raw_input())
    for case in range(0,cases):
        num = int(raw_input())
        print 'Case #{}: {}'.format(case+1, last_tidy(num))

run()

def test_is_tidy():
    cases = [
        (123, True),
        (222, True),
        (322, False),
        (220, False),
        (1, True),
    ]
    for case in cases:
        assert case[1] == is_tidy(case[0])

    print 'LGTM'
