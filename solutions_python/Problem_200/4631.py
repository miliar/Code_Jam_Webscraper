import sys
import numpy as np


def tidy_number(input):
        
    list_input=np.array(list(input), dtype='int')
    num_input=np.int64(input)

    while np.any(np.sort(list_input) != list_input):
        num_input-=1
        list_input =np.array(list(str(num_input))) 

    else:
        return num_input    
        
#        for j in np.arange(1, len(list_input)-1):
#            if (list_input[j] > list_input[-1]):
                #if (list_input[j-1] > list_input[j]):   
#                num_input-=1
#                list_input =list(str(num_input))
#                break
#             elif list_input[j] > list_input[j+1]:
#                num_input-=1
#                list_input =list(str(num_input))
#                break
    
    

def main():

    args= sys.argv[1:]
    file=args[0]
    f=open(file, 'rU')
    data=f.read().splitlines()

    file_pre_i=file.find('.in')
    file_pre=file[:file_pre_i]
    fw = open(file_pre+'.out', 'w')

    numcases = int(data[0])

    for i in xrange(numcases):
        
        input = (data[i+1].strip())
        output = tidy_number(input)
        fw.write( 'Case #%i: %i \n' % ( i+1, output) )
    
    fw.close()

if __name__ == '__main__':
    main()
