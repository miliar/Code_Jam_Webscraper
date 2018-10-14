def main(s):
    x=True
    i=0
    while x and i<len(s)-1:
        if s[i]>s[i+1] :
            x=False
        else :
            i= i+1
    return x
x=int(input())
for i in range(x):
    no=input()
    n=int(no)
    while n>0 :
        if main(str(n)) :
            break
        else :
            n=n-1
    print"Case #"+str(i+1)+": "+str(n)