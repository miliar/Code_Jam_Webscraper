import re
cases = int(input())

for n in range(0,cases):

    no = int(input())

    s = str(no)
    fullpatt = re.compile(r"(\d)\1+")
    allmatch = fullpatt.search(s)
    if(allmatch!=None):
        if(len(allmatch.group()) == len(s)):
            pass
    else :
        patt = re.compile(r"(\d)\1")
        matc = patt.search(s)
        if(matc!=None):
            kk = matc.span()
            m = int(kk[0])
            m = m+1
            sliced = int(s[m:])
            no = no - sliced

    for i in range(no,0,-1):
        temp = i
        minimum = temp % 10
        temp = temp // 10
        while(temp > 0):
          k = temp % 10
          if(k <= minimum):
             minimum = k
             temp = temp//10
          else :
             break
            
        if(temp == 0):
            print("Case #{}: {}".format(n+1,i))
            break
