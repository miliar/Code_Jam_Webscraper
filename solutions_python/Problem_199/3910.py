import copy
def invert_values(arr, i , k):

    for l in range(i, i+k):
        if arr[l] == "+":
            arr[l] = "-"
        else:
            arr[l] = "+"
    return arr

def reverse(arr):
    arr.reverse()
    return arr

def allPos(arr):
    for i in range(len(arr)):
        if (arr[i] == "-"):
            return 0
    return 1

file = open("A.in", "r")
out = open("out.txt", "w")
impossible = ''
i = 0
p=0
for line in file:
    j=0
    arr=line.split(' ')
    tmp = arr[0]
    k = int(arr[1])
    row = list(tmp)
    p=p+1
    loop = 0
    while allPos(row) !=1 and j != 'IMPOSSIBLE':
        if row[i] == '-' :
            if i+k-1 < len(row):
                row = invert_values(row , i, k)
                i=0
                #row = reverse(row)
                j=j+1
            else:
                #impossible='IMPOSSIBLE'
                #j = ''
                row = reverse(row)
                i=0
        else:
            i=i+1
        loop = loop + 1
        if(loop > 100):
            j='IMPOSSIBLE'
            i=0
            break
    out.write("Case #" + str(p) + ": " + str(j) + "\n")
