T=int(raw_input())

for x in range(1,T+1):
    first_row=int(raw_input())-1
    first_arrangement=[]
    for _ in range(4):
        line1=[ int(a) for a in raw_input().split()]
        first_arrangement.append(line1)
    second_row=int(raw_input())-1
    second_arrangement=[]
    for _ in range(4):
        line1= [int(a) for a in raw_input().split()]
        second_arrangement.append(line1)
    count=0
    num=0
##    print first_arrangement
##    print second_arrangement
    for t in range(4):
        temp=first_arrangement[first_row][t]
        if temp in second_arrangement[second_row]:
            count+=1
            num=temp
    if count==1:
        print "Case #"+str(x)+": "+str(num)
    elif count==0:
        print "Case #"+str(x)+": Volunteer cheated!"
    else:
        print "Case #"+str(x)+": Bad magician!"
