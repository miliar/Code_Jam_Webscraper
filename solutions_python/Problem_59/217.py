



input = open("input.txt","r")    
output = open("output.txt","w+")
cases = int(input.readline())

for case in range(1,cases+1):
    print("--")
    n,m = map(int,input.readline().rstrip().split())
    dirlist = [['']]
    mkdirlist = []
    mkcount = 0
    for i in range(n):
        dirlist.append(input.readline().rstrip().split("/"))
    for j in range(m):
        curdir = input.readline().rstrip().split("/")
        if curdir in dirlist:
            print("%s exists in %s"%(curdir,dirlist))
        else:
            print("%s does not exists in %s"%(curdir,dirlist))  
            for k in range(1,len(curdir)+1):
                if curdir[:k] in dirlist:
                      print("%s exists in %s"%(curdir[:k],dirlist))
                else:
                      print("%s not exists in %s"%(curdir[:k],dirlist))
                      dirlist.append(curdir[:k])
                      mkcount+=1   
        mkdirlist.append(curdir)    
    

    output.write("Case #%d: %d\n"%(case,mkcount))
    print("-*-")