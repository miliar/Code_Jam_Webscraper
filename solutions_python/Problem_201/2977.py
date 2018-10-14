'''
Problem

A certain bathroom has N + 2 stalls in a single row; the stalls on the left and right ends are permanently occupied by the bathroom guards. The other N stalls are for users.

Whenever someone enters the bathroom, they try to choose a stall that is as far from other people as possible. To avoid confusion, they follow deterministic rules: For each empty stall S, they compute two values LS and RS, each of which is the number of empty stalls between S and the closest occupied stall to the left or right, respectively. Then they consider the set of stalls with the farthest closest neighbor, that is, those S for which min(LS, RS) is maximal. If there is only one such stall, they choose it; otherwise, they choose the one among those where max(LS, RS) is maximal. If there are still multiple tied stalls, they choose the leftmost stall among those.

K people are about to enter the bathroom; each one will choose their stall before the next arrives. Nobody will ever leave.

When the last person chooses their stall S, what will be the values of max(LS, RS) and min(LS, RS) be?

Solving this problem

This problem has 2 Small datasets and 1 Large dataset. You must solve the first Small dataset before you can attempt the second Small dataset. You will be able to retry either of the Small datasets (with a time penalty). You will be able to make a single attempt at the Large, as usual, only after solving both Small datasets.

Input

The first line of the input gives the number of test cases, T. T lines follow. Each line describes a test case with two integers N and K, as described above.

Output

For each test case, output one line containing Case #x: y z, where x is the test case number (starting from 1), y is max(LS, RS), and z is min(LS, RS) as calculated by the last person to enter the bathroom for their chosen stall S.

Limits

1 <= T <= 100.
1 <= K <= N.
Small dataset 1

1 <= N <= 1000.
Small dataset 2

1 <= N <= 106.
Large dataset

1 <= N <= 1018.
Sample


Input 
 	
Output 
 
5
4 2
5 2
6 2
1000 1000
1000 1

Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499

'''








def this_is_bathroom(N,K) :
    l = []
    l.append( [0,0])
    l.append( [N+1, N+1] )
    
    for k in xrange(K) :
        
        max_space = 0
        max_index = 0
        
        for i in xrange( len(l) - 1 ) :
            y1 = l[i][1]
            y2 = l[i+1][1]
            local_space = y2 - y1 - 1
            if local_space > max_space :
                max_space = local_space
                max_index = i
        
        offset = int(round(1.0 * max_space/2))  #always bugs me 5/2 = 2 because int/int. need to make one as float
        
        LS = RS = 0
        if offset - l[max_index][1] == 1 :
            LS = 0
            l[max_index][1] = l[max_index][1]+1
            RS = l[max_index+1][0] - l[max_index][1] - 1
            #print "yo1 {}:{}".format(LS,RS)
        elif l[max_index+1][1] - offset == 1 :
            RS = 0
            l[max_index+1][0] = l[max_index+1][0] - 1
            LS = l[max_index][0] - l[max_index-1][1] - 1
            #print "yo2 {}:{}".format(LS,RS)
        else :
            new_occupied = l[max_index][1]+offset
            LS = new_occupied - l[max_index][1] - 1
            RS = l[max_index+1][0] - new_occupied - 1
            #print "yo3 {}:{}".format(LS,RS)
            l.insert( max_index+1, [new_occupied, new_occupied] )
    
    # print "{}:{}".format(LS,RS)
    return max(LS,RS), min(LS,RS)    
    
            
            
if __name__ == '__main__' :
    #print this_is_bathroom(1000,1)
    t = int(raw_input())
    for i in xrange(1, t+1) :
        N, K = [int(s) for s in raw_input().split(" ")]
        mx, mn = this_is_bathroom(N, K)
        print "Case #{}: {} {}".format(i, mx, mn)
    
    
    
    
    
