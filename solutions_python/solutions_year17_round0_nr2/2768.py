# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def is_tidy_number(N):
    N = str(N)
    for i in xrange(len(N)-1):
        if N[i] > N[i+1]:
            return False
    return True

T = int(raw_input())# read a line with a single integer
for i in xrange(1, T + 1):
    N = int(raw_input())
    change_starting_index = 0
    
    if is_tidy_number(N):
        print "Case #{}: {}".format(i, N)
        continue

    N = list(str(N))
        
    for j in xrange(len(N) - 1):
        if int(N[j]) > int(N[j + 1]):
            break
        if int(N[j]) < int(N[j + 1]):
            change_starting_index = j + 1

    if change_starting_index == None:
        print "Case #{}: {}".format(i, int(''.join(N)))
        continue
    else:
        N[change_starting_index] = str(int(N[change_starting_index]) - 1)
        for j in xrange(change_starting_index+1, len(N)):
            N[j] = '9'
        print "Case #{}: {}".format(i, int(''.join(N)))