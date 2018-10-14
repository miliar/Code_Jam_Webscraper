def case():
    t=input()
    i=1
    while i<=t:
        n=input()
        temp=check(n)
        print '{}{}: {}'.format('Case #',i,temp)
        i=i+1
    return

def check(n):
    i=n
    while i>=1:
        temp=str(i)
        #print temp
        l=len(temp)
        j=l-1
        flag=0
        while j>0:
            if temp[j] < temp[j-1]:
              #  print '{} > {}'.format(temp[j],temp[j-1])
                flag=1
                break
            j=j-1
        if flag==0:
            return i
        i=i-1
    return i


def main():
    case()

main()
