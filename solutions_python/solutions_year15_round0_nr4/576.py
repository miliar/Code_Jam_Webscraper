'''
Created on Apr 11, 2015

@author: lroot
'''

if __name__ == '__main__':
    input_fname = "../q4.txt"
    output_fname = "../a4.txt"
    content = []
    with open(input_fname) as inf:
        content = inf.readlines()
    outf = open(output_fname, 'w')
    
    i = 0  
    for idx, line in enumerate(content):
        result =''
        if idx == 0:
            continue
        else:
            data = line.strip().split(" ")
            nums = [int(num) for num in (data)]
#             print nums
            size = nums[1]*nums[2]
            if size % nums[0] == 0 and nums[0] <= max(nums[1:3]) and nums[0]-1 <= min(nums[1:3]):
                print nums[1:3]
                print nums
                result = 'GABRIEL'
            else:
                result = 'RICHARD'
                
            outf.write("Case #"+str(idx)+": " + str(result)+'\n')       
#             sum_audience = 0
#             index = 0
#             new_audience = 0
#             for num in (nums):
# #                 print num
# #                 print str(index) + " "+ str(num) +" "+str(sum_audience)
#                 audience = sum_audience - index
# #                 print audience
#                 if audience < 0 :
#                     new_audience = new_audience + abs(audience)
#                     sum_audience = sum_audience + abs(audience)
#                 sum_audience = sum_audience + num
#                 index = index + 1
# #             Case #1: 0
#             outf.write("Case #"+str(idx)+": " + str(new_audience)+'\n')
            
#                 print idx