def solve():
    srcFile=open("C:\\Users\\Neo\\Desktop\\Learning Python\\google code jam\\CookieClickerAlphaLarge.in")
    rstFile=open("C:\\Users\\Neo\\Desktop\\Learning Python\\google code jam\\CookieClickerAlphaLargeResult.txt","a")
    cases=int(srcFile.readline())
    for case in range(cases):
        var=list(map(lambda x: float(x),srcFile.readline().strip().split(" ")))
        c=var[0]
        f=var[1]
        x=var[2]
        p=2
        used=0
        time=used+x/p
        while time>used+c/p+x/(p+f):
            used+=c/p
            p+=f
            time=used+x/p
        result="Case #"+str(case+1)+": "
        result+=str(time)
        rstFile.write(result+"\n")  
    srcFile.close()
    rstFile.close()
