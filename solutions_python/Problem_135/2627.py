#! /usr/bin/env python
import sys

# parsing input for a case

def read_line_int(f):
    line = f.readline()
    arr = line.split()
    t = [int(i) for i in arr]
    return t

     
# to have a nice name
def getfilename():
    args = sys.argv
    n = len(args)
    if n>1:
        return args[1]

# common element of two rows
def common_element_row(r1,r2):
    arr = [x for x in r1 if x in r2]
    #print(arr)
    l = len(arr)
    #print l
    #return arr
    if l > 1 :
        res="Bad magician!"    
    elif l == 0 :
        res="Volunteer cheated!"    
    else: 
        res="%d" % (arr[0])
    return res

def common_element(r1,r2,i):
    res = common_element_row(r1,r2)
    s = "Case #%d: %s" % (i+1,res)
    #s = "Case #%d" % (i+1)
    #print (res)
    return s

# main program for a case
def caseprocess(f,i):
    #1st answer
    ans1 = read_line_int(f)[0]
    #print("1st answer is: %d\n")%(ans1) 
    #1st arrangement
    arr1 = [read_line_int(f) for j in range(4)]
    #print("arrangement 1\n")
    #print(arr1)
    ans_arr1 = arr1 [ans1-1]
    #print("1st selected row\n")
    #print(ans_arr1)

    #2nd answer
    ans2 = read_line_int(f)[0]
    #print("2nd answer is: %d\n")%(ans2) 
    #1st arrangement
    arr2 = [read_line_int(f) for j in range(4)]
    #print("arrangement 2\n")
    #print(arr2)
    #print("2nd selected row\n")
    ans_arr2 = arr2 [ans2-1]
    #print(ans_arr2)
    #return "answer 1: %d\n" % (ans1)
    #res = 0
    #return "Case #%d: %d\n" % (i+1,res)
    return common_element(ans_arr1,ans_arr2,i)

# main
if __name__=='__main__':
    input = getfilename()
    name = input[:-3]
    output = name+".out"
    f = open(input,'r')
    t1 = read_line_int(f)
    T = t1[0]
    #print "nb of cases :%d\n" % T
    o = open(output,'w')
    for i in range(T):
        #print "case number %d processed\n" % i
        oline = caseprocess(f,i)
        print oline
        o.write(oline)
    o.close()
    f.close()


