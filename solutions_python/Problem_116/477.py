
inp = open("C:/Users/Mariusz/Desktop/input.txt","r")
out = open("C:/Users/Mariusz/Desktop/output.txt","w")




if __name__ == '__main__':
    T = int(inp.readline()[:-1])
    for i in range(1,T+1):
        cases=[]
        s=''
        for j in range(4):
            x = inp.readline()[:-1]
            s+=x
        for j in range(0,15,4):
            cases.append(s[j:j+4])
        pion=['','','','']
        for j in range(len(s)):
            pion[j%4] += s[j]
        cases += pion
        vert=['','']
        for j in range(0,len(s),5):
            vert[0]+= s[j]
        for j in range(3,len(s)-3,3):
            vert[1]+= s[j]
        
        cases += vert

        noend_flag = False
        en = False
        for case in cases:
            if '.' in case:
                noend_flag = True

            if not en and case.count('X') == 4 or (case.count('X') == 3 and 'T' in case):
                out.write("Case #{0}: {1}".format(i, 'X won')+'\n')
                en = True
                break
            elif not en and case.count('O') == 4 or (case.count('O') == 3 and 'T' in case):
                out.write("Case #{0}: {1}".format(i, 'O won')+'\n')
                en = True
                break

        if not en:
            if noend_flag:
                out.write("Case #{0}: {1}".format(i, 'Game has not completed')+'\n')
                en = True
            else:
                out.write("Case #{0}: {1}".format(i, 'Draw')+'\n')
                en = True
                
        inp.readline()
            
            
            







        #out.write("Case #{0}: {1}".format(i, result)+'\n')
      #  print("Case #{0}: {1}".format(i, result))

    inp.close()
    out.close()
