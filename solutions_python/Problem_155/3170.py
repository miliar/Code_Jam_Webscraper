#input 110011
#      012345

infile = open("A-large.in","r")
rawdata = infile.readlines()
infile.close()
l = []
for line in rawdata:
    a = line.split()
    l.append(a)

l = l[1:]
temp = []
for i in l:
    temp2 = []
    for num in i[1]:
        temp2.append(int(num))
    temp.append(temp2)

def backward_num(temp:list)->list:
    i = len(temp)-1
    newlist = []
    while i > 0:
        newlist.append(i)
        i = i - 1
    return newlist

test = [0,1,2]

def check_from_back(case:list)->int:
    friend = 0
    for shyness in backward_num(case):
        standing = sum(case[:shyness])+friend
        if standing < shyness:
            friend += (shyness-standing)
    return friend


result = []
for case in temp:
    result.append(check_from_back(case))

outfile = open('audience2.txt','w')
for i in range(len(result)):
    outfile.write("Case #{}: {}\n".format(i+1,result[i]))
outfile.close()
