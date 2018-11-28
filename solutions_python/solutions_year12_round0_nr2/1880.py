'''
Created on 14 Apr 2012

@author: benoit
'''

def isValidableWithoutException(note,limit):
    limit_total = limit + (max(limit-1,0))*2
    return (limit_total <= note)
    
def isValidableWithException(note,Limit):
    limit_total = limit + (max(0,limit-2))*2
    return (limit_total <= note)   

if __name__ == '__main__':
    f= open(r'C:/google/input.txt', 'r')
    number_case = int(f.readline())
    
    g = open(r'C:/google/output.txt', 'w')
    for i in range(int(number_case)):
        data = f.readline().split(' ')
        googlers = int(data[0])
        surprising_results = int(data[1])
        limit = int(data[2])
        notes = data[3:]
        
        ok_total_with_exception = 0 
        ok_total_without_exception = 0
        
        for note in notes:
            int_note = int(note)
            if isValidableWithoutException(int_note,limit):
                ok_total_without_exception = ok_total_without_exception +1
            elif isValidableWithException(int_note,limit):
                ok_total_with_exception = ok_total_with_exception +1
        nb_max = ok_total_without_exception + min(ok_total_with_exception, surprising_results)
          
        
        result = "Case #" + str(i+1) + ": " + str(nb_max) + "\n"
        g.write(result)
        
        
        

    