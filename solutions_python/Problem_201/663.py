fin="C-large.in"
fout="coutlarge.txt"
file = open(fin, "r")
t=int(file.readline())

arr=[]
ans=[]
for i in range(t):
    temparr = map(int,file.readline().strip().split(' '))
    print temparr
    arr.append(temparr)
    
##t=100
##for i in range(t):
##    arr.append([100,i+1])
##   
##
    
for i in range(t):

    
    if arr[i][0]%2==1:
        cta = 2
        ctb = 0
    else:
        cta=1
        ctb=1

    a = arr[i][0]/2
    b = a - 1

    j = 1

    if j == arr[i][1]:
        if arr[i][0]%2==1:
            print a,a
            l=a
            r=a
        else:
            print a,b
            l=a
            r=b
            

  
    while(j < arr[i][1]):
        if j + cta >= arr[i][1]:
            if a%2==1:
                l=r=a/2
                print a/2,a/2
            else:
                l = a/2
                if a/2-1>0:
                    r = a/2-1
                else:
                    r=0
                print l,r
            break
        elif j + cta + ctb >= arr[i][1]:
            if b%2==1:
                print b/2,b/2
                l=r=b/2
            else:
                 l = b/2
                 if b/2-1>0:
                     r = b/2-1
                 else:
                     r=0
                 print l,r

            break
        childcta = 0 
        childctb =  0
        childa = a/2
        childb = a/2 - 1

        if a%2==1:
            childcta = 2 * cta + ctb
            childctb = 0 + ctb
        else:
            childcta = cta 
            childctb = cta + 2 * ctb


        a = childa
        b = childb
        j = j + cta + ctb
        cta = childcta
        ctb = childctb
        


    ans.append(str(l)+' '+str(r))
            
        
print ans

file.close()
file = open(fout, "w")

for i in range(t):
    file.write("Case #"+str(i+1)+": "+ans[i]+'\n')
file.close()

