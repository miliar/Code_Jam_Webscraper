
import sys

def main():
    # Read standard input
    lines = sys.stdin.readlines()
    # For each sample input S : count ==  (lines[0])
    for s in range(int( lines[0] )):
        N = list( lines[s+1].strip() )
        tidy_num = N
        # If single digit ---> no modifications to num
        if len(tidy_num) != 1:
            def isTidy(num_list):
                for i in range(len(num_list) - 1):
                    if num_list[i] > num_list[i+1]:
                        return False
                return True
            while not isTidy(tidy_num):
                # For each i^th digit 0 ~ len(tidy_num) - 1
                for i in range(len(tidy_num) - 1):
                    # Obtain (i)^th num
                    curr_i = int(tidy_num[i])
                    # Obtain (i+1)^th num
                    next_i = int( tidy_num[i+1] )
                    # If ( i )^th > (i+1)^th
                    if curr_i > next_i:
                        # i^th : subtract 1
                        tidy_num[i] = str( curr_i - 1 )
                        # (i+1)^th ~~ end : set to 9
                        for offset in range(len(tidy_num) - (i+1)):
                            tidy_num[i+1+offset] = '9'
        # Convert modified list back to number
        # result = long( ''.join(tidy_num) )
        result = int( ''.join(tidy_num) )
        # result = 0
        # Print result
        print "Case #" + str(s+1) + ": " + str(result)

main()
