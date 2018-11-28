def sol3(A,B):    
    ret = 0
    
    for n1 in range(A,B):
        str1 = str(n1)
        temp = []
        for i in range(len(str1)):
            str2 = str1[i:] + str1[:i]
            if str2 in temp:
                continue
            temp.append(str2)
            
            if str2[0] == '0':
                continue
            
            n2 = int(str2)
            
            if n1 < n2 and n2 <= B:
                ret +=1
    return ret



if __name__ == '__main__':
    f = open("C-small-attempt0.in",'r')
    num = f.readline()
    
    t = open('output.txt','w')
    
    for i in range(int(num)):
        line = f.readline()
        l = line.strip().split()

        A = l[0]
        B = l[1]

        t.write("Case #" + str(i+1) + ": " + str(sol3(int(A),int(B))) + "\n")
        
    f.close()
    t.close()