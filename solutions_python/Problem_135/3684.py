loop = int(input())
I = 1
while (loop):
    first_line = int(input())
    first_vector = []
    
    for i in range(4):
        x = input()
        if i == first_line - 1:
            first_vector = x.split(' ')
                
    secound_line = int(input())
    secound_vector = []
    
    for i in range(4):
        x = input()
        if i == secound_line - 1:
            secound_vector = x.split(' ')
    
    if len(set(first_vector+secound_vector)) == 8:
        print ('Case #%d: Volunteer cheated!'%I)
    elif len(set(first_vector+secound_vector)) == 7:
        for i in first_vector:
            for j in secound_vector:
                if i == j:
                    print ('Case #%d: %s'%(I,i))
    else:
        print ('Case #%d: Bad magician!'%I)

    first_vector = secound_vector = []
    I+=1
    loop-=1
