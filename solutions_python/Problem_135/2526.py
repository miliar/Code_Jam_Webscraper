def f():
    i=1
    l = input().splitlines()[1:]
    l = [[int(x) for x in y.split()] for y in l]
    while(l):
        s=set.intersection(set(l[l[0][0]]), set(l[5+l[5][0]]))
        print("Case #"+str(i)+": ", end='')
        if len(s)==1:
            print (s.pop())
        elif len(s)!=0:
            print ("Bad magician!")
        else:
            print ("Volunteer cheated!")
        i+=1
        l = l[10:]
        
