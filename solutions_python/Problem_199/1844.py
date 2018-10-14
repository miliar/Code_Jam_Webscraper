from collections import deque
import time


def main():
    with open("C:\\Users\\user\\Dropbox\\Documents\\GoogleCodeJam2017\\A.Pancakes\\result" + str(time.time()) +
                ".txt", 'w') as resF:
        T, K, rows = readFile("C:\\Users\\user\\Dropbox\\Documents\\GoogleCodeJam2017\\A.Pancakes\\example.txt")
        for i in xrange(T):
            currNum = plusesToBinary(rows[i])
            currOps = calcOps(rows[i], K[i])
            res = bfs(currNum, currOps)
            resF.write("Case #" + str(i+1) + ": " + str(res) + "\n")




def readFile(filename):
    with open(filename) as f:
        lines = f.readlines()
        if len(lines) == 0:
            print "Err reading"
        T = int(lines[0].replace("\n",""))

        K = []
        rows = []
        for i in xrange(1, T+1):
            temp = lines[i].split(" ")
            K.append(int(temp[1].replace("\n", "")))
            rows.append(temp[0])
        return (T, K, rows)

def plusesToBinary(row):
    return int(row.replace("-", "1").replace("+", "0"), 2)

def calcOps(row, k):
    return [int('1'*k, 2) << i for i in xrange(len(row) - k + 1)]

def bfs(number, ops):
    maxResult = len(ops) + 1
    fringe = deque()
    visited = set()
    fringe.append((number, 0))
    while len(fringe) > 0:
        currentState = fringe.popleft()
        #print currentState
        if currentState[0] == 0:
            return currentState[1]
        if currentState[0] not in visited and currentState[1] < maxResult:
            visited = visited | set([currentState[0]])
            for op in ops:
                fringe.append((currentState[0]^op, currentState[1] + 1))

    return 'IMPOSSIBLE'


def bfs2(number, ops):
    maxResult = len(ops) + 1
    fringe = deque()
    visited = set()
    fringe.append((number, 0, set(ops)))
    while len(fringe) > 0:
        currentState = fringe.popleft()
        #print currentState
        if currentState[0] == 0:
            return currentState[1]
        if currentState[0] not in visited and currentState[1] < maxResult and len(currentState[2]) > 0:
            visited = visited | set([currentState[0]])
            for op in currentState[2]:
                fringe.append((currentState[0]^op, currentState[1] + 1, currentState[2] - {op}))
    return 'IMPOSSIBLE'


if __name__ == '__main__':
    main()

