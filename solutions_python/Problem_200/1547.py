t = int(input())
for i in range(1, t + 1):
    s = input()    
    l = [int(c) for c in s]
    
    begin = None
    for j in range(len(l) - 1):
        if l[j] == l[j+1]:
            if l[j+1] == l[-1]:
                begin = None
            else:
                if begin is None:
                    begin = j
        elif l[j] > l[j+1]:
            if begin is None:
                begin = j
            break
        else:
            begin = None

    if begin is not None:
        l[begin] -= 1
        for j in range(begin+1, len(l)):
            l[j] = 9
        if l[begin] == 0: # then begin == 0
            l = l[1:]

    print("Case #{}: {}".format(i, ''.join(str(e) for e in l)))


    
        
            
