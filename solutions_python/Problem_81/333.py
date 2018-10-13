'''
Created on Apr 30, 2011

@author: Marius Dorin Moraru
'''

#filename without extension
#fileName = raw_input("Enter a name:")
fileName = "c:/learn/a"

inFile = open(fileName + ".in", "rU")
outFile = open(fileName + ".out", "w")

nrOfTestCases = int(inFile.readline());        
print "nrOfTestCases " + str(nrOfTestCases)




def readTestCase():   
    s = inFile.readline().replace("\n","").replace("\r","");
    n = int(s);
    v = []
    for i in xrange(n):
        s = inFile.readline().replace("\n","").replace("\r","");
        v.append(s)
    return v

#resolve testCase
def resolve(v):
#    print v
    n = len(v)
    r ="";
    w = []
    for i in xrange(n):
        nr = 0;
        wins = 0;
        for j in xrange(len(v[i])):
            if v[i][j] == "1":
                nr = nr + 1
                wins = wins + 1
            if v[i][j] == "0":
                nr = nr + 1
        w.append([nr, wins])
#        print i, w[i]
#    print w
    wp_list =[]
    for i in xrange(n):
        wp = float(w[i][1]) / float(w[i][0]);
        wp_list.append(wp);
    
    owp_list =[]
    for i in xrange(n):
        count = 0
        sum = 0
        for j in xrange(n):
            if v[i][j] != ".":
                count = count + 1
                owp = float(w[j][1]-int(v[j][i])) / float(w[j][0] - 1);
                sum = sum + owp
        owp = float(sum) / float(count);
        owp_list.append(owp)
    
    oowp_list =[]
    for i in xrange(n):
        count = 0
        sum = 0
        for j in xrange(n):
            if v[i][j] != ".":
                sum = sum + owp_list[j];
                count = count + 1;
        oowp = float(sum) / float(count);
        oowp_list.append(oowp)
    
    for i in xrange(n):
        r = r + ("\n" + str(0.25 * wp_list[i] + 0.50 * owp_list[i] + 0.25 * oowp_list[i])); 

        
        
#    print wp_list, owp_list, oowp_list 
    return r


for i in range(nrOfTestCases):
    print "resolving testCase " + str(i + 1)
    out = resolve(readTestCase())
    outFile.writelines("Case #" + str(i + 1)+": " + str(out) + "\n")
outFile.close()


    
        