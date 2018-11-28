def solve(infile,outfile):
    ent = open(infile,'r')
    sal = open(outfile,'w')
    T = int(ent.readline())
    for t in range(1,T+1):
        sta1 = 'X won'
        sta2 = 'O won'
        sta3 = 'Draw'
        sta4 = 'Game has not completed'
        rw1 = ent.readline()
        rw2 = ent.readline()
        rw3 = ent.readline()
        rw4 = ent.readline()
        espacio = ent.readline()
        res = 0
        for i in range(4):
            if rw1[i] == 'O' and rw2[i] == 'O' and rw3[i] == 'O' and rw4[i] == 'O' :
                sal.write('Case #'+str(t)+': '+sta2+'\n')
                res = 1
                break
            elif rw1[i] == 'T' and rw2[i] == 'O' and rw3[i] == 'O' and rw4[i] == 'O':
                sal.write('Case #'+str(t)+': '+sta2+'\n')
                res = 1
                break
            elif rw1[i] == 'O' and rw2[i] == 'O' and rw3[i] == 'O' and rw4[i] == 'T':
                sal.write('Case #'+str(t)+': '+sta2+'\n')
                res = 1
                break
            elif rw1[i] == 'X' and rw2[i] == 'X' and rw3[i] == 'X' and rw4[i] == 'X':
                sal.write('Case #'+str(t)+': '+sta1+'\n')
                res = 1
                break
            elif rw1[i] == 'X' and rw2[i] == 'X' and rw3[i] == 'X' and rw4[i] == 'T':
                sal.write('Case #'+str(t)+': '+sta1+'\n')
                res = 1 
                break
            elif rw1[i] == 'T' and rw2[i] == 'X' and rw3[i] == 'X' and rw4[i] == 'X':
                sal.write('Case #'+str(t)+': '+sta1+'\n')
                res = 1
                break
            else: 
                res = 0
        #print res
        if res == 0:
            if rw1[0]== rw2[1] == rw3[2] == rw4[3] == 'O' or rw1[3]== rw2[2] == rw3[1] == rw4[0] == 'O':
                sal.write('Case #'+str(t)+': '+sta2+'\n')
                res = 1
            elif rw1[0]== rw2[1] == rw3[2] == rw4[3] == 'X' or rw1[3]== rw2[2] == rw3[1] == rw4[0] == 'X':
                sal.write('Case #'+str(t)+': '+sta1+'\n')
                res = 1
            elif rw1[0]== rw2[1] == rw3[2] == 'O' and rw4[3] == 'T':
                sal.write('Case #'+str(t)+': '+sta2+'\n')
                res = 1
            elif rw1[0]== rw2[1] == rw3[2] == 'X' and rw4[3] == 'T':
                sal.write('Case #'+str(t)+': '+sta1+'\n')
                res = 1
            elif rw1[3]== rw2[2] == rw3[1] == 'O' and rw4[0] == 'T':
                sal.write('Case #'+str(t)+': '+sta2+'\n')
                res = 1
            elif rw1[3]== rw2[2] == rw3[1] == 'X' and rw4[0] == 'T':
                sal.write('Case #'+str(t)+': '+sta1+'\n')
                res = 1
            else:
                B = rw1+'\n'+rw2+'\n'+rw3+'\n'+rw4
                if 'OOOT\n' in B or 'TOOO\n' in B or 'OOOO' in B:
                    sal.write('Case #'+str(t)+': '+sta2+'\n')
                elif 'XXXT\n' in B or 'TXXX\n' in B or 'XXXX' in B:
                    sal.write('Case #'+str(t)+': '+sta1+'\n')
                elif '.' in B and res == 0:
                    sal.write('Case #'+str(t)+': '+sta4+'\n')
                else:
                    sal.write('Case #'+str(t)+': '+sta3+'\n')
           
        
            
            
  
    
def main():
    solve('A-small-attempt0.in','P1out.out')
    
main()
    