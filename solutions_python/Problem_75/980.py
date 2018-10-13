import os
import copy

def next_num(path=os.path.expanduser("~")+"/Desktop/codeJam/"):
    fin=open(path+"B-large.in", "r")
    fout = open(path+"out1.txt", "w")

    test_cases_count = fin.readline().strip()
#    print "No of test characters == %s" % test_cases_count
    

    for i in range(int(test_cases_count)):
        
         case_string = fin.readline().strip().split(" ")
         c= int(case_string.pop(0))
         s1= case_string[:c]
         
         s1_list = {}
         if c != 0:
             
             for j in range(len(s1)):
                 tmp = s1[j][:2]
                 s1_list[tmp]= s1[j][2]
                 tmp = tmp[::-1]
                 s1_list[tmp] = s1[j][2]


         d= int(case_string.pop(c))
         tmp = case_string[c:c+d]
         
         s2 = []
         s2_list = {}

         if d != 0:
             for j in range(len(tmp)):
                 tmp1 = tmp[j][0]
                 tmp2 = tmp[j][1]
                 s2.append(tmp1+tmp2)
                 s2.append(tmp2+tmp1)
                 if tmp1 in s2_list.keys():
                     s2_list[tmp1].append(tmp2)
                 else:
                     s2_list[tmp1] = list(tmp2)
                 if tmp2 in s2_list.keys():
                     s2_list[tmp2].append(tmp1)
                 else:
                     s2_list[tmp2] = list(tmp1)

         n = int(case_string.pop(c+d))
         s3= case_string[c+d:][0]
         elist = []
#         print "text is %s" %s3
         prev = s3[0]
         for j in range(0, n):
             tmp2 = s3[j]
             if j == 0:
                 elist.append(tmp2)
             else:
                 if len(elist):
                     prev = elist[-1]
                 else:
                     prev = ''
                 tmp = prev + tmp2
                 if tmp in s1_list.keys():
                     tmp1 = s1_list[tmp]
                     del elist[-1]
#                     elist.pop(-1)
                     elist.append(tmp1)
#                     print "INSIDE 1"
                 elif tmp in s2:
                     del elist[:]
#                     elist.pop(-1)
#                     print "INSIDE 2"
                 elif tmp2 in s2_list.keys():
                     tmp1 = s2_list[tmp2]
                     for z in tmp1:
                         if z in elist:
#                          elist.reverse()
#                          ind = elist.index(tmp1) + 1
#                          elist.reverse()
#                          ind = -ind
                             del elist[:]
                             break
                     else:
                         elist.append(tmp2)
#                     print "INSIDE 3"
                 else:
                     elist.append(tmp2)
#                     print "INSIDE 4"
#             print "Iteration $%s: %s" %(str(j+1), str(elist))
         tmp = ''
         tmp = tmp.join(str(elist).split("'"))
#         print "Case #%s: %s" %(str(i+1), str(tmp))
         fout.write("Case #" + str(i+1) + ": " + str(tmp) +"\n" )
             
#          N = (int(case_string.pop(0)) * 2)
#          ostart =1
#          bstart = 1
#          tmp = 0
#          time = 0
#          prev = 0
#          last = case_string[0]

#          for j in range(0, N, 2):
#              if case_string[j] == 'O':
#                  tmp = abs(int(case_string[j+1]) - ostart) 
#                  ostart = int(case_string[j+1])
#                  if last == 'O':
#                      time = time + tmp + 1
#                      prev = prev + tmp + 1
#                  else:
#                      if tmp > prev:
#                          time = time + (tmp-prev) + 1
#                          prev = (tmp-prev) + 1
#                      else:
#                          time = time + 1
#                          prev = 1
#                      last = 'O'
#              else:
#                  tmp = abs(int(case_string[j+1]) - bstart)
#                  bstart = int(case_string[j+1])
#                  if last == 'B':
#                      time = time + tmp + 1
#                      prev = prev + tmp + 1
#                  else:
#                      if tmp > prev:
#                          time = time + (tmp-prev) + 1
#                          prev = (tmp-prev) + 1
#                      else:
#                          time = time + 1
#                          prev = 1
#                      last = 'B'
# #         print "Case #%s: %s" %(str(i+1), str(time))
#          fout.write("Case #" + str(i+1) + ": " + str(time) +"\n" )

    fout.close()
    fin.close()
    

next_num()
