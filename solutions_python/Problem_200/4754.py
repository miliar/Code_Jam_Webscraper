# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

# This problem feeds # of cases as line 1. Then, for each case, return the largest "tidy" number starting from the case.

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = int(input())  # read an integer
# Check if we already know it won't work
    done = 0
    while done < 1:
        if n % 10 != 0:
            string = str(n)
            result = list(string)
            result.sort()
            if result[0] != 0:
                result = "".join(result)
                if result == string:
                    print("Case #{}: {}".format(i, result ))
                    done = 1
        n -= 1
# check out .format's specification for more formatting options
