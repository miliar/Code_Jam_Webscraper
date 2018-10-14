def fill(x,dic,A,r,c):
    i,j = dic[x]
    k = j+1
    while k < c and A[i][k] == '?' :
        A[i][k] = x
        k += 1
    k = j-1
    while k >=0 and A[i][k] == '?' :
        A[i][k] = x
        k -= 1
def copyList(l1,l2,size):
    i = 0
    while i < size:
        l2[i] = l1[i]
        i += 1
def fillQuestionMarks(A,r,c):
    i = 0
    tempList1 = []
    while i < r:
        if A[i][0] == '?' :

            tempList1 = []
            tempList2 = []
            j = i
            while j >=0 and A[j][0] == '?' :
                tempList1.append(j)
                j -= 1
            k = i
            while k < r and A[k][0] == '?':
                tempList2.append(k)
                k += 1
            if j >= 0:
                for x in tempList1:
                    copyList(A[j],A[x],c)
            else:
                for x in tempList2:
                    copyList(A[k],A[x],c)

        i += 1

def fun(A,r,c):

    dic = {}
    i = 0
    while i < r:
        j = 0
        while j < c:
            if A[i][j] != '?':
                dic[A[i][j]] = [i,j]
            j += 1
        i += 1
    for x in dic:
        fill(x,dic,A,r,c)
    fillQuestionMarks(A,r,c)


def printTwoDArray(A,r,c):
    i = 0
    while i < r:
        print "".join(A[i])
        i += 1
t = int(raw_input())
i1 = 1

while i1 <= t:
    r,c = map(int,raw_input().split())
    A = [0]*r
    j1 = 0
    while j1 < r:
        A[j1] = list(raw_input())
        j1 += 1
    fun(A,r,c)
    print "Case #"+str(i1)+":"
    printTwoDArray(A,r,c)
    i1 += 1
