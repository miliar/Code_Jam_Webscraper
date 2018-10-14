# Google Code Jam 2017
# Qualification Round
# Problem C. Bathroom Stalls
    
import bisect

def bathroom_stalls(n, k):
    # some corner cases:
    if k == n:
        return 0,0
        
    # data structure: row lenght -> number of rows with that length
    row_len = {}
    row_len[n] = 1
    row_len_keys = [n] # precomputed list of sorted keys
    
    for p in range(k):
        # ########################################### #
        # query the data structure: lenght -> (s0,s1) #
        # ########################################### #
        length = row_len_keys[-1] # longest bathroom row
        
        # ####################### #
        # perform the computation #
        # ####################### #

        len0 = (length - 1) / 2
        len1 = (length - 1) - len0
        
        left  = len0
        right = len1
        
        # ##################### #
        # update data structure #
        # ##################### #
        if row_len[length] == 1:
            del row_len[length]
            row_len_keys.pop( bisect.bisect_left(row_len_keys, length) )
        else:
            row_len[length] -= 1
        
        #if len0 not in row_len:
        if len0 not in row_len_keys:
            row_len[len0] = 1
            bisect.insort_left(row_len_keys, len0)
        else:
            row_len[len0] += 1
        
        #if len1 not in row_len:
        if len1 not in row_len_keys:
            row_len[len1] = 1
            bisect.insort_left(row_len_keys, len1)
        else:
            row_len[len1] += 1
    
    return right, left


def solver():
    # t: the number of cases
    t = int(raw_input())
    
    for i in xrange(1, t+1):
        n, k = raw_input().split(' ')

        n = int(n)
        k = int(k)        

        ans1, ans2 = bathroom_stalls(n, k)
        
        print "Case #{}: {} {}".format(i, ans1, ans2)


def main():
    solver()

if __name__ == '__main__':
    main()