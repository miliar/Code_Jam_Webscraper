'''
Created on 14 Apr 2012

@author: manofest
'''
import os

folder = 'C1'
input_file_name = 'C-small-attempt0.in' 
output_file_name = 'C-small-attempt0.out'



def Process(input_file):
    output = open(folder + os.sep + output_file_name,'wb')
    
    total = input_file.readline().strip()
    
    #results = []
    case = 1
    print "Processing and writing out file"
    for line in input_file:
        results_list = []
        count_matches = 0
        row = line.split()
        ranges = range(int(row[0]),int(row[1]))
        
        if (len(row[0]) == 1 and len([1]) == 1):
            pass
        
        for i in ranges:
            #print i
            m = ''
            n = ''
            m = str(i)
            n = str(i)
            #print m
            
            length = len(str(i -1));
            for j in range(length):
                
                m = m[-1] + m[0:-1]
                
                if (int(m) <= (int(row[1])) and int(m) > int(n) and int(m) >= (int(row[0]))):
                    #print str(m) + ", " + str(n)
                    res = [m,n]
                    if res not in results_list:
                        results_list.append(res)
                        count_matches = count_matches + 1
        print count_matches
                
                             
        output.write("Case #" + str(case) + ": " + str(count_matches) + "\n")
        case = case + 1
    
    output.close()


if __name__ == '__main__':
    import time
    t0= time.clock()
    print "Starting"
    input_file = open(folder + os.sep + input_file_name)
    Process(input_file)
    
    input_file.close()
    print "Finished Processing"
    t= time.clock() - t0
    print t