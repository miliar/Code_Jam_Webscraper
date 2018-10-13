f = open('C-small-attempt1.in', 'r')
output = open('C-Output.txt', 'w')
T = int(f.readline())
cT = 1

while cT <= T:
    l = f.readline()[:-1]
    sep = l.split(" ")
    A, B = int(sep[0]), int(sep[1])

    num_results = 0
    for i in range(A, B+1):
        if len(str(i)) == 2:
            attempt = int(str(i)[1]+str(i)[0])
            if len(str(i)) == len(str(attempt)) and attempt > i and i >= A and\
                                                B >= attempt:
                #print(i, attempt)
                num_results += 1

        if len(str(i)) == 3:
            attempt1 = int(str(i)[2]+str(i)[0]+str(i)[1])
            if len(str(i)) == len(str(attempt1)) and attempt1 > i and i >= A and\
                                                B >= attempt1:
                #print(i, attempt1)
                num_results += 1

            attempt2 = int(str(i)[1]+str(i)[2]+str(i)[0])
            if len(str(i)) == len(str(attempt2)) and attempt2 > i and i >= A and\
                                                B >= attempt2:
                #print(i, attempt2)
                num_results += 1

    output.write("Case #"+str(cT)+": "+str(num_results)+"\n")
    print("Case #"+str(cT)+": "+str(num_results))
    cT += 1

output.close()
