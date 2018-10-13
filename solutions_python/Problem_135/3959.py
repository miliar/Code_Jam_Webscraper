import sys

def main():
    for T in xrange(1, int(sys.stdin.readline())+1):
        grid = []
        A = []
        for x in xrange(2):
        	A.append(int(sys.stdin.readline()))
        	for row in xrange(4):
        		grid.append(set([int(w) for w in sys.stdin.readline().split()]))

        print 'Case #%d: ' % (T),
        card = grid[A[0]-1] & grid[A[1]+3]
        if len(card) == 1:
        	print card.pop()
        elif len(card) > 1:
        	print 'Bad magician!'
        else:
                print 'Volunteer cheated!'
        

if __name__ == '__main__':
    main()
