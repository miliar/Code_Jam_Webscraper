def Bin_to_int(s):
    n = len(s)
    output = 0
    for k in range(n):
        output = output+int(s[n-k-1])*2**k
    return output

def int_to_Bin(n):
   if n < 2:
      return str(n)
   else:
      return int_to_Bin(n//2) + str(n%2)



def PbA(Input):
    f = open(Input)
    T = f.readline()
    T = int(T.rstrip('\n'))

    Map = {'+':'0','-':'1'}
    Exchange = {'0':'1','1':'0'}
    # print(T==4)
    out = open("output.txt",'w')
    count = 1
    for line in f:
        L = line.rstrip('\n')
        L= L.split(' ')

        Pancake = ''
        N = len(L[0])
        for k in range(N):
            
            Pancake = Pancake + Map[L[0][k]]

        Pancake = Bin_to_int(Pancake)
        K = int(L[1])

        List =[Pancake];

        Visited = [];
        Order = {Pancake:0}
        Found = False
        while len(List)>0:

            Pancake = List[0]
            List = List[1:]
            if Pancake == 0:
                Found = True
                break
            if Pancake not in Visited:
                Visited = Visited + [Pancake]
                Pancake_s = int_to_Bin(Pancake)
                Pancake_s = '0'*(N-len(Pancake_s)) + Pancake_s

                for k in range(N-K+1):
                    New_Pancake_s = Pancake_s[0:k]
                    for l in range(K):
                        New_Pancake_s = New_Pancake_s+Exchange[Pancake_s[k+l]]
                    New_Pancake_s = New_Pancake_s + Pancake_s[k+K:]

                    New_Pancake_i = Bin_to_int(New_Pancake_s)
                    List = List + [New_Pancake_i]
                    if New_Pancake_i not in Order:
                        Order[New_Pancake_i] = Order[Pancake]+1
            


        if Found == True:
            out.write('Case #'+str(count)+': '+str(Order[Pancake])+'\n')
        else:
            out.write('Case #'+str(count)+': '+'IMPOSSIBLE'+'\n')
        count = count+1

    out.close()
        
