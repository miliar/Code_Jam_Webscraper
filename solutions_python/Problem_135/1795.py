f = open( "testcase.txt", "r" )
array = []

#Test cases
n = int(f.readline())

def compare(table1,table2):
    solution = []
    for i in table1:
        if i in table2:
            solution.append(i)
    return solution

for i in range(n):
    rows_1 = []
    rows_2 = []
    choice_1 = int(f.readline())
    for j in range(4):
        rows_1.append(f.readline().split())
    choice_2 = f.readline()
    for j in range(4):
        rows_2.append(f.readline().split())
    solution = compare(rows_1[int(choice_1)-1],rows_2[int(choice_2)-1])

    if len(solution) == 0:
        print "Case #"+str(i+1)+": Volunteer cheated!"
    elif len(solution) == 1:
        print "Case #"+str(i+1)+": "+str(solution[0])
    else :
        print "Case #"+str(i+1)+": Bad magician!"

f.close()
