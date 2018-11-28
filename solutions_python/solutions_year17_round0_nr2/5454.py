from sys import argv

#script, filename = argv

#txt = open(filename)


def isTidy(m):
    x=str(m)
    if len(x)==1:
        return True
    elif len(x)>1 and int(x[len(x)-1])==0:
        return False
    else:
        for j in range(0,len(x)-1):
            if x[j]>x[j+1]:
                j+=1
                return False
            else:
                return True
def isTidyR(m):
    x=str(m)
    if len(x)==1:
        return True
    elif len(x)>1 and x[1:]==0: #int(x[len(x)-1])
        return False
    elif x[0]>x[1]:
        return False
    else:
        return isTidy(x[1:])
            

def tidy(n):
    tidiest=0
    for i in range(1,n+1):
        if isTidyR(i)== True:
            tidiest=i
            i+=1
        else:
            i+=1
    return tidiest

def main():
    #txt=open(filename)
    t = int(input())
    for i in range(1,t+1):
        n=int(input())
        print("Case #{}: {}".format(i,tidy(n)))

main()

#def tidy():
 #   t = int(input())
#"Case #",t,":",,sep=' ', end='\n',file=sys.stdout,flush=False)

def test(m):
    return int(str(m)[1])
