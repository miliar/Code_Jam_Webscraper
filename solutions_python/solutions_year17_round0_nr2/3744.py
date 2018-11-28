
def is_tidy(n):
    str_n = str(n)
    for i in range(len(str_n)-1):
        if int(str_n[i]) > int(str_n[i+1]):
            return False
    return True


def get_last_tidy(N):
    for n in xrange(N, -1, -1):
        if is_tidy(n):
            return n


outp = open("tidy-output3", "w")
cache = {}
cases = []
solutions = []
with open("B-small-attempt0.in") as f:
    skip = True
    case = 0
    for l in f:
        if skip:
            skip = False
        else:
            case += 1
            y = get_last_tidy(int(l))
            print("Case #%d: %d" % (case, y))
            outp.write("Case #%d: %d\n" % (case, y))
