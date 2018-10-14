def strictly_increasing(L):
    return all(x<=y for x, y in zip(L, L[1:]))

t=input()
te=1
with open("\Users\SridharReddy\Downloads\r.txt","w") as f1:
        while(te<=t):
                i=input()
                while(i!=0):
                        if(strictly_increasing(list(str(i)))):
                                f1.write("Case #"+str(te)+":"+" "+str(i)+"\n")
                                break
                        else:
                                i=i-1
                                strictly_increasing(list(str(i)))
                te=te+1
