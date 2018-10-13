T = raw_input()
T = int(T)

for inp in range(T):
    line = raw_input()
    tokens = line.split()
    A = int(tokens[0])
    B = int(tokens[1])
    
    delta = B-A
    count = 0

    for i in range(A, B):
        string = str(i)
        arr = []
        for j in range(1, len(string)):
            n = string[j:] + string[0:j]
            n = int(n)

            if n > i and n <= B and n not in arr:
                arr.append(n)
                count += 1


    print "Case #" + str(inp+1) + ": " + str(count)

