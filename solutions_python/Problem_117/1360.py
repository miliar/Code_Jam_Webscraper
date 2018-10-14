import sys
import numpy as np

# transpose lawn as transposed
# for row in lawn:
#   Get the max level for this row
#   for elem in row:
#     if elem < max:
#       if transposed[:row].max() > elem:
#         print "NO"
#         return
# print "YES"

def can_cut(lawn):
    transposed = np.transpose(lawn)
    i = 0
    j = 0
    for row in lawn:
        max_level = row.max()
        for elem in row:
            if elem < max_level:
                if transposed[j:j+1].max() > elem:
                    print "NO"
                    return
            j += 1
        j = 0
        i += 1
    print "YES"

if __name__ == "__main__":
    lawns = []
    with open(sys.argv[1], "r") as f:
        testcases = int(f.readline().strip())
        for case in xrange(testcases):
            lawn = []
            size = f.readline().strip().split(" ")
            N = int(size[0])
            M = int(size[1])
            for i in xrange(N):
                lawn.append(map(int, f.readline().strip().split(" ")))
            lawns.append(np.array(lawn, np.int))

    case = 0
    for lawn in lawns:
        case += 1
        print "Case #%d:" % (case,),
        can_cut(lawn)
