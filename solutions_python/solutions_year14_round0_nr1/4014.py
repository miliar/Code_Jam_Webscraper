import sys
def mgc():
    f = open('A-small-attempt1.in','r')
    tc = f.readline()
    tc = (int)(tc)
    a = []
    for k in range(0,tc):
        b = []
        no = f.readline()
        no = (int)(no)
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        line4 = f.readline()
        d = {}
        d[1] = line1
        d[2] = line2
        d[3] = line3
        d[4] = line4
        line = d[no]
        line = line.split()
        no = f.readline()
        no = (int)(no)
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        line4 = f.readline()
        d = {}
        d[1] = line1
        d[2] = line2
        d[3] = line3
        d[4] = line4
        lin = d[no]
        lin = lin.split()
        for i in line:
            for j in lin:
                if i == j:
                    b.append(i)
        if len(b) == 0 or len(b)>1:
            if len(b) == 0:
                a.append('Volunteer cheated!')
            else :
                a.append('Bad magician!')
        else :
            a.append(b[0])
    f.close()
    j = 1
    f1 = open('output.txt','w')
    for i in a:
        f1.write("Case #%d: %s\n" %(j,i))
        j = j+1
    f1.close()
def main():
    mgc()

if __name__ == '__main__':
    main()
