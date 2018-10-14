# -*- coding: cp949 -*-
fin = open('D:/Users/정강식/Desktop/A-large.in')
fout = open('D:/Users/정강식/Desktop/A-large.out', 'w')
numCase = int(fin.readline())
#print 'num of case: ' + str(numCase)
for i in range(numCase):
    #print 'Case #' + str(i+1)
    numChange = 0
    numSE = int(fin.readline())
    #print 'num of search engines: ' + str(numSE)
    listSE = []
    for j in range(numSE):
        listSE.append(fin.readline())
    #print 'list: ', listSE
    listSE2 = listSE[:]
    numQuery = int(fin.readline())
    #print 'num of query: ' + str(numQuery)
    for j in range(numQuery):
        query = fin.readline()
        #print 'remove query: ' + query
        if query in listSE:
            listSE.remove(query)
        #print 'list: ', listSE
        if len(listSE) == 0:
            listSE = listSE2[:]
            listSE.remove(query)
            numChange += 1
    #print 'Case #' + str(i+1) + ': ' + str(numChange)
    fout.write('Case #' + str(i+1) + ': ' + str(numChange) + '\n')
fout.close()
    
    
            
