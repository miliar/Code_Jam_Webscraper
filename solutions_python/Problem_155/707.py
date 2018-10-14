import sys

def solve():
    tests = int(input())
    for test in range(tests):
        line = input().split()
        arr = list(map(int, list(line[1])))
        for friends in range(0, 1111):
            cur = list(arr)
            cur[0] += friends
            works = True
            for i in range(1, len(cur)):
                if cur[i-1]<i:
                    works = False
                    break
                cur[i] += cur[i-1]
            if works:
                print("Case #" + str(test+1)+": "+str(friends))
                break

def run():
    if sys.hexversion == 50594544:
        sys.stdin = open("test.txt")
        sys.stdout = open("a.txt", 'w')
    solve()

run()