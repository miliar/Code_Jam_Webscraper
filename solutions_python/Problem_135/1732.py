f1=open('C:/Python27/thing', 'w+')

linelist = []
for line in open('C:\Users\User\Downloads\A-small-attempt0.in'):
    linelist.append(line.rstrip('\n'));

testnum = int(linelist[0]);

for i in xrange(testnum):
    subset = [linelist[x] for x in xrange(10*i+1,10*(i+1)+1)]
    firstset = subset[int(subset[0])].split()
    secondset = subset[int(subset[5])+5].split()
    options = set(firstset).intersection(set(secondset))
    if len(options)==0:
        f1.write("Case #"+str(i+1)+": Volunteer cheated!\n")
    elif len(options)==1:
        f1.write("Case #"+str(i+1)+": "+list(options)[0]+"\n")
    else:
        f1.write("Case #"+str(i+1)+": Bad magician!\n")
    
f1.close()
