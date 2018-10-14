'''
Created on 3 May 2014

@author: Nigel.Fernandez
'''

#import time

if __name__ == '__main__':
    
    #start = time.time()
    
    fread = open('B-small-attempt0.in', 'r')
    fwrite = open('B_small_output.dat', 'w')
    c_num = int(fread.readline())
    
    for i in range(c_num):
        case = fread.readline().split(" ")
        
        a = int(case[0])
        b = int(case[1])
        c = int(case[2])
        count = 0;
        for j in range(a):
            for k in range(b):
                if (j & k < c):
                    count += 1
        
        fwrite.write('Case #' + str(i + 1) + ': ' + str(count) + '\n')
   
    fread.close()
    fwrite.close()
    #stop = time.time()
    #print "Time " + str(stop - start) + " s" 