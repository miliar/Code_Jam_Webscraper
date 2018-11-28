#!/usr/bin/python

T = int(raw_input())
for case in range(T):
    line = raw_input().split()
    line.reverse()
    combinations = {}
    oppositions  = {}

    C = int(line.pop())
    for c in range(C):
        combination = line.pop()
        combinations[(combination[0], combination[1])] = combination[2]
        combinations[(combination[1], combination[0])] = combination[2]

    D = int(line.pop())
    for d in range(D):
        opposition = line.pop()
        oppositions[opposition[0]] = (opposition[1],) if opposition[0] not in oppositions else oppositions[opposition[0]] + (opposition[1],)
        oppositions[opposition[1]] = (opposition[0],) if opposition[1] not in oppositions else oppositions[opposition[1]] + (opposition[0],)

    line.pop()
    invocations = line.pop()

    element_list = []
    for invocation in invocations:
        element_list.append(invocation)
        #print element_list

        do_elimination = True
        # Check for combinations
        while len(element_list) >= 2 and ((element_list[-2], element_list[-1]) in combinations or (element_list[-1], element_list[-2]) in combinations):
            if (element_list[-2], element_list[-1]) in combinations:
                result = combinations[(element_list[-2], element_list[-1])]
            else:
                result = combinations[(element_list[-1], element_list[-2])]
            element_list.pop()
            element_list.pop()
            element_list.append(result)
            do_elimination = False
            #print element_list

        # Check for eliminations
        if do_elimination and (invocation in oppositions):
            for e in oppositions[invocation]:
                if e in element_list:
                    element_list = []
                    #print element_list

    print ("Case #%s: %s"  % (str(case + 1), element_list)).replace("'", '')

