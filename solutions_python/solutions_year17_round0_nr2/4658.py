def int2list(N):
    list = []
    while(N != 0):
        list += [N%10]
        N = N/10
    return list

def is_tidy_number(N):
    res = True
    list = int2list(N)
    i = 0

    while(i < (len(list) - 1) and res):
        if(list[i] < list[i + 1]):
            res = False
        i += 1
        
    return res

## Returns the biggest tiny number Tatiana has counted
## while counting until N counting from N to 0 and returning
## the first number encountered which is tidy
def max_tidy_number_dumb(N):
    found = False

    i = N
    while(not found):
        if(is_tidy_number(i)):
            found = True
        else:
            i -= 1

    return i

def main():
    file = open(r'B-small-attempt0.in', 'r')
    lines = file.readlines()
    file.close()

    n = int(lines[0])

    output = []
    
    for i in range(1, n + 1):
        output += ["Case #" + str(i) + ": " + str(max_tidy_number_dumb(int(lines[i]))) + "\n"]

    file= open(r'ProblemB_output.txt', 'w')
    file.writelines(output)
    file.close()
    
main()

