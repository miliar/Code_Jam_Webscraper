# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.




def tidyNumbers(n):
    # print n
    n = str(n)
    carryOver = False
    added = 0
    output = ""
    for i in range(len(n), 0, -1):
        curr = int(n[i-1])
        prev = int(n[i-2])

        # print(str(curr)+" is curr")
        # print(str(prev)+" is prev")
        # print(str(i)+" IS INDEX")



        if carryOver:
           curr = curr-1

        if i == 1:
            if curr == 0:
                return output
            else:
                output = str(curr) + output
                return output
        elif curr >= prev:
            output = str(curr) + output
            added += 1
            carryOver = False
        else:
            # print("Curr less than previous, "+ str(curr)+" < "+str(prev))
            added += 1
            output = str(9)*added
            carryOver = True
        # print (output)
    return output


# print(tidyNumbers(1000))
t = int(input())
for i in range(1 , t+1):
    n = input()
    output = tidyNumbers(n)
    print("Case #{}: {}".format(i, output))
