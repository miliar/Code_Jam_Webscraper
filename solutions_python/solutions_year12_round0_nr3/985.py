# -*- codi9ng: cp932 -*-

num_in = input()
num_out = 1

while 0 < num_in :
    ans = 0
    ab = raw_input()
    a = ab.split()[0] 
    b = ab.split()[1]
    discover = []
    l =  range(int(a),int(b)+1)
    
    digits = len(a) 

    while int(a) < int(b):
        a = str(a)

        if digits == 1: 
            ans = 0


        if digits == 2: 
            search = int(a[1]+a[0])
            if search in l:
                if search > int(a):
                    discover.append(a+str(search))
                    #l.remove(search)
                    
        if digits == 3: 
            search = int(a[2]+a[0]+a[1])
            if search in l:
                if search > int(a):
                    discover.append(a+str(search))
            search = int(a[1]+a[2]+a[0])
            if search in l:
                if search > int(a):
                    discover.append(a+str(search))
                    
        if digits == 4:
            search = int(a[3]+a[0]+a[1]+a[2])
            if search in l:
                if search > int(a):
                    discover.append(a+str(search))
            search = int(a[2]+a[3]+a[0]+a[1])
            if search in l:
                if search > int(a):
                    discover.append(a+str(search))
            search = int(a[1]+a[2]+a[3]+a[0])
            if search in l:
                if search > int(a):
                    discover.append(a+str(search))
        a = int(a)
        a += 1

    discover = list(set(discover))
    
    
    print "Case #"+str(num_out)+": " + str(len(discover))
    num_in -= 1
    num_out += 1


