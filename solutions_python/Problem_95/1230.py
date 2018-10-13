#!/usr/bin/env python
import sys

def googlease(filename1,output_name1):
    string1="ejp mysljylc kd kxveddknmc re jsicpdrysi"
    string2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
    string3="de kr kd eoya kw aej tysr re ujdr lkgc jv"
    
    newstr1="our language is impossible to understand"
    newstr2="there are twenty six factorial possibilities"
    newstr3="so it is okay if you want to just give up"
    
    dic1={}
    dic1['y']='a'
    dic1['e']='o'
    dic1['q']='z'
    string4=string1+string2+string3
    newstr4=newstr1+newstr2+newstr3
    for i in range(len(string4)):
        if string4[i] in dic1:
            pass
        else:
            dic1[string4[i]]=newstr4[i]
    print dic1
    
    string_total='abcdefghijklmnopqrstuvwxyz'
    for f in string_total:
        if f not in dic1.values():
            print f
    dic1['z']='q'
    
    file1=open(filename1,'r')
    lines=file1.readlines()
    
    file2=open(output_name1,'w')
    length=len(lines)
    total=int(lines[0].strip("\r\n"))
    index=1
    for i in range(total):
        string5=lines[index].strip("\r\n")
        length_string=len(string5)
        
        list1=[]
        for j in range(length_string):
            list1.append(dic1[string5[j]])
        newstr5="".join(list1)
        file2.write("Case #%s: %s\n" %(i+1,newstr5))
        index+=1
    
if __name__=="__main__":
    googlease(sys.argv[1],sys.argv[2])
