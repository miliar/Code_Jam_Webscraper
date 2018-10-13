t = int(raw_input())

for k in range(t):
    first = int(raw_input())
    for i in range(1,5):
        if i==first:
            first_set = {e for e in raw_input().split(" ")}
        else:
            raw_input()
    second = int(raw_input())
    for i in range(1,5):
        if i==second:
            second_set = {e for e in raw_input().split(" ")}
        else:
            raw_input()
    inter = first_set.intersection(second_set)
    if len(inter)==0:
        print "Case #"+str(k+1)+": Volunteer cheated!"
    elif len(inter)>1:
        print "Case #"+str(k+1)+": Bad magician!"
    else:
        print "Case #"+str(k+1)+": "+str(inter.pop())
