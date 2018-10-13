def seprated(n):
    ls = []
    while(n>0):
        x = n%10
        ls.insert(0,x)
        n = n/10
    return ls


def isAsc(list):
    previous = list[0]
    for number in list:
        if number < previous:
            return False
        previous = number
    return True


t = int(raw_input())
for i in range(0,t):
    n = int(raw_input())
    if n<10:
        print "Case #"+str(i+1)+":",n
    else:
        flag = True
        ls = seprated(n)
        while flag:
            if isAsc(ls) == False:
                n = n-1
                #print n
                ls = seprated(n)
            else:
                print "Case #"+str(i+1)+":",n 
                flag = False
                




