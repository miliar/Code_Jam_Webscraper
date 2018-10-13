import sys
input = file(sys.argv[1])
    
T = int(input.readline())

def solve():
    A1 = int(input.readline())
    board1 = [map(int,input.readline().split()) for i in range(4)]
    A2 = int(input.readline())
    board2 = [map(int,input.readline().split()) for i in range(4)]
    
    x = set(board1[A1-1]) & set(board2[A2-1])
    if len(x) == 1:
        y, = x
        return y
    if len(x) == 0:
        return "Volunteer cheated!"
    return "Bad magician!"

for t in range(T):
    print 'Case #%s: %s' % (t+1,solve())
