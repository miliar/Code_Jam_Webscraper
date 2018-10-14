## Written by Nivvedan S
## Google Codejam

def divide(g):
    if len(g)==1:
        return [[[g[0]],[]],[[],[g[0]]]]
    else:
        sub_div=divide(g[0:len(g)-1])
        res=[]
        for item in sub_div:
            temp=item[0][:]
            temp.append(g[-1])
            res.append([temp,item[1]])
            temp=item[1][:]
            temp.append(g[-1])
            res.append([item[0],temp])

        return res

def sum_a_list(lst):
    s=0
    for i in lst:
        s=s+i
    return s

def xor_a_list(lst):
    s=0
    for i in lst:
        s=s^i
    return s

def filter_the_list(lst):
    res=[]
    for item in lst:
        if not (item[1]==[]):    
            if (sum_a_list(item[0])>=sum_a_list(item[1])):
                res.append(item)
    return res
        
INPUT_FILE_NAME="c.in"
## OUTPUT_FILE_NAME="c.out"
IN = open(INPUT_FILE_NAME, "r")
## OUT = open(OUTPUT_FILE_NAME, "w")

par_input=IN.readlines()

T=int(par_input[0].strip())

count=0
while (count<T):
    par_input=par_input[2:]
    line=par_input[0]
    to_parse=line.strip().split()

    values=[]
    for item in to_parse:
        values.append(int(item))
    
    values=filter_the_list(divide(values))

    max_val=0

    for item in values:
        if (xor_a_list(item[0])==xor_a_list(item[1])):
            temp=sum_a_list(item[0])
            if (temp>max_val):
                max_val=temp

    if max_val==0:
        max_val="NO"
    else:
        max_val=str(max_val)

    count=count+1
    output="Case #"+str(count)+": "+max_val
    print output


    
