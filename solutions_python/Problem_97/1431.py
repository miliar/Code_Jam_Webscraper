fptr = open('C-small-attempt0.in','r')
fptr2=open('q3_ans.txt','w')

test_cases=int(fptr.readline())
line_no=1

for line in fptr:
    count=0
    nums=line.split()
    length = len(nums[0])
    A=int(nums[0])
    B=int(nums[1])
    n=A
    if length>1:
        for n in range(A,B):
            temp=str(n)
            for i in range(1,length):
                temp2 = int(temp[i:]+temp[:i])
                if str(temp2)[0]=='0':
                    continue
                if str(temp2)==temp:
                    print temp,temp2
                    break
                if temp2<=B and temp2>n:
                    count+=1
                    
    case="Case #"+str(line_no)+": "+str(count)
    if line_no!=test_cases:
        case = case+"\n"
    fptr2.write(case)
    line_no+=1

fptr.close()
fptr2.close()
