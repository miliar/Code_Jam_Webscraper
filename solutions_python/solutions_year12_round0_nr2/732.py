import sys, string

def solve(N, S, p, scores):
    normal = 0
    strange = 0
    for score in scores:
        best = score/3
        if score % 3: best +=1
        if best >= p:
            normal += 1
        elif score >= 2:
            best = (score+1)/3 + 1
            if best >= p:
                strange += 1
    return normal + min(S, strange)

def main(args):
    f = file(args[1])
    ncases = int(f.readline())
    for i in range(ncases):
        line = f.readline()
        line = line.rstrip()
        parts = line.split()
        nums = map(int, parts)
        N, S, p = nums[0:3]
        scores = nums[3:]
#        if len(scores) != N: print "Mismatch"
        ans = solve(N, S, p, scores)
        sys.stdout.write("Case #%d: %d\n" % (i+1, ans))

if __name__ == "__main__":
    main(sys.argv)