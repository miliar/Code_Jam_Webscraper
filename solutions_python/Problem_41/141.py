import sys, itertools
from bisect import bisect

output_line = "Case #{X:d}: {K}"


def next_num(num):
    num = list(num)
    smallest = "a"
    smalli = len(num) - 1
    stopi = smalli
    last = "0"
    for cur, i in zip(reversed(num), itertools.count(len(num)-1,-1)):
        if cur < last:
            stopi = i
            break
        last = cur
    if stopi == len(num) - 1: # this means we need to add a zero, because it is in reverse sorted order
        num += "0"
        num.sort()
        for cur, i in zip(num, itertools.count()):
            if cur!="0":
                num[0], num[i] = num[i], num[0]
                break
    else:
        for cur, i in zip(reversed(num), itertools.count(len(num)-1,-1)):
            if cur < smallest and cur > num[stopi]:
                smallest = cur
                smalli = i
            if stopi == i:
                break
        num[smalli], num[stopi] = num[stopi], num[smalli]
        end = num[stopi+1:]
        end.sort()
        num[stopi+1:] = end
    return "".join(num)

if __name__ == "__main__":
    infile, outfile = sys.argv[1:]
    with open(infile, "r") as inhandle, open(outfile, "w") as outhandle:
        T = int(inhandle.readline())
        for t in range(T):
            num = inhandle.readline().strip()
            K = next_num(num)
            print(output_line.format(X=t+1, K=K), file=outhandle)
