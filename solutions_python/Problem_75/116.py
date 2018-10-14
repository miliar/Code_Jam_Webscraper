import sys

elements = ['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']
f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    combine = [[None for i in range(0, len(elements))] for j in range(0, len(elements))]
    opposed = [[False for i in range(0, len(elements))] for j in range(0, len(elements))]

    line = f.readline().split()
    C = int(line[0])
    for i in range(1, C + 1):
        triple = line[i]
        a = elements.index(triple[0])
        b = elements.index(triple[1])
        c = triple[2]
        combine[a][b] = combine[b][a] = c
    line = line[C+1:]
    D = int(line[0])
    for j in range(1, D + 1):
        double = line[j]
        a = elements.index(double[0])
        b = elements.index(double[1])
        opposed[a][b] = opposed[b][a] = True
    line = line[D+1:]
    N = int(line[0])
    input = line[1]
    output = []
    for char in input:
        if output:
            next = elements.index(char)
            try:
                last = elements.index(output[-1])
                val = combine[last][next]
                if val is not None:
                    output[-1] = val
                    continue
            except:
                pass

            output.append(char)

            relevant_opposed = opposed[next]
            for i in range(0, len(relevant_opposed)):
                if relevant_opposed[i]:
                    if elements[i] in output:
                        output = [] 
                        break
            continue
        output.append(char)
    print "Case #%d: [%s]" % (case + 1, ",".join(output).replace(",", ", "))
        
