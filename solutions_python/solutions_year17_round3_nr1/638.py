import math

def output(t, res):
    casestr = "Case #" + str(t+1) +": "
    status = str(res) if res != None else "IMPOSSIBLE"
    outputLine = casestr+status
    print outputLine



def main():
    T = int( raw_input() )
    pi = math.pi
    for t in xrange(T):
        N, K = map(int, raw_input().split(' '))
        pans = []
        for n in xrange(N):
            R, H = map(int, raw_input().split(' '))
            pans.append([R, H])

        pans.sort(key=lambda p: p[0]*p[1])
        pans1 = pans[-K::]
        pans1.sort(key=lambda p: p[0])
        bestp1 = pans1[-1]
        answer1 = pi*(2*sum(p[0]*p[1] for p in pans1) + bestp1[0]*bestp1[0])

        #print pans1, answer1

        pans.sort(key=lambda p: p[0])
        bestp2 = pans.pop()
        pans.sort(key=lambda p: p[0] * p[1])
        pans.append(bestp2)
        pans2 = pans[-K::]
        answer2 = pi * (2 * sum(p[0] * p[1] for p in pans2) + bestp2[0] * bestp2[0])

        #print pans2, answer2
        output(t, max(answer1, answer2))


if __name__ == "__main__":
    main()