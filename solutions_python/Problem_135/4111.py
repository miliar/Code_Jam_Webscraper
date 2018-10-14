'''
Created on Apr 12, 2014

@author: anupamm
'''

def main():
    fin = open('test','r')
    fout = open('output.txt','w')
    
    T = int(fin.readline())
    
    for i in range(T):
        lineNo1 = int(fin.readline())
        for k in range(4):
            if k == lineNo1 -1:
                data1 = fin.readline().strip().split(' ')
            else:
                fin.readline().strip().split(' ')
        
        lineNo2 = int(fin.readline())
        for k in range(4):
            if k == lineNo2 -1:
                data2 = fin.readline().strip().split(' ')
            else:
                fin.readline().strip().split(' ')
        
        cmon = list(set(data1).intersection(data2))
        
        lengt = len(cmon)
        if lengt == 1:
           val = cmon.pop()
           print 'Case #' + str(i+1) + ': ' + str(val)
           fout.write('Case #' + str(i+1) + ': ' + str(val) + '\n') 
        elif lengt == 0:
            print 'Case #' + str(i+1) + ': ' + "Volunteer cheated!"
            fout.write('Case #' + str(i+1) + ': ' + "Volunteer cheated!" + '\n') 
        else:
            print 'Case #' + str(i+1) + ': ' + "Bad magician!"
            fout.write('Case #' + str(i+1) + ': ' + "Bad magician!" + '\n') 
        
        
if __name__ == '__main__':
    main()
    