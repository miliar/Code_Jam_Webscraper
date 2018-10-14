import sys

T = int(sys.stdin.readline())

for case in range(1, T + 1) :
    output = "Case #" + str(case) + ": "
    line = sys.stdin.readline().strip().split()
    A = line[0]
    B = line[1]
    digit = len(A)
    result = 0

    pairs = {}

    for n in range(int(A), int(B) + 1):
        for sublength in range(1, digit):
           # for insertPos in range(0, digit - sublength) :
                insertPos = 0
                oriNum = str(n)
                newNum = oriNum[0:insertPos] + oriNum[-sublength:] + oriNum[insertPos:-sublength]
                m = int(newNum)
                if n < m and int(A) <= m <= int(B):
                    if (n, m) not in pairs:
                        pairs[(n, m)] = 1
                        result += 1
    output += str(result)
    print output

