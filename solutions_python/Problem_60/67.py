import sys

def solve(vel, pos, bdist, howmany, time):
    if howmany == 0:
        return 0
    pos.reverse()
    vel.reverse()
    swaps = 0
    marks = []
    for idx, (p, v) in enumerate(zip(pos, vel)):
        if ((bdist - p) / float(v)) <= time:
            marks.append(idx)
    if len(marks) < howmany:
        return "IMPOSSIBLE"
    counter = 0
    def between(idx):
        return idx - counter 
    for idx in marks[:howmany]:
        swaps += between(idx)
        counter += 1
    return swaps

def main():
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        n, k, b, t = [int(x) for x in sys.stdin.readline().strip().split()]
        p = [int(x) for x in sys.stdin.readline().strip().split()]
        v = [int(x) for x in sys.stdin.readline().strip().split()]
        print "Case #%d:" % (i+1), solve(v, p, b, k, t)

if __name__ == "__main__":
    main()
