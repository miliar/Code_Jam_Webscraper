__author__ = 'bingorabbit'

def primaDonna():
    """
    >>> primaDonna()
    Case #1: 0
    Case #2: 1
    Case #3: 2
    Case #4: 0
    """
    file = open('A-large.in')

    no_test_cases = int(file.readline())
    for test_item in range(no_test_cases):
        test_case = file.readline().split()
        max_shyness = int(test_case[0])
        audience = test_case[1]
        suggested_audience = (max_shyness + 1) * '1'
        if audience == suggested_audience:
            no_of_invited_attendees = 0
        else:
            no_of_invited_attendees = 0
            number_of_standing_attendees = 0
            for shyness_level, c in enumerate(audience):
                if number_of_standing_attendees >= shyness_level:
                    number_of_standing_attendees += int(c)
                else:
                    no_of_invited_attendees += shyness_level - number_of_standing_attendees
                    number_of_standing_attendees += int(c) + shyness_level - number_of_standing_attendees
        print("Case #{0}: {1}".format(test_item+1, no_of_invited_attendees))

    file.close()


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    primaDonna()