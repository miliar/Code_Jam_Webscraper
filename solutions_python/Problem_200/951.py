def is_tidy(n):
    n = str(n)
    for i in xrange(len(n)):
        if i == len(n) - 1:
            return True
        if int(n[i]) > int(n[i+1]):
            return False
    print "Shouldn't happen"


def solve(n):
    multiplier = 1
    current_index = len(str(n)) - 1
    while True:
        if is_tidy(n):
            return int(n)
        current_digit = int(str(n)[current_index])
        n -= multiplier * (current_digit + 1)

        multiplier *= 10
        current_index -= 1
    print "Shouldn't happen (2)"

t = int(raw_input())

for i in xrange(1, t+1):
    n = int(raw_input())
    print "Case #{}: {}".format(i, solve(n))