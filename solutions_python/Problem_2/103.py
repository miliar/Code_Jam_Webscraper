import sys

def tt(x):
    t = x.split(":")
    return int(t[0])*60 + int(t[1])

def improve(left):
    global match_left, match_right, adj, n, seen
    if seen[left]: return False
    seen[left] = True
    for right in adj[left]:
        if match_right[right] == -1 or improve(match_right[right]):
            match_left[left] = right
            match_right[right] = left
            return True
    return False

def pro(inp = sys.stdin, outp = sys.stdout):
    global match_left, match_right, adj, n, seen
    cases = int(inp.readline())
    for cc in range(cases):
        t = int(inp.readline())
        journey = []
        na, nb = map(int, inp.readline().split())
        for i in range(na):
            st, en = inp.readline().strip().split()
            journey.append((tt(st), tt(en), 0))
        for i in range(nb):
            st, en = inp.readline().strip().split()
            journey.append((tt(st), tt(en), 1))
        journey.sort()
        n = len(journey)
        match_left = [-1] * n
        match_right = [-1] * n
        adj = [[] for i in range(n)]
        for i in range(n):
            for j in range(i+1,n):
                if journey[i][2] != journey[j][2] and journey[i][1] + t <= journey[j][0]:
                    adj[i].append(j)
        for i in range(n):
            seen = [False] * n
            improve(i)
        na, nb = 0, 0
        for i in range(n):
            if match_right[i] == -1:
                if journey[i][2] == 0:
                    na += 1
                else:
                    nb += 1
        print na, nb
        outp.write("Case #%d: %d %d\n" % (cc+1, na, nb))
        
def r(infile, outfile):
    a = open(infile, "r")
    b = open(outfile, "w")
    pro(a, b)
    a.close()
    b.close()

#r("b-small-attempt2.in", "b-small.out")
#r("inp.txt", "outp.txt")
r("b-large.in", "b-large.out")
