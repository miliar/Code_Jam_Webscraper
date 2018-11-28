f = open('B-small-attempt0.in', 'r')
out = open('q2.out', 'w')
num_cases = int (f.readline())

for i in range(num_cases):
    combos = []
    opposed = []
    tokens = f.readline().strip("\n").split(" ")
    
    num_combos = int(tokens.pop(0))
    
    for j in range(0, num_combos):
        combo = tokens.pop(0)
        combos.append((combo[0], combo[1], combo[2]))
    
    num_opposed = int(tokens.pop(0))
    
    for j in range(0, num_opposed):
        o = tokens.pop(0)
        opposed.append((o[0], o[1]))
        
    sequence = tokens.pop(1)
    
    list = []
    
    for step in sequence:
        list.append(step) 
        if len(list) >= 2:
            combined = False
            a = list[-1]
            b = list[-2]
            
            for combo in combos:
                if (a == combo[0] and b == combo[1]) or (a == combo[1] and b == combo [0]):
                    list = list[0:-2]
                    list.append(combo[2])
                    combined = True
                    break
            if combined:
                continue
            
            for o in opposed:
                test_list = list
                o1 = False
                o2 = False
                for el in test_list:
                    if el == o[0]:
                        o1 = True
                    elif el == o[1]:
                        o2 = True
                if o1 and o2:
                    list = []
                break

    out.write("Case #%d: [%s]\n" % (i+1, ", ".join(list)))