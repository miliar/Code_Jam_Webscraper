'''
Created on 13.04.2013

@author: Alex
'''
   
if __name__ == '__main__':
    f = open('in/A-large.in', mode='r')
    g = open('out/A-large.out', mode='w')
    n = int(f.readline())
    for i in range(1,n+1):
        l = list(f.readline().split())
        levels = int(l[0])
        audience = l[1]
        result = 0
        persons = int(audience[0])
        for j in range(1, levels+1):
            persons_j = int(audience[j])
            if j > persons:
                result += j-persons
                persons = j + persons_j
            else:
                persons += persons_j 
        g.write('Case #' + str(i) + ': ' + str(result) + '\n')        
        