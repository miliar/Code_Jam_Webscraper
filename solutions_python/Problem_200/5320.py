# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

t = int(input())                            # t = number of test cases ie lines to follow

for i in range(1, t + 1):                   # for each test case
    n = int(input())                        # last number counted in that test case
    #print("n: " + str(n))
    last_tidy = 0

    for j in range(n, 0, -1):               # for each decreasing range of that case's number
        #if int(last_tidy) > 0:
        #    break
        test = str(j)                       # the string version of that decreasing number
        #print("test: " + test)
        counter = 0

        for k in range(0, len(test) - 1):   # for each digit
            #print("counter: " + str(counter))
            if int(test[k]) <= int(test[k + 1]):
                counter += 1

            if counter == len(test) - 1:
                break

            #if k == len(test) - 1:
                #

        if counter == len(test) - 1:
            last_tidy = test
            #print("last_tidy: " + last_tidy)
            break

    print("Case #{}: {}".format(i, last_tidy))