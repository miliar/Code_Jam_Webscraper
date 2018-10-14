import sys

def solve(d, horses):
    finishtimes = []
    for h in horses:
        finishtimes.append((d - h[0]) / h[1])
    return d / max(finishtimes)

if __name__ == '__main__':
    lines = sys.stdin.readlines()
    T = int(lines[0])
    i = 1
    for t in range(1,T+1):
        d, n = (int(x) for x in lines[i].split())
        horses = [ tuple(int(x) for x in l.split()) for l in lines[i+1:i+1+n] ]
        i += n+1
        print('Case #{}: {}'.format(t, solve(d, horses)))

