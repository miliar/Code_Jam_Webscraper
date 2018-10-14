import string
def sort_list(list0):
    count=0
    list1=[0]
    list1=list1+list0
    for i in  range(1,len(list1)):
        if list1[i]!=i:
            index_array=[i]
            index1=list1.index(i)
            index_array.append(index1)
            while index1!=list1[i]:
                index1=list1.index(index1)
                index_array.append(index1)
            for j in index_array:
                list1[j]=j
            count+=len(index_array)               
    return count
fin=open("D-large.in",'r')
out=open("output1.txt","w")
x=fin.readline()
T = int(x)
out.write(x)
result=[]
outfile=open("output.txt","w")
for case in range(1,T+1):
    out.write("#"+str(case)+"\n")
    number=fin.readline()
    out.write(number)
    line0 = fin.readline()
    out.write(line0)
    numbers=[int(x) for x in line0.split()]
    f_str=sort_list(numbers)
    f_str=str(f_str)+".000000"
    f_str="Case #%d: %s \n" % (case,f_str)
    outfile.write(f_str)
outfile.close()
out.close()  
print "done" 
