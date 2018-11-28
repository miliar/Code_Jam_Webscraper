arr=[]
def revert(arr,index,s,flip):
    for i in range(index,index+flip):
        if(arr[i]=='-'):
            arr[i]='+'
        else:
            arr[i]='-'

def comp(arr,k,size):
    for i in range(k,size):
        if(arr[i]=='-'):
            return False
    return True;


def main():
    t=raw_input()
    for num in range(int(t)):
        string=raw_input()
        l=string.split()
        arr=list(l[0])
        s=len(arr)
        f=int(l[1])
        count=0

        for k in range(s-f+1):
              if(arr[k]=='-'):
                count+=1
                revert(arr,k,s,f);
        if(comp(arr,k,s)==True):
            print "Case #"+str(num+1)+":",count
        else:
            print "Case #"+str(num+1)+": IMPOSSIBLE"
    

if __name__=="__main__":
    main()

