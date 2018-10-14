import sys

def readline():
    return sys.stdin.readline().strip()

def compute_wp(data):
    v1 = sum(1 for x in data if x == '1')
    v2 = sum(1 for x in data if x == '0' or x == '1')
    return (v1, v2)

def compute_owp(data, wp):
    total = 0
    sum = 0.0
    #print data
    for idx, val in enumerate(data):
        if val == '.':
            continue
        total += 1
        v1, v2 = wp[idx]
        if val == '0' and v1 != 0:
            v1 -= 1
        v2 -= 1
        #print v1, v2
        sum += float(v1) / v2
    return sum / total

def compute_oowp(data, owp):
    total = 0
    sum = 0.0
    for idx, val in enumerate(data):
        if val == '.':
            continue
        total += 1
        sum += owp[idx]
    return sum / total

def compute_rpi(wp, owp, oowp):
    return 0.25 * (float(wp[0]) / wp[1]) + 0.50 * owp + 0.25 * oowp

def solve(data):
    wp = [compute_wp(x) for x in data]
    owp = [compute_owp(x, wp) for x in data]
    oowp = [compute_oowp(x, owp) for x in data]
    #print wp, owp, oowp

    rpi = [compute_rpi(a, b, c) for (a, b, c) in zip(wp, owp, oowp)]
    for val in rpi:
        print "%.8f" % (val)

def main():
    n_inputs = int(readline())
    for i in range(n_inputs):
        N = int(readline())
        data = []
        for j in range(N):
            data.append(list(readline()))
        print "Case #%d:" % (i + 1)
        solve(data)

if __name__ == "__main__":
    main()
