# coding: utf-8
import sys
import os.path
#import itertools
#from itertools import groupby
import math

def read(f):
    return tuple( int(v) for v in f.readline().split() )

def answer(f, X, ans):
    out = "Case #{}: {}".format(X, ans)
    f.write(out)
    f.write("\n")
    print(out)

def answer2(f, ans):
    f.write(ans)
    f.write("\n")
    print(ans)


def main(inf, outf):

    patterns = {}
    for m1 in range(1, 6):
        for m2 in range(1, 6):
            for m3 in range(1, 6):
                m = m1 * m2 * m3
                mlst = patterns.get(m, set())
                mlst.add( tuple(sorted( v for v in [m1, m2, m3] if v > 1 )) )
                patterns[m] = mlst
    print(patterns)

    T, = read(inf)
    for X in range(1, T + 1):

        R, N, M, K = read(inf)

        answer(outf, X, "")

        for r in range(R):

            ans = None
            nums = [0] * 6
            for p in read(inf):
                for pp in patterns[p]:
                    if len(pp) == 3:
                        answer2(outf, "".join(map(str, pp)))
                        break
                    else:
                        for i in pp:
                            nums[i] += 1
                else:
                    continue
                break
            else:
                nums = sorted(map(tuple, enumerate(nums)), key=lambda n: n[1], reverse=True)
                ans = ""
                for num in nums[0:3]:
                    if num[0] < 2:
                        ans += "2"
                    else:
                        ans += str(num[0])
                answer2(outf, ans)

def menseki(r):
    return r * r * math.pi



if __name__=="__main__":
    infname = sys.argv[1]
    outfname = os.path.splitext(infname)[0] + ".out"
    with open(infname, "r") as inf:
        with open(outfname, "w") as outf:
            main(inf, outf)
