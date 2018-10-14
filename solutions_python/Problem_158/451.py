def read_list_of(numtype):
    return map(numtype, raw_input().split())


def solve(x, r, c):
    if r < c:
        c, r = r, c

    if x == 1:
        return True
    elif x == 2:
        # 1x1 doesnt fit for 2 reasons
        return r % 2 == 0 or c % 2 == 0
    elif x == 3:
        min_r, min_c = 3, 2
        if c < min_c or r < min_r:
            return False

        return c % 3 == 0 or r % 3 == 0
    elif x == 4:
        min_r, min_c = 4, 3
        if c < min_c or r < min_r:
            return False

        return True


def main():
    for case_number in xrange(int(raw_input())):
        x, r, c = read_list_of(int)

        result = {True: 'GABRIEL', False: 'RICHARD'}[solve(x, r, c)]

        print 'Case #%d: %s' % (case_number + 1, result)


main()

# t = gabriel, f = richard
# print solve(2,2,2) == True
# print solve(2,1,3) == False
# print solve(4,4,1) == False
# print solve(3,2,3) == True
# print solve(1,1,1) == True
# print solve(1,3,2) == True
#
# print solve(2,1,1) == False
# print solve(2,1,2) == True
# print solve(2,3,4) == True
#
# print solve(3, 3, 3) == True
# print solve(3, 1, 3) == False
# print solve(3, 2, 3) == True
# print solve(3, 4, 4) == False
#
# print solve(4, 4, 3) == True
# print solve(4, 4, 4) == True
# print solve(4, 3, 3) == False
