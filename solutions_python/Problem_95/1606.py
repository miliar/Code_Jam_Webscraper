import os
import copy

from string import maketrans

def tongues(path=os.path.expanduser("~")+"/"+"/gcj/"):
    fin=open(path+"A-small-attempt0.in", "r")
    fout = open(path+"out.txt", "w")

    test_cases_count = fin.readline().strip()
    print "No of test characters == %s" % test_cases_count

    intab = "abcdefghijklmnopqrstuvwxyz"
    outtab = "yhesocvxduiglbkrztnwjpfmaq"
    transtab = maketrans(intab, outtab)

    for i in range(int(test_cases_count)):
        
         case_string = fin.readline().strip()
         new_str = case_string.translate(transtab)
#         print "Case #"+ str(i+1) +": "+ new_str


         fout.write("Case #" + str(i+1) + ": " + new_str +"\n" )
    fout.close()
    fin.close()
    

tongues()
