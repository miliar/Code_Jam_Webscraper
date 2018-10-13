def n_snaps(N):
    if N == 0:
        return 0
    else:
        return 2 * n_snaps(N - 1) + 1

PRECOMPUTE_n = [n_snaps(i) + 1 for i in range(31)]

def is_light_on(N, K):
##    n = n_snaps(N) + 1
    n = PRECOMPUTE_n[N]
    if K % n == (n - 1):
        return True
    else:
        return False

def parse_input_and_output(infile, outfile):
    lines = open(infile).readlines()
    R = []
    onoff = ["OFF", "ON"]
    for i, line in enumerate(lines[1:]):
        try:
            t = line.split()
            N = int(t[0])
            K = int(t[1])
            res = int(is_light_on(N, K))
            R.append("Case #%d: %s" % (i + 1, onoff[res]))
        except (IndexError, ValueError):
            pass
    open(outfile, "w").write("\n".join(R))

