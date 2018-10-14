import sys

T = int(sys.stdin.readline())

for _t in xrange(T):

    line = sys.stdin.readline().split()
    
    C = int(line.pop(0))
    if C > 0:
        i = 0
        combo_elements = []
        while i < C:
            combo_elements.append(line.pop(0))
            i += 1
        
    D = int(line.pop(0))
    if D > 0:
        i = 0
        opposed_elements = []
        while i < D:
            opposed_elements.append(line.pop(0))
            i += 1 

    N = int(line.pop(0))
    if N > 0:
        base = line.pop(0)

    final_elements = []

    while len(base) > 0:
        flag = False
        
        if C > 0:
            i = 0            
            while i < C:
                if base[0] in combo_elements[i][:-1] and \
                        len(final_elements) > 0 and \
                        final_elements[-1] in combo_elements[i][:-1] and \
                        (base[0] != final_elements[-1] or \
                             combo_elements[i][0] == combo_elements[i][1]):
                    final_elements.pop(-1)
                    final_elements.append(combo_elements[i][-1])
                    base = base[1:]
                    flag = True
                    break
                i += 1
            if flag == True:
                continue

        if D > 0:
            i = 0
            while i < D:
                if base[0] in opposed_elements[i]:
                    for element in final_elements:
                        if element in opposed_elements[i] and \
                                element != base[0]:
                            final_elements = []
                            base = base[1:]
                            flag = True
                            break
                i += 1
            if flag == True:
                continue
            
        final_elements.append(base[0])
        base = base[1:]        
        
    print "Case #%d:" % (_t+1), str(final_elements).replace("'","")

        
