__author__ = 'alestainer'

def check_if_tidy(number):
    for i in range(len(number) - 1):
        if (number[i] > number[i+1]):
            return False
    return True

def solution(number):
    if (check_if_tidy(str(number))):
        return number
    else:
        return solution(number / 10 - 1) * 10 + 9

t = int(raw_input())
for i in xrange(1, t + 1):
    num = int(raw_input())
    print "Case #{}: {}".format(i, solution(number=num))
