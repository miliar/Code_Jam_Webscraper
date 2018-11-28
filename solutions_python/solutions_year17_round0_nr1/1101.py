import sys

def flip(ch):
        if ch == '-':
                return '+'
        else:
                return '-'

# returns 'IMPOSSIBLE', or number of moves
def flipStack(stack,K):
        # check for '-' in stack
        moves = 0
        while '-' in stack:
                # check if still solvable
                if K > len(stack[stack.index('-'):]):
                        return 'IMPOSSIBLE'
                # if solvable, flip from '-'
                else:
                        idx = stack.index('-')
                        for i in range(idx,idx + K):
                                stack[i] = flip(stack[i])
                        moves += 1
        return moves


def rep(case,moves):
        print "Case #" + str(case) + ": " + str(moves)


def main():
	# read data in
	filename = str(sys.argv[1])
	f = open(filename,'r')

	# burn first line
	f.readline()

	#iterate lines
	case = 1
	for line in f:
		line = line.split()
		stack = list(line[0])
		K = int(line[1])
		#print 'flipStack input (stack/K): ' + str(stack) + ' ' + str(K)
		moves = flipStack(stack,K)
		rep(case,moves)
		case += 1
			
main()	
#print flipStack(['-','-','-','+','-','+','+','-'],3)
	
