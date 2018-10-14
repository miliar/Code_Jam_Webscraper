n = int(raw_input())

c=1

def get(num):
    for i in range(num,0,-1):
        l = [int(d) for d in str(i)]
        if sorted(l) == l:
            print "Case #"+ str(c)+":",i
            return


while n:

    num =  int(raw_input())

    get(num)

    c+=1

    n-=1
