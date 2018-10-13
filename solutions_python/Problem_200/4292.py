#Problem B. Tidy Numbers


def solve(N):
    i = 0
    while i < len(N)-1:
        if N[i] > N[i+1]:
            count = i
            index = i
            while count:
                if N[count] == N [count-1]:
                    index = count - 1
                else:
                    break
                count -= 1
            subtract = int(N[index+1:])+1
            return int(N) - subtract
        i += 1

    return N


#Fetch the number of test cases
T = int(raw_input())
for testcase in range(1,T+1):
    #Fetch N from input file
    N = raw_input().strip()
    solution = str(solve(N))
    print "Case #{}: {}".format(testcase, solution)