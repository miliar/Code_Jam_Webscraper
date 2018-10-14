# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer

for i in xrange(1, t + 1):

    #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    #print "Case #{}: {} {}".format(i, n + m, n * m)
    # check out .format's specification for more formatting options
    #s, k = [sk for sk in raw_input().split(" ")]
    n = int(raw_input())
    y = None

    if str(n) == int(''.join(sorted(str(n)))):
        y = n
    else:
        while n != int(''.join(sorted(str(n)))):
            #print n, int(''.join(sorted(str(n))[::-1]))
            #n = int(n)
            n -= 1
        y = n


    print "Case #{}: {}".format(i, y)



'''
Input 
 	
Output 
 
4
132
1000
7
111111111111111110

Case #1: 129
Case #2: 999
Case #3: 7
Case #4: 99999999999999999

'''
