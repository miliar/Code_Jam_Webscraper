#! /usr/bin/python

def find_number_standing_ovation(test_cases):

    more_friends = []
    existing_friends = []

    count = 0
    for x in test_cases:

        test_case = x[1]

        more_friends.append(0)
        existing_friends.append(0)


        length = int(x[0]) + 1
        for i in xrange(1, length):
            existing_friends[count] += int(test_case[i-1])

            if existing_friends[count] + more_friends[count] < i:
                more_friends[count] += i - (existing_friends[count] + more_friends[count])

        count += 1

    return  more_friends



    pass

if __name__ == '__main__':

    count = int(raw_input())

    test_cases = []
    for x in xrange(0, count):
        test_cases.append(raw_input().split(" "))

    result = find_number_standing_ovation(test_cases)

    for x in xrange(1, count+1):
        print("Case #%d: %d" % (x, result[x-1]))