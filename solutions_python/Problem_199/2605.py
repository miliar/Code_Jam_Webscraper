t = int(input())
c = 1;
while c <= t:
    string = input()
    arr = string.split(' ')
    k = int(arr[1])
    sym = list(arr[0])
    index = 0
    count = 0
    #print(sym)
    
    while index<len(sym):
        #print(index)
        if '-' not in sym:
            break
        if sym[index] == '+':
            index+=1
            continue
        else:
            i = 0
            count += 1
            while i<k:
                if index+k <= len(sym):
                    if sym[index+i]=='+':
                        sym[index+i] = '-'
                    else:
                        sym[index+i] = '+'
                    i+=1
                else:
                    break
            #print(sym)
        index +=1
    if '-' in sym:
        print('Case #'+str(c)+': IMPOSSIBLE')
    else:
        print('Case #'+str(c)+': '+str(count))
        
    c+=1
