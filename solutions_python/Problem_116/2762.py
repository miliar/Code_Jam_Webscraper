#read the lines
nlines=[]
for line in open('A-small-attempt1.in','r'):
    nlines.append(line)

lines=[]


#removing the \ns
for line in nlines:    
    if line.endswith('\n'):
        line=line[:-1]
    lines.append(line)

#taking no of cases
t=int(lines[0])

#removing the empty gaps
for c in range(0,t):
        lines.remove('')    


##print(lines)
        
#making list for separating cases
cases=[]
for k in range(0,t):
    cases.append([])



print(lines)
print(cases)

print('lines='+str(len(lines)))
#separating cases
cno=0
count=1
for k in range(1,len(lines)):
    print(count)
    print(cno)
    cases[cno].append(lines[count])
    if(count%4==0):
        print('changing cno')
        cno+=1
    count+=1

print('cases= '+str(cases))



f=open('output.txt','w')


#getting results
cno=0
xcombo=['XXXX','XXXT','XXTX','XTXX','TXXX']
ocombo=['OOOO','OOOT','OOTO','OTOO','TOOO']
for case in cases:
    cno+=1
    for line in case:
##        print(line)
        if(line in xcombo):
##            print('line is'+line)
            print('Case #'+str(cno)+': X won')
            break
        elif(line in ocombo):
            print('Case #'+str(cno)+': O won')
            break
        else:
            ldiag=case[0][0]+case[1][1]+case[2][2]+case[3][3]
            rdiag=case[0][3]+case[1][2]+case[2][1]+case[3][0]
            col1=case[0][0]+case[1][0]+case[2][0]+case[3][0]
            col2=case[0][1]+case[1][1]+case[2][1]+case[3][1]
            col3=case[0][2]+case[1][2]+case[2][2]+case[3][2]
            col4=case[0][3]+case[1][3]+case[2][3]+case[3][3]
            if(ldiag in xcombo or rdiag in xcombo or col1 in xcombo or col2 in xcombo or col3 in xcombo or col4 in xcombo):
                print('Case #'+str(cno)+': X won')
                break
            elif(ldiag in ocombo or rdiag in ocombo or col1 in ocombo or col2 in ocombo or col3 in ocombo or col4 in ocombo):
                print('Case #'+str(cno)+': O won')
                break
            else:
                for line in case:
##                    print('line is'+line+' in not complete case')
                    if('.' in line):
                        print('Case #'+str(cno)+': Game has not completed')
                        draw=False
                        notcomplete=True
                        break
                    else:
                        draw=True
        if(draw):
            print('Case #'+str(cno)+': Draw')
            break
        if(notcomplete):
            break

