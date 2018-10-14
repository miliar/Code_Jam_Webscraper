import fileinput

def handle_case(s_is):
    people_left = 0
    extras = 0
    for s_i in s_is:
        people_left += s_i - 1
        while people_left < 0:
            extras += 1
            people_left += 1
    return extras

def solve():
    it = fileinput.input()
    num_cases = int(it.next())
    for i,l in enumerate(it):
        s_max,s_is = l.split()
        s_is = [int(x) for x in s_is]
        print "Case #%d: %d" % (i+1,handle_case(s_is))

if __name__ == "__main__":
    solve()
