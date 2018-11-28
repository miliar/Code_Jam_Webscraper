'''
Created on Apr 13, 2013

@author: Federico
'''
lst_number = [line.strip() for line in open('B-small-attempt2.in', "r")]
file_solution = open('result.txt', 'w')

number_test = int(lst_number.pop(0))

for i in range(1, number_test + 1):
    array = []

    N, M = map(int, lst_number.pop(0).split())

    if N == 1 or M == 1:
        if N == 1:
            lst_number.pop(0)
        elif M == 1:
            for j in range(N):
                lst_number.pop(0)
        print "Case #%d: YES"%(i)
        file_solution.write("Case #%d: YES\n"%(i))
    else:
        string = "Case #%d: %s"%(i, "YES")
        
        for j in range(N):
            array.extend(map(int, lst_number.pop(0).split()))

        height = set(array)

        if len(height) == 1:
            print "Case #%d: YES"%(i)
            file_solution.write("Case #%d: YES\n"%(i))
            continue

        for j in range(N):
            row = array[M * j:M+M*j]

            if len(set(row)) != 1:
                number_times = 0
                for x in range(M):
                    if sum(array[x::M]) == N:
                        number_times += 1
#                if i == 3:
#                    print row
#                    print row.count(1)
#                    print number_times
                if row.count(1) != number_times:
                    string =  "Case #%d: %s"%(i, "NO")
                    break

                        
        
        
        print string
        file_solution.write(string+"\n")
        