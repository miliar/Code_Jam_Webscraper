import sys
import numpy as np

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    if len(argv) >= 1:
        inFileName= argv[0]
    else:
        inFileName = "test.in"
    if len(argv) >= 2:
        outFileName = argv[1]
    else:
        outFileName = "out.out"

    with open(inFileName) as inFile:
        with open(outFileName, 'w') as outFile:
            for caseNo, line in enumerate(inFile):
                if caseNo == 0:
                    numCases = int(line)
                    continue
                toks = line.split()
                N = int(toks[0])
                seq = []
                seq2 = [[],[]]
                for i in xrange(N):
                    name = toks[i*2+1]
                    botNo = 0 if name == 'O' else 1
                    pos = int(toks[i*2+2])
                    seq.append((botNo, pos))
                    seq2[botNo].append(pos)

                t = 0
                pos = [1, 1]
                dp = [1, 1]
                for i in xrange(2):
                    if seq2[i]:
                        dp[i] = seq2[i].pop(0)
                move = None
                for bot, dp2 in seq:
                    if dp[bot] != dp2:
                        print "Error!"
                    dt = abs(dp[bot] - pos[bot]) + 1
                    t += dt
                    pos[bot] = dp[bot]
                    delta = dp[1-bot] - pos[1-bot]
                    if abs(delta) <= dt:
                        pos[1-bot] = dp[1-bot]
                    elif delta < 0:
                        pos[1-bot] -= dt
                    elif delta > 0:
                        pos[1-bot] += dt

                    if seq2[bot]:
                        dp[bot] = seq2[bot].pop(0)
                outFile.write('Case #{0}: {1}\n'.format(caseNo, t))
                
            if numCases != caseNo:
                print "Missing Case!"


if __name__ == "__main__":
    main()
