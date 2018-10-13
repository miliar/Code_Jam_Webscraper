from __future__ import division
import sys
import copy

def isPerm(x1,x2):
    for x in x1:
        if not x in x2:
            return False
    return True


def flip(list1,index):
    #list1 = copy.deepcopy(list2)
    for i in xrange(0,len(list1)):
        if list1[i][index] == 0:
            list1[i][index] = 1
        elif list1[i][index] == 1:
            list1[i][index] = 0
    return list1

def subsets(my_set):
    result = [[]]
    for x in my_set:
        result = result + [y + [x] for y in result]
    return sorted(result,key=lambda x: len(x))

    
def compress(s):
    result = []
    last = s[0]
    count = 1
    n = len(s)
    for i in xrange(1, n):
        if s[i] == last:
            count += 1
        else:
            result.append((last, count))
            count = 1
            last = s[i]
    result.append((last, count))
    return result

    
def match2(str1, str2):
    arr1 = compress(str1)
    arr2 = compress(str2)
    len1 = len(arr1)
    len2 = len(arr2)
    if len1 != len2:
        return -1
    
    moves = 0
    for i in xrange(0, len1):
        if arr1[i][0] != arr2[i][0]:
            return -1
        moves += abs(arr1[i][1] - arr2[i][1])

    return moves


def matchN(strs2):
    strs = [compress(s) for s in strs2]
    N = len(strs)
    len0 = len(strs[0])
    for i in xrange(0, N):
        if len0 != len(strs[i]):
            return -1
    
    moves = 0
    for j in xrange(0, len0):
        avg = 0
        curr = strs[0][j][0]
        for i in xrange(0, N):
            if strs[i][j][0] != curr:
                return -1
            avg += strs[i][j][1]
        avg = round(avg / N)
        for i in xrange(0, N):
            moves += abs(strs[i][j][1] - avg)
    
    return moves

def generate(A, B, K):
    win = 0
    for a in xrange(0, A):
        for b in xrange(0, B):
            if (a & b) < K:
                # print a, b, K
                win += 1
    return win

def main():
    file = open(sys.argv[1], 'r')
    T = int(file.readline().strip())
    
    for trial in xrange(1,T+1):
        sys.stdout.write("Case #%d: " % trial)
        
        data = file.readline().strip().split()
        A = int(data[0])
        B = int(data[1])
        K = int(data[2])
        
        sys.stdout.write("%d\n" % generate(A,B,K))

if __name__ == '__main__':
    main()
