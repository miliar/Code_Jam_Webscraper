input_file=open('E:\A-large.in', 'r')
output_file=open('A-large.out', 'w')

test_cases=int(input_file.readline())

for case_num in range(1, test_cases+1):
    num_wires=int(input_file.readline())
    wires = [[0, 0]] * num_wires
    #print wires
    for i in range(num_wires):
        wire = input_file.readline().split()
        wires[i] = map(int, wire)
    #print wires
    result = 0
    for i in range(num_wires):
        for j in range(i+1, num_wires):
            a1 = wires[i][0]
            b1 = wires[i][1]
            a2 = wires[j][0]
            b2 = wires[j][1]
            #print a1, b1, a2, b2
            #print (a1-a2)*(b1-b2)
            if (a1-a2)*(b1-b2) < 0:
                result += 1
    #print result
    output_file.write("Case #%s: %s\n" %(case_num, result))

input_file.close()    
output_file.close()
