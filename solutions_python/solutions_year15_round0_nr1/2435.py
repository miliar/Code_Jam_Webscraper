import sys

def standing_ovation(smax, arr):
    if smax==0:
        return 0
    n = len(arr)
    standing = arr[0]
    toadd = 0
    for i in range(1, n):
        #print("%d: st:%d"%(i, standing))
        missing = 0
        if standing<i:
            missing += (i-standing)
            standing += missing
            toadd += missing
        standing += arr[i]
    return toadd
    
if __name__=='__main__':
    fname = sys.argv[1]
    cases = []
    with open(fname, 'r') as f:
        ntest = int(f.readline())
        for i in range(ntest):
            tmp = f.readline().split()
            smax = int(tmp[0])
            data = list(map(lambda x: int(x), list(tmp[1])))
            cases.append([smax, data])
    for i in range(ntest):
        print("Case #%d: %d"% ((i+1), standing_ovation(cases[i][0], cases[i][1])))