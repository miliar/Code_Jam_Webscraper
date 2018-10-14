'''
Created on Apr 11, 2015

@author: lroot
'''


import math

def multiply(x,y):
    if x == '1':
        if y == '1':
            return ['1', 1]
        elif y == 'i':
            return ['i', 1]
        elif y == 'j':
            return ['j', 1]
        elif y == 'k':
            return ['k', 1]
    elif x == 'i':
        if y == '1':
            return ['i', 1]
        elif y == 'i':
            return ['1', -1]
        elif y == 'j':
            return ['k', 1]
        elif y == 'k':
            return ['j', -1]
    elif x == 'j':
        if y == '1':
            return ['j', 1]
        elif y == 'i':
            return ['k', -1]
        elif y == 'j':
            return ['1', -1]
        elif y == 'k':
            return ['i', 1]
    elif x == 'k':
        if y == '1':
            return ['k', 1]
        elif y == 'i':
            return ['j', 1]
        elif y == 'j':
            return ['i', -1]
        elif y == 'k':
            return ['1', -1]
       

if __name__ == '__main__':
    input_fname = "../q3.txt"
    output_fname = "../a3.txt"
    content = []
    with open(input_fname) as inf:
        content = inf.readlines()
    outf = open(output_fname, 'w')
    
    i = 0  
    for idx, line in enumerate(content):
        if idx == 0:
            continue
        elif idx%2 == 0:
            print content[idx-1]
            print line
            data = content[idx-1].split(" ")
            index = 0
            pos = 0
            exchr = '1'
            expos = 1
            while (index < int(data[1].strip())):
                for chr in line.strip():
                    
                    print exchr + " "+chr
                    result = multiply(exchr,chr)
                    exchr = result[0]
                    expos = expos*result[1]
                    if exchr == 'i' and expos == 1 and pos == 0:
                        exchr = '1'
                        expos = 1
                        pos = 1
                    elif exchr == 'j' and expos == 1 and pos == 1:
                        exchr = '1'
                        expos = 1
                        pos = 2
                    elif exchr == 'k' and expos == 1 and pos == 2:
                        exchr = '1'
                        expos = 1
                        pos = 3
                index = index + 1
                
            if exchr == '1' and expos == 1 and pos == 3:
                returnvalue = 'YES'
            else:
                returnvalue = 'NO'
            outf.write("Case #"+str(idx/2)+": " +returnvalue+'\n')
#             nums = [int(num.strip()) for num in (data)]
#             sum_num = sum(nums)
#             
#             plates = (math.floor(math.sqrt(sum_num)))
#             print plates
#             min_num = (math.ceil(sum_num/plates))
#             print min_num
#             min_minutes = 0
#             max_num = 0
# #             sum_audience = 0
# #             index = 0
# #             new_audience = 0
#             for num in (nums):
#                 if num > max_num:
#                     max_num = num
#                 if num > min_num:
#                     print str(num)+"  "+str(math.ceil(num/min_num)-1)+"####"
#                     min_minutes = min_minutes+ math.ceil(num/min_num)-1
#             
#             if min_num>max_num:
#                 min_minutes = max_num
#             else:
#                 min_minutes = min_minutes+ min_num
#             if min_minutes> max_num:
#                 min_minutes = max_num
# #                 # Case #1: 0
#             outf.write("Case #"+str(idx/2)+": " + str(int(min_minutes))+'\n')
