import sys
sys.setrecursionlimit(10000000)
def flip_pancake(pancake_row,k):
    data = ""
    for i in range(k):
        if pancake_row[i] == '+':
            data += '-'
        else:
            data += '+'
    data += pancake_row[k:]
    return data


def getFlips(pancake_row, k, n):
    pancake_row = pancake_row.lstrip('+')
    if len(pancake_row) == 0:
        return n
    if len(pancake_row) < k:
        return "IMPOSSIBLE"
    pancake_row = flip_pancake(pancake_row,k)
    pancake_row = pancake_row.lstrip('+')
    return getFlips(pancake_row, k, n+1)


def main():
    n = input()
    for i in range(n):
        pancake_row = raw_input().split()
        k = int(pancake_row[1])
        pancake_row = str(pancake_row[0])
        print "Case","#"+str(i+1)+":",getFlips(pancake_row,k,0)
main()
