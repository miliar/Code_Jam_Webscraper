import sys

def active_after_snap(pos, snap):
    return (snap - (2**pos) + 1) % (2**pos) == 0

def solve(inpath, outpath):
    f = open(inpath, 'r')
    topline = f.readline() # will go unused
    cases = f.readlines()
    f.close()

    f = open(outpath, 'w')
    i = 0
    for case in cases:
        i += 1
        snappers, snaps = map(int, case.split(' '))
        output = 'Case #%d: %s' % (i,
            'ON' if active_after_snap(snappers, snaps)
            else 'OFF')
        # print output
        f.write(output + '\n')
    return

if __name__ == "__main__":
    inpath = sys.argv[1]
    outpath = sys.argv[2]
    solve(inpath, outpath)