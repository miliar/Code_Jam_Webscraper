def eval_mag(first,list1,second,list2):
    a= list1[first-1]
    b= list2[second-1]
    c=set(a)&set(b)
    if(len(c)==1):
        return list(c)[0]
    elif(len(c)==0):
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

if __name__=="__main__":
    fo=open("A-small-attempt2.in","r")
    number=int(fo.readline())
    myfile=open("1.txt","w")
    for i in range(number):
        list1=[]
        list2=[]
        first=int(fo.readline())
        for j in range(4):
            string= fo.readline().rstrip('\n')
            string=map(int,string.split())
            list1.append(string)
        second =int(fo.readline())
        for k in range(4):
            string= fo.readline().rstrip('\n')
            string=map(int,string.split())
            list2.append(string)
        #print list1,list2
        myfile.write("Case #"+str(i+1)+": "+str(eval_mag(first,list1,second,list2))+"\n")
    myfile.close()
