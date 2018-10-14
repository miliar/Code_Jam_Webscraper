with open('input.in','r') as f:
    with open('output.out','w')as out:
        n = int(f.readline())
        for i in range(n):
            answer1 = int(f.readline())
            for j in range(4):
                if j == answer1-1:
                    list1 = f.readline().split()
                else:
                    f.readline()    
            #print(list1)
            answer1 = int(f.readline())
            for j in range(4):
                if j == answer1-1:
                    list2 = f.readline().split()
                else:
                    f.readline()
            card = []
            #print(list2)
            for j in list1:
                if j in list2:
                    card.append(j)
            #print(list1)
            #print(list2)
            if len(card) == 0:
                out.write("Case #{}: Volunteer cheated!\n".format(i+1))
            elif len(card) == 1:
                out.write("Case #{}: {}\n".format(i+1,card[0]))
            else:
                out.write("Case #{}: Bad magician!\n".format(i+1))
    
        
