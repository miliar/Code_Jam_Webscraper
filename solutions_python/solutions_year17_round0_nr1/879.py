import sys
'''
Always need to flip the leftmost one, no matter what.
Flips are independent of order
'''


if __name__  == '__main__':

    xx = sys.stdin.readline()
    num = 0
    for line in sys.stdin:
        num += 1
        (cake, k) = line.strip().split()
        k = int(k)
        arr = []
        for c in cake:
            if c == '+':
                arr.append(1)
            else:
                arr.append(0)
        flip = 0
        for i in range(len(arr)-k+1):
            if arr[i] == 1: continue # already done
            flip += 1
            arr[i] = 1
            for j in range(i+1,i+k): # flip
                arr[j] = 1 - arr[j]
            #print arr
        for a in arr:
            if a == 0:
                ret = 'IMPOSSIBLE'
                break
        else:
            ret = str(flip)

        print 'Case #'+str(num)+': '+ ret
