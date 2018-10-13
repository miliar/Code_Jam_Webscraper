'''
Created on 2013-4-13

@author: t
'''
import copy

def test(lawn):
#    h_highest = []
#    v_highest=[]
#    for line in lawn:
#        h_highest.append(max(line))
#    for i in range(len(lawn[0])):
#        v_list = []
#        for k in range(len(lawn)):
#            v_list.append(lawn[k][i])
#        v_highest.append(max(v_list))
#    print lawn
    for i in range(len(lawn)):
        for k in range(len(lawn[0])):
            line_h = copy.copy(lawn[i]) 
            line_h.remove(lawn[i][k])
            line_v = []
            for j in range(len(lawn)):
                line_v.append(lawn[j][k])
            line_v.remove(lawn[i][k])
            if (line_h == []) or (line_v == []):
                continue
            else:
#                print 'line_h:' + str(line_h)
#                print 'line_v:' + str(line_v)
                if (lawn[i][k] >= max(line_h)) or (lawn[i][k] >= max(line_v)):
                    continue
                else:
                    return 'NO'
    return 'YES'
                
            
            
#            if lawn[i][k] > max
    
    








if __name__ == "__main__":
    inputfile = open("B-large.in",'r')
    
    outputfile = open('result_large','w')
    num_test = int(inputfile.readline())
    for i in range(num_test):
        lawn=[]
        record = inputfile.readline()
        width = int(record.split(' ')[0])
        length = int(record.split(' ')[1])
        for k in range(width):
            line_records = inputfile.readline().split(' ')
            line_num = []
            for num in line_records:
                line_num.append(int(num))
            lawn.append(line_num)
        outputfile.write('Case #'+str(i+1)+': '+test(lawn)+'\n')
            
            
        
        