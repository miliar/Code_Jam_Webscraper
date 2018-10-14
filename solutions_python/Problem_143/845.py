input = open("input.txt", "r")

cases = int(input.readline())

for case in range(cases):
    this_case = input.readline().split()
    A = int(this_case[0])
    B = int(this_case[1])
    K = int(this_case[2])
    result = 0
    for x in range(A):
        for y in range(B):
            if x & y < K:
                result += 1
    
    print "Case #%i: %i" % (case+1, result)

input.close()