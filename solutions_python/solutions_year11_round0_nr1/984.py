import os
import copy

def next_num(path=os.path.expanduser("~")+"/Desktop/codeJam/"):
    fin=open(path+"A-large.in", "r")
    fout = open(path+"out1.txt", "w")

    test_cases_count = fin.readline().strip()
#    print "No of test characters == %s" % test_cases_count


    for i in range(int(test_cases_count)):
        
         case_string = fin.readline().strip().split(" ")
         N = (int(case_string.pop(0)) * 2)
         ostart =1
         bstart = 1
         tmp = 0
         time = 0
         prev = 0
         last = case_string[0]

         for j in range(0, N, 2):
             if case_string[j] == 'O':
                 tmp = abs(int(case_string[j+1]) - ostart) 
                 ostart = int(case_string[j+1])
                 if last == 'O':
                     time = time + tmp + 1
                     prev = prev + tmp + 1
                 else:
                     if tmp > prev:
                         time = time + (tmp-prev) + 1
                         prev = (tmp-prev) + 1
                     else:
                         time = time + 1
                         prev = 1
                     last = 'O'
             else:
                 tmp = abs(int(case_string[j+1]) - bstart)
                 bstart = int(case_string[j+1])
                 if last == 'B':
                     time = time + tmp + 1
                     prev = prev + tmp + 1
                 else:
                     if tmp > prev:
                         time = time + (tmp-prev) + 1
                         prev = (tmp-prev) + 1
                     else:
                         time = time + 1
                         prev = 1
                     last = 'B'
#         print "Case #%s: %s" %(str(i+1), str(time))
         fout.write("Case #" + str(i+1) + ": " + str(time) +"\n" )

    fout.close()
    fin.close()
    

next_num()
