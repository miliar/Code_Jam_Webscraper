import re,string,sys
file = open('C-small-attempt2.in')
N = file.readline().rstrip("\r\n")
N=int(N)
for i in range(N):
    line = file.readline().rstrip("\r\n")
    lenght= len(line)-len("welcome to code jam")+1
    found=0
    for n1 in range(lenght):
        if (line[n1]=='w'):
            l=lenght+1
            for n2 in range(n1,l):
                if line[n2]=='e':
                    l=lenght+2
                    for n3 in range(n2+1,l):
                        if line[n3]=='l':
                            l=lenght+3
                            for n4 in range(n3+1,l):
                                if line[n4]=='c':
                                    l=lenght+4
                                    for n5 in range(n4+1,l):
                                        if line[n5]=='o':
                                            l=lenght+5
                                            for n6 in range(n5+1,l):
                                                if line[n6]=='m':
                                                    l=lenght+6
                                                    for n7 in range(n6+1,l):
                                                        if line[n7]=='e':
                                                            l=lenght+7
                                                            for n8 in range(n7+1,l):
                                                                if line[n8]==' ':
                                                                    l=lenght+8
                                                                    for n9 in range(n8+1,l):
                                                                        if line[n9]=='t':
                                                                            l=lenght+9
                                                                            for n10 in range(n9+1,l):
                                                                               if line[n10]=='o':
                                                                                    l=lenght+10
                                                                                    for n11 in range(n10+1,l):
                                                                                        if line[n11]==' ':
                                                                                            l=lenght+11
                                                                                            for n12 in range(n11+1,l):
                                                                                                if line[n12]=='c':
                                                                                                    l=lenght+12
                                                                                                    for n13 in range(n12+1,l):
                                                                                                        if line[n13]=='o':
                                                                                                            l=lenght+13
                                                                                                            for n14 in range(n13+1,l):
                                                                                                                if line[n14]=='d':
                                                                                                                    l=lenght+14
                                                                                                                    for n15 in range(n14+1,l):
                                                                                                                            if line[n15]=='e':
                                                                                                                                l=lenght+15
                                                                                                                                for n16 in range(n15+1,l):
                                                                                                                                    if line[n16]==' ':
                                                                                                                                        l=lenght+16
                                                                                                                                        for n17 in range(n16+1,l):
                                                                                                                                            if line[n17]=='j':
                                                                                                                                                l=lenght+17
                                                                                                                                                for n18 in range(n17+1,l):
                                                                                                                                                    if line[n18]=='a':
                                                                                                                                                        l=lenght+18
                                                                                                                                                        for n19 in range(n18+1,l):
                                                                                                                                                           if line[n19]=='m':
                                                                                                                                                               found+=1

    sys.stdout.write("Case #"+str(i+1)+": ")
    if(found<9999):
        out="%4.d" %found
        print(out.replace(" ","0"))
    else:
        print(int(found%10000))
