in_file = open("C-small-1-attempt3.in","r")
T = in_file.readline()
T = int(T)

out_file = open("C-small-1-attempt3.out","w")




def DIV(X):
    if X%2 == 0:
        return [int((X-2)/2), int(X/2)]
    else:
        return [int((X-1)/2), int((X-1)/2)]




    
for t in range(T):
    N = ""
    while True:
        c = in_file.read(1)
        if c != " ":
            N = N + c
        else:
            break
    N = int(N)

    K = ""
    while True:
        c = in_file.read(1)
        if c != "\n":
            K = K + c
        else:
            break
    K = int(K)



    s = [N]
    i = 0
    while i < K:
        a = DIV(s[i])
        ans = [a]
        s = s + a
        s.sort()
        s.reverse()
        i = i + 1

    a.sort()
    a.reverse()
    print(a)
    out_file.write("Case #"+str(t+1)+": "+str(a[0])+" "+str(a[1])+"\n")

in_file.close()
out_file.close()  


    

