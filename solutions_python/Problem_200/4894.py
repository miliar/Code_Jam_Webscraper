outval_global = 0

def is_untidy(input_str):
    if len(input_str) == 1:
        return False
    else:
        for j in xrange(0, len(input_str)-1):
            if input_str[j] > input_str[j+1]:
                #print "untidy %r" % inputStr[0][j]
                return True

def dec_input_str(input_str):
    if is_untidy(input_str):
        #print "untidy!!"
        #print "decreasing by 1: %r" % str(int(input_str) - 1)
        dec_input_str(str(int(input_str) - 1))
    else:
        #print "tidy value %r" % int(input_str)
        global outval_global
        outval_global = int(input_str)

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    inputList = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    # for each n, check if tidy, if not, subtract 1 and check if tidy, keep checking until we get a tidy number
    output = dec_input_str(inputList[0])

    #print "Output value: %r" % output
    print "Case #{}: {}".format(i, outval_global)
