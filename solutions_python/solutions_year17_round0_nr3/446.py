import sys
sys.stdout = open('BathroomStalls.out', 'w')

n = int( input())

def splitme( n ):
    if n%2==0:
        return (n//2, n//2-1)
    else:
        return (n//2, n//2)

def solve(n,k):
    acc = []
    acc.append([n,1,1])
    map = {n:0}
    i = 0
    while i<len(acc):
        for candidate in splitme( acc[i][0] ):
            if candidate not in map:
                map[candidate] = len(acc)
                acc.append([candidate,0,0])
            acc[ map[candidate]][1] += acc[i][1]
        i += 1
    for i in range(0,len(acc)):
        acc[i][2] = acc[i][1]
        if i>0:
            acc[i][2] += acc[i-1][2]

        if acc[i][2]>=k:
            return splitme( acc[i][0] )

    return (0,0)

for test in range(1,n+1):
    (a,b) = input().split(" ")
    answer = solve( int(a), int(b) )
    print("Case #{}: {} {}".format(test, answer[0], answer[1] ))