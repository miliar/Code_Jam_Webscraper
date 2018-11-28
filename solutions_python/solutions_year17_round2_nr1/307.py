from sys import stdin

def get_answer():
    parts = stdin.readline().strip().split()
    d = int(parts[0])
    n = int(parts[1])
    ks = []
    ss = []
    for i in range(n):
        ps = [int(el) for el in stdin.readline().strip().split()]
        ks.append(ps[0])
        ss.append(ps[1])
    t = max([(d - k + 0.0) / s  for (k, s) in zip(ks, ss)])
    return str(d / t)

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        print "Case #{0}: {1}".format(i + 1, get_answer())

if __name__ == "__main__":
    main()
