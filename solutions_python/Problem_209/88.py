import sys, math

stdout = sys.stdout
stdin = sys.stdin
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

maxTop = 0

def top(pancake):
    return pancake[0]**2 * math.pi
def side(pancake):
    return pancake[0]*2*math.pi*pancake[1]
def area(pancake):
    global maxTop
    return side(pancake) + max(top(pancake)-maxTop, 0)

def solve():
    global maxTop
    maxTop = 0
    
    result = 0
    N, K = map(int, input().split())
    pancakes = []
    for i in range(N):
        Ri, Hi = map(int, input().split())
        pancakes.append([Ri, Hi])
    for k in range(K):
        maxIndex = 0
        for p in range(1,len(pancakes)):
            if area(pancakes[p]) > area(pancakes[maxIndex]):
                maxIndex = p
        result += area(pancakes[maxIndex])
        maxTop = max(maxTop, top(pancakes[maxIndex]))
        pancakes.pop(maxIndex)
    return result

T = int(input())
for CASE in range(1,T+1):
    print('Case #' + str(CASE) + ': ', end='')
    print(solve())

sys.stdout = stdout
sys.stdin = stdin
