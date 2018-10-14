
import random

def get_closest_tidy_number(number):
    number = list(str(number)) # strings are immutable in python

    for index in range(len(number)-1):
        charhere = int(number[index])
        nextchar = int(number[index+1])
        if nextchar < charhere:
            number[index] = str(charhere-1)
            for settonineindex in range(index+1,len(number)):
                number[settonineindex] = str(9)

            return get_closest_tidy_number(''.join(number))
    return int(''.join(number))

if __name__ == "__main__":
    assert get_closest_tidy_number(10) == 9
    assert get_closest_tidy_number(132) == 129
    assert get_closest_tidy_number(1000) == 999
    assert get_closest_tidy_number(7) == 7
    assert get_closest_tidy_number(111111111111111110) == 99999999999999999
    with open('B-large.in') as file:
        for casenum,line in enumerate(file):
            if casenum == 0:
                continue
            print("Case #%d: %d" % (casenum,get_closest_tidy_number(int(line))))
