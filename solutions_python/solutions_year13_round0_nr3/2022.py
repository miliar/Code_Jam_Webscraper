"""
Google Code Jam 2013
Problem C. Fair and Square
"""

def is_palin(x):
    return str(x) == str(x)[::-1]

def get_fair_palins():
    palins = filter(is_palin, xrange(1, 10**7))
    return filter(is_palin, map(lambda x : x * x, palins))

if __name__ == '__main__':
    fair_palins = get_fair_palins()

    case_number = input()
    for case_id in xrange(case_number):
        a, b = map(int, raw_input().split())
        answer = len(filter(lambda x : a <= x <= b, fair_palins))
        print 'Case #%d: %d' % (case_id + 1, answer)
