
input1=2
lst1=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

input2=2
lst2=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]


ref_list1=lst1[input1-1]
ref_list2=lst2[input2-1]

count=0
outp=[]
for x in ref_list1:
    if x in ref_list2:
        outp.append(x)
        count+=1
        
if(count==0):
    print 'Volunteer Cheated!'
elif(count==1):
    print outp[0]

elif(count>=2):
    print "Bad Magician!"
    
 
