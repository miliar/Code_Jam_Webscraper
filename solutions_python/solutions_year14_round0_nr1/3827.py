t = raw_input()
t = int(t)
ls = []
lst = []
for i in range(0,t):
    a1 = raw_input()
    a1 = int(a1)
    lst1 = []
    for j in range(0,4):
        temp1 = raw_input()
        lst1.append(map(int,temp1.split(' ')))
    a2 = raw_input()
    a2 = int(a2)
    lst2 = []
    for j in range(0,4):
        temp2 = raw_input()
        lst2.append(map(int,temp2.split(' ')))

    lst.append((a1,lst1,a2,lst2))

flag = 0

def fun(lss):
    for i in range(0,len(lss)):
        (a1,lst1,a2,lst2) = lss[i]
        ele = 0
        cnt = 0
        for a in lst1[a1-1]:
            if(a in lst2[a2-1]):
                cnt += 1
                ele = a                
                  
        if(cnt == 0):
            print "Case #" + str(i+1) + ": Volunteer cheated!" 
        elif(cnt == 1):
            print "Case #" + str(i+1) + ": " + str(ele)
        else:
            print "Case #" + str(i+1) + ": Bad magician!"
        
fun(lst)
