import sys
sys.stdout = open('TidyNumbers.txt', 'w')

def solve(data):
    for i in range( len(data)-2,-1,-1):
        if data[i]>data[i+1]:
            data[i] -= 1
            for j in range(i+1, len(data)):
                data[j] = 9
    if data[0] == 0:
        return "".join( str(x) for x in data[1:])
    else :
        return "".join( str(x) for x in data )

n = int( input())
for test in range(1,n+1):

    answer = solve( list( map( int, list(input()))) )
    print("Case #{}: {}".format(test, answer ) )