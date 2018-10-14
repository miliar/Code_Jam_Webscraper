import numpy as np
import sys

with open(sys.argv[2], "w") as outfile:
    with open(sys.argv[1], "r") as infile:
        mawcount=int(infile.readline())
        for i in range(mawcount):
            dim = tuple([int(c) for c in infile.readline().split()])
            tmp = []
            for _ in range(dim[0]):
                tmp.append([int(c) for c in infile.readline().split()])
            maw = np.array(tmp)
            res = None
            for level in range(np.max(maw), 0, -1):
                goal = maw<=level
                mask = np.zeros(dim)
                for j in range(dim[0]):
                    m = np.product(goal[j])
                    if m:
                        mask[j]=goal[j]
                goal = goal.T
                mask = mask.T
                for j in range(dim[1]):
                    m = np.product(goal[j])
                    if m:
                        mask[j]=goal[j]
                res=np.product(goal==mask.astype(bool))
                if (res==0):
                    break
            if  (res==0):
                outfile.write("Case #%d: NO\n" % (i+1,))
            else:
                outfile.write("Case #%d: YES\n" % (i+1,))