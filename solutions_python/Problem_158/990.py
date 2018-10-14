def is_possible(x, r, c):
    if x == 1:
        return False
    elif r * c % x != 0:
        return True
    elif x == 3:
        return r == 1 or c == 1
    elif x == 4:
        return r < 3 or c < 3
    return False


for t in range(input()):
    print "Case #%s:" % str(t + 1),
    x, r, c = map(int, raw_input().split())
    if is_possible(x, r, c):
        print "RICHARD"
    else:
        print "GABRIEL"
