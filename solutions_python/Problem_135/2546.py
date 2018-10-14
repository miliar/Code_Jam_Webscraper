f = open('A-small-attempt2.in','r')
testcases = int(f.readline())
for testcase in range(1,testcases+1):
    first_row = int(f.readline()) - 1
    roster = []
    for row in range(0,4):
        roster.append([])
        curr_row = f.readline().split()
        for i in range(0,4):
            roster[row].append(int(curr_row[i]),)
    is_in1 = set(roster[first_row])
    second_row = int(f.readline()) - 1
    roster = []
    for row in range(0,4):
        roster.append([])
        curr_row = f.readline().split()
        for i in range(0,4):
            roster[row].append(int(curr_row[i]),)
    is_in2 = set(roster[second_row])
    if len(list(is_in1 & is_in2))==1:
        number = list(is_in1 & is_in2)[0]
        output = "Case #"+str(testcase)+": "+str(number)
    elif len(list(is_in1 & is_in2))==0:
        output = "Case #"+str(testcase)+": Volunteer cheated!"
    else:
        output = "Case #"+str(testcase)+": Bad magician!"
    f2 = open('A-small-out.txt', "a")
    f2.write(output)
    f2.write("\n")
    f2.close()
