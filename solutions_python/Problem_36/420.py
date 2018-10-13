
import os, sys, re, string

def main():
    N = int(sys.stdin.readline())
    for i in range(1, N+1):
        text = sys.stdin.readline().strip()
        welcome = "welcome to code jam"
        count = 0
        wlen = len(welcome)
        maxindex = len(text) - len(welcome)
        def countup(ti,index):
            if index == wlen:
                return 1
            if ti - index > maxindex:
                return 0
            if text[ti] == welcome[index]:
                return countup(ti + 1, index) + countup(ti + 1, index + 1)
            else:
                return countup(ti + 1, index)
        for j in range(maxindex+1):
            if text[j] == 'w':
                count = countup(j, 0)
                break
        print "Case #%d: %04d" % (i, count)

if __name__ == '__main__':
    main()
