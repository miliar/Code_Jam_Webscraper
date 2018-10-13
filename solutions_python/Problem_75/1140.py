              

T = int(raw_input())
for i in range(T):
        line = raw_input().split()
        C = int(line[0])
        combine = {frozenset((foo[0], foo[1])):foo[2] for foo in line[1:C+1]}
        D = int(line[C+1])
        oppose = {foo[0]:foo[1] for foo in line[C+2:C+2+D]}
        oppose2 = {foo[1]:foo[0] for foo in line[C+2:C+2+D]}
        N = int(line[C+2+D])
        invoke = line[C+2+D+1]
        
        elements = []
        for char in invoke:
                if len(elements) and frozenset((char, elements[-1])) in combine:
                        elements[-1] = combine[frozenset((char, elements[-1]))]
                elif char in oppose and oppose[char] in elements:
                        elements = []
                elif char in oppose2 and oppose2[char] in elements:
                        elements = []
                else:
                        elements.append(char)

        output = "Case #" + str(i+1) + ": ["
        if len(elements):
                output += elements[0]
                if len(elements) > 1:
                        output += ', '
                output += ', '.join(elements[1:])
        output += ']'
        print output

                        


                
