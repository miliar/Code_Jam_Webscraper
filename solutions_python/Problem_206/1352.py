from collections import defaultdict

import sys
sys.setrecursionlimit(1000000)

def mask(s, k):
    res = []
    for i in range(len(s) - k + 1):
        copys = list(s)
        for j in range(i, i + k):
            if copys[j] == "+":
                copys[j] = "-"
            else:
                copys[j] = "+"
        res.append(''.join(copys))
    return res

class Solution1(object):
    def solution(self, line):
        s, k = line.split(" ")
        k = int(k)
        self.k = k
        self.target = "+" * len(s)
        self.smap = {}
        self.smap[s] = 0
        list = [s]

        while len(list) >0 :
            s = list.pop(0)
            depth = self.smap[s] + 1
            for item in mask(s, self.k):
                if item not in self.smap or self.smap[item] > depth:
                    self.smap[item] = depth
                    list.append(item)
            if self.target in self.smap:
                break

        if self.target in self.smap:
            return str(self.smap[self.target])
        else:
            return "IMPOSSIBLE"

class Solution2(object):
    def solution(self, line):
        k = len(line)
        listline = [int(s) for s in list(line)]
        def istidy(listline) :
            for i in range(1, len(listline)):
                if listline[i] < listline[i-1]:
                    return False
            return True
        if istidy(listline):
            return int(line)
        maxn = []
        for i in range(1, k):
            maxn.append(int(line[:i]) * (10 ** (k- i)) -1)
        return max([num for num in maxn if istidy(list(str(num)))])

def getn(line, i):
    return int(line[:i]) * (10 ** (len(line) - i)) -1


def findk(listn):
    n = listn[0]
    length = len(listn)
    start = 0
    end = length - 1
    mid = 0
    while start <= end:
        mid = int((start + end) / 2)
        if n != listn[mid]:
            end = mid - 1
        elif mid + 1 < length and listn[mid+1] == n:
            start = mid + 1
        else:
            break
    return mid


class Solution3(object):
    def solution(self, line):
        s, k = [int(i) for i in line.split(" ")]
        listn = [(s, 1)]
        while listn[0][0] > 1:
            n = listn[0][0]
            i = listn[0][1]
            if k < (i + 1):
                break
            k -= i

            listn = listn[1:]

            m = int((n-1)/2)
            if n % 2 == 0:
                listn.append((m+1, i))
                listn.append((m, i))
            else:
                listn.append((m, i * 2))
            #print(n, k, listn)

        head = listn[0][0]
        if head == 1:
            return (0, 0)
        m = int((head - 1) / 2)
        if head % 2 == 0:
            return (m + 1, m)
        else:
            return (m, m)

def printm(matrix):
    pass
    #print()
    #for a in matrix[1:]:
    #    print(a[1:])
import copy
class Solution4(object):
    def solution(self, n, bou):
        score = 0
        scoremap = {" ": 0,"+" : 1, "x":1, "o" :2}
        validmap = {"+" : {"+", "o"}, "x" : {"x", "o"}, "o" : {"o"}}
        matrix = [[{" ", "+", "x", "o"} for i in range(n+1)] for j in range(n + 1)]
        self.matrixres = [[" " for i in range(n+1)] for j in range(n + 1)]
        change = []
        matrixresold = [[" " for i in range(n+1)] for j in range(n + 1)]
        for i in range(n+1):
            matrix[i][0].add('?')
        #print(self.matrixres)
        for boua in bou:
            s, si, sj = boua[0], int(boua[1]), int(boua[2])
            matrixresold[si][sj] = s
            matrix[si][sj] = validmap[s]
        #print(matrix)
        def tranverse(matrix, i, j):
            # global change
            # global matrixresold
            # print(i, j)
            if i == n + 1:
                #print("result")
                printm(self.matrixres)
                return (True, 0)

            validij = matrix[i][j]
            valid, score = True, 0
            if len(validij) == 0:
                return (False, 0)

            if "o" in validij:
                matrixcopy = [[set(s) for s in matrix[i][:]] for i in range(n + 1)]
                #print(i, j, "o")
                #print("matrix23--->", matrixcopy[2][2])
                k = 1
                while i + k < n + 1 or j + k < n + 1:
                    if i + k < n + 1:
                        matrixcopy[i + k][j] &= {"+", " "}
                        if len(matrixcopy[i + k][j]) == 0:
                            valid = False
                            break
                        if j - k >= 1:
                            matrixcopy[i + k][j - k] &= {"x", " "}
                            if len(matrixcopy[i + k][j - k]) == 0:
                                valid = False
                                break
                        if j + k < n + 1:
                            matrixcopy[i + k][j + k] &= {"x", " "}
                            if len(matrixcopy[i + k][j + k]) == 0:
                                valid = False
                                break
                    if j + k < n + 1:
                        matrixcopy[i][j + k] &= {"+", " "}
                        if len(matrixcopy[i ][j + k]) == 0:
                            valid = False
                            break
                    k += 1
                #print("matrix23--->", matrixcopy[2][2])
                if valid:
                    valid, score = tranverse(matrixcopy, i + int(j / n), 1 if j == n else j + 1)
                    if valid:
                        self.matrixres[i][j] = "o"
                        if matrixresold[i][j] != "o":
                            change.append(["o", i, j])
                        #print("valid matrixres")
                        printm(self.matrixres)
                        return (valid, score + 2)

                #print(i, j, "o", valid)




            if "+" in validij:
                valid = True
                matrixcopy = [[set(s) for s in matrix[i][:]] for i in range(n + 1)]
                k = 1
                #print(i, j, "+")
                #print("matrix23--->", matrixcopy[2][2])
                while i + k < n + 1 or j + k < n + 1:
                    if i + k < n + 1:
                        if j - k >= 1:
                            matrixcopy[i + k][j - k] &= {"x", " "}
                            if len(matrixcopy[i+k][j - k]) == 0:
                                valid = False
                                break
                        if j + k < n + 1:
                            matrixcopy[i + k][j + k] &= {"x", " "}
                            if len(matrixcopy[i+k][j + k]) == 0:
                                valid = False
                                break
                    k += 1
                #print("matrix23--->", matrixcopy[2][2])
                if valid:
                    valid, score = tranverse(matrixcopy, i + int(j / n), 1 if j == n else j + 1)
                    if valid:
                        self.matrixres[i][j] = "+"
                        if matrixresold[i][j] != "+":
                            change.append(["+", i, j])
                        #print("valid matrixres")
                        printm(self.matrixres)
                        return (valid, score + 1)
                #print(i, j, "+", valid)


            if "x" in validij:
                valid = True
                matrixcopy = [[set(s) for s in matrix[i][:]] for i in range(n + 1)]
                #print(i, j, "x")
                #print("matrix23--->", matrixcopy[2][2])
                k = 1
                while i + k < n + 1 or j + k < n + 1:
                    if i + k < n + 1:
                        #if i == 1 and j == 2:
                            #print(i + k, j, "matrix23--->", matrixcopy[2][3] == matrixcopy[2][2])
                        matrixcopy[i + k][j] &= {"+", " "}
                        #if i == 1 and j == 2:
                            #print(k, "matrix23--->", matrixcopy[2][3])
                        if len(matrixcopy[i + k][j]) == 0:
                            valid = False
                            break
                    if j + k < n + 1:
                        matrixcopy[i][j + k] &= {"+", " "}
#                        if i == 1 and j == 2:
                            #print(k, "matrix23--->", matrixcopy[2][3])
                        if len(matrixcopy[i][j + k]) == 0:
                            valid = False
                            break
                    k += 1
                #print("matrix23--->", matrixcopy[2][2])

                if valid:
                    valid, score = tranverse(matrixcopy, i + int(j / n), 1 if j == n else j + 1)
                    if valid:
                        self.matrixres[i][j] = "x"
                        #print("valid matrixres")
                        if matrixresold[i][j] != "x":
                            change.append(["x", i, j])
                        printm(self.matrixres)
                        return (valid, score + 1)
                #print(i, j, "x", valid)

            if " " in validij:
                matrixcopy = [[set(s) for s in matrix[i][:]] for i in range(n + 1)]
                #print(i, j, "empty")
                valid, score = tranverse(matrixcopy, i + int(j / n), 1 if j == n else j + 1)
                if valid:
                    self.matrixres[i][j] = " "
                    printm(self.matrixres)
                    return (valid, score)

            return (False, 0)

        res = tranverse(matrix, 1, 1)
        #print(change)
        printm(self.matrixres)
        return (res[1], change)

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
#res = Solution4().solution(2, [])
#print(res)
# res = Solution4().solution(3, [["+", "2", "3"], ["+", "2", "1"],["x", "3", "1"],["+", "2", "2"]])
# print(res)

import math

def findLongestRepeatSeq(alist):
    maxr = int(len(alist) / 2)
    answers = [0] + [1] * maxr
    totry = maxr + 1
    def valid(alist, totry):
        #print(totry)
        group = math.ceil(len(alist) / totry)
        for j in range(totry):
            start = alist[j]
            for i in range(1, group):
                if j + i * totry < len(alist) and alist[j + i * totry] != start:
                    return False
        return True

    while totry > 1:
        totry -= 1
        #print(maxr, totry)
        if answers[totry] == 0:
            continue
        if valid(alist, totry):
            return totry
        else:
            for k in range(1, totry + 1):
                if totry%k == 0:
                    answers[k] = 0
    return 1



def arriveTime(k, s ,d):
    return (d - k) /s

def findSpeed(d, listh):
    timea = [arriveTime(item[0], item[1], d) for item in listh]
    maxtime = max(timea)
    return d/maxtime



t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    #res = Solution3().solution(input())
    line = input()
    d, nhost = line.split(" ")[0], line.split(" ")[1]
    horses = []
    for j in range(int(nhost)):
        line = input()
        horses.append((int(line.split(" ")[0]), int(line.split(" ")[1])))
    print("Case #{}: {} ".format(i, findSpeed(int(d), horses)))
    # check out .format's specification for more formatting options