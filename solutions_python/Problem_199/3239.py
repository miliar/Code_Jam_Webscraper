
def flip(case,start,end):
    output = []
    for i in range(0,len(case)):
        if i < start:
            output.append(case[i])
        elif i > end-1:
            output.append(case[i])
        else:
            output.append(not case[i])
    return output
                       

def all_happy(case):
    for e in case:
        if e == False:
            return False
    #print case," All Happy"
    return True

def case2binary(case):
    output = []
    for e in case:
        if e == '+':
            output.append(True)
        elif e == '-':
            output.append(False)
    return output

f = open("A-large.in")
w = open("q1-output.txt",'w')

num_tests = f.readline()
test_case = 1
for line in f:
    output_prefix = "Case #"+str(test_case)+": "
    case = line.strip().split(" ")
    case_b = case2binary(case[0])
    width = int(case[1])
    index = 0
    count = 0
    while(not all_happy(case_b) and index + width <= len(case_b)):
        if not case_b[index]:
            #print "Before: ",case_b
            case_b = flip(case_b,index,index+width)
            count += 1
            #print "After: ",case_b
        index += 1
    if all_happy(case_b):
        print count
        w.write(output_prefix + str(count)+'\n')
    else:
        print "IMPOSSIBLE"
        w.write(output_prefix + "IMPOSSIBLE\n")
    test_case += 1
    
w.close()
f.close()
