'''
Created on 13 Apr 2013

@author: Landi
'''
import numpy as np
import re
def reverseSeq(arr):
    list_numbers = []
    for integer in arr:
        int_num = integer
        string_num = np.str(integer)
            
        reverse = ''
        inte = 0
        while integer >= 10:
            inte = inte*10 + integer%10
            
            if inte == 0:
                reverse = reverse + '0'
            integer = integer/10
                
        reverse = reverse + np.str(inte*10+integer)    
             
        if re.match(reverse, string_num):
            list_numbers.append(int_num)
            
    return list_numbers

        
def solveSmall():
    file = open('output.txt', 'r+')
    read_data = np.fromfile('C-small-attempt3.in', dtype=int, count=-1, sep=' ')
    length = read_data.shape[0]
    read_data_sqrt = np.zeros_like(read_data, int)
    read_data_sqrt = np.trunc(np.sqrt(read_data))
    
    para = 1
    countr = 1
    
    for index in range(1, length, 2):
        a = np.int(read_data_sqrt[index])
        b = np.int(read_data_sqrt[index+1])
     
        count = np.arange(a, b+1)
            #print a, b
        list_numbers = reverseSeq(count)
        nums = np.array(list_numbers)  
        nums = np.power(nums, 2)
            
        list_sqrt = reverseSeq(nums)
        size = len(list_sqrt)
        size2 = size
        if size == 0:
            size = 0 
        elif size == 1:
            if list_sqrt[0] < read_data[index] or list_sqrt[0] > read_data[index+1]:
                size = 0
        elif list_sqrt[0] < read_data[index] or list_sqrt[size2-1] > read_data[index+1]:
            size = size - 1
        elif list_sqrt[0] < read_data[index] and list_sqrt[size2-1] > read_data[index+1]:
            size = size - 2
           
        string  = np.str("Case #"+ np.str(countr)+ ": "+ np.str(size)+ "\n")
        file.write(string)
        countr = countr + 1 
        
        
                
if __name__ == '__main__':
    solveSmall()
    