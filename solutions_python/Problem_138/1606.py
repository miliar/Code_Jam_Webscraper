# Google Code Jam 2014 - Problem D Deceitful War
# Steven Stevanus stevenstevanus@gmail.com

def DeceitfulWar():
    try:
        f_input = open('D-large.in','r')
        f_output = open('D-large.ou','w')
        case = int(f_input.readline().strip('\n'))
        for i in range(1,case+1):
            N = int(f_input.readline().strip('\n'))
            naomi = [float(j) for j in f_input.readline().strip('\n').split(' ')]
            ken = [float(j) for j in f_input.readline().strip('\n').split(' ')]
            naomi.sort()
            ken.sort()
            y = []
            z = []
            for j in naomi:
                for k in ken:
                    if j > k and k not in y:
                        y.append(k)
                        break

            for j in ken:
                for k in naomi:
                    if j > k and k not in z:
                        z.append(k)
                        break
                    
            f_output.write('Case #'+str(i)+': '+str(len(y))+' '+str(N-len(z))+'\n')
            
    except:
        print ("Error reading file")

    f_input.close()
    f_output.close()

if __name__ == '__main__':
    DeceitfulWar()
    
