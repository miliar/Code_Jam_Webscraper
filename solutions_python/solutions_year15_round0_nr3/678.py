f = open("c-small.in")

o = open("c-small.out", "w+")

line = f.readline()
T = int(line[:-1])

for rep in range(T):
    line = f.readline()
    L = line[:-1] if line[-1] == '\n' else line
    L = L.split(" ")
    nchars = int(L[0])
    X = int(L[1])

    line = f.readline()
    line = line[:-1] if line[-1] == '\n' else line
    large = line*X
    mod = list(large)
    
    mult =  {'1': {'1': '1', 'i': 'i',  'j': 'j',  'k': 'k'},
             'i': {'1': 'i', 'i': '-1', 'j': 'k',  'k': '-j'},
             'j': {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'},
             'k': {'1': 'k', 'i': 'j',  'j': '-i', 'k': '-1'}}


    if nchars*X < 50:
        print("string:",large)
        
    state = 0
    neg = False
    newchar = large[0]
    for i in range(1,nchars*X):
#        print('->',newchar, end="")
        if state == 0:
            if newchar == 'i' and not neg:
 #               print("\ns0 with +i") 
                state += 1
                newchar = large[i]
 #               print("newchar now %s", newchar)
                continue;
        elif state == 1:
            if newchar == 'j' and not neg:
 #               print("\ns1 with +j") 
                state += 1
                newchar = large[i]
 #               print("newchar now %s", newchar)
                continue;

            
                    
 #       print(large[i],'->',  mult[newchar][large[i]], '(-)' if neg else '(+)')
        try:
            newchar = mult[newchar][large[i]]
        except KeyError:
            print('->',i,'|',newchar, "|", large[i], end="", sep="")

            raise ValueError()
        
        if newchar[0] == '-':
            neg = not neg
            newchar = newchar[1]

 #   print('Exited loop')
                

    ans = 'NO'
    if state == 2 and newchar == 'k' and not neg:
        ans = 'YES'

    
    print("Case #%d: %s\n"%(rep+1, ans))
    o.write("Case #%d: %s\n"%(rep+1, ans))
o.close()
f.close()
