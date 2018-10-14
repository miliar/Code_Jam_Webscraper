from pprint import pprint


def read_list_of(numtype):
    return map(numtype, raw_input().split())

def calculate(a, b, k):
    count = 0
    for i in xrange(a):
        for j in xrange(b):
            if i & j < k:
                count+=1
    return count


def main():
    for case_number in xrange(int(raw_input())):
        a, b, k = read_list_of(int)

        result = calculate(a, b, k)

        print 'Case #%d: %s' % (case_number+1, result)

main()
#
# print calculate(3,4,2) == 10
# print calculate(4,5,2) == 16
# print calculate(7,8,5) == 52
# print calculate(45, 56, 35) == 2411
# print calculate(103, 143, 88) == 14377