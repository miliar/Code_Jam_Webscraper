
def translate(string, n):
    A = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    C = ['y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q']
    L = []
    W = []
    S = []
    for i in string:
        c = list(i)
        for k in c:
            ind = C.index(k)
            L.append(A[ind])
        W.append("".join(L))
        del L[:]
        S = " ".join(W)
    del W[:]
    file2 = open("spk_out.txt", 'a')
    file2.write("Case #"+str(n)+": ")
    file2.write(S)
    file2.write("\n")
    file2.close()
        

file1 = open("spk_in.txt", 'r')
n = int(file1.readline())
for i in range(n):
    l = file1.readline()
    s = l.split()
    translate(s, i+1)



        
