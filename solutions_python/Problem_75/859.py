# Problem B. Magicka

current = -1

with open('input.txt') as a_file:

    for a_problemset in a_file: # Case #current : []

        current += 1

        if current == 0: # 문제 수를 구하기 위해 딱 한번 실행. 사실 필요없음.
            number_of_problem = a_problemset.strip()
            continue

        line = a_problemset.split()

        # combine
        combine_count = int(line[0])
        combine = []

        for val in range(combine_count):
            combine.append(line[val+1])

        # opposed
        opposed_count = int(line[combine_count+1])
        opposed = []

        for val in range(opposed_count):
            opposed.append(line[combine_count+1+val+1])

        # element
        element_count = int(line[combine_count+1+opposed_count+1])
        element = line[combine_count+opposed_count+3]

        #print(combine)
        #print(opposed)
        #print(element)

        invoke = []

        for val in element:
            invoke.append(val)

            if len(invoke) >= 2 :
                # check combine
                combine_1 = invoke[len(invoke)-2] + invoke[len(invoke)-1]
                combine_2 = invoke[len(invoke)-1] + invoke[len(invoke)-2]                 
                for one_combine in combine:
                    match = one_combine[0] + one_combine[1]
                    to = one_combine[2]
                    if combine_1 == match or combine_2 == match :
                        print('combine')
                        invoke.pop()
                        invoke.pop()
                        invoke.append(to)
                    
                # check opposed
                if len(invoke) >= 2 :
                    for one_opposed in opposed:
                        if invoke.count(one_opposed[0]) :
                            if invoke.count(one_opposed[1]) :
                                print('opposed')
                                invoke = []
                            

        print(invoke)

        with open('output.txt', mode='a') as o_file:
            o_file.write('Case #')
            o_file.write(str(current))
            o_file.write(': [')

            comma = 0
            for spell in invoke:
                if comma : o_file.write(', ')
                o_file.write(spell)
                comma = 1

            o_file.write(']\n')
