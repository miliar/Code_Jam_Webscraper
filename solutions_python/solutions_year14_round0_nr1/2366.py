location = 'D:\\Saved Stuff\\'

inp=[]
inpp=[]
badresult='Bad Magician!'
noresult='Volunteer cheated!'
cases=0

with open(location+'magic.in','r') as f:
    count = 0
    for each in f:
        if count!=0:
            inp.append(each[:-1])
        else:
            cases=int(each)
        count+=1

for each in inp:
    if len(each)>1:
        inpp.append(each.split())
    else: inpp.append(each)
        
results=[]

#creates case dictionaries of a ten row set
def caser(data):
    case = {}
    case[1]=data[0]
    case[2]=data[5]
    case['1']=data[1:5]
    case['2']=data[6:]
    return case

#takes a case and decides if it is possible
def solver(case):
    possible=[]
    firstrow=case['1'][int(case[1])-1]
    secondrow=case['2'][int(case[2])-1]
    for each in firstrow:
        if each in secondrow:
            possible.append(each)
    if len(possible)==0:
        return noresult
    if len(possible)>1:
        return badresult
    return possible[0]

for each in range(0,cases):
    case = inpp[each*10:(each+1)*10]
    case = caser(case)
    result = solver(case)
    results.append('Case #'+str(each+1)+': '+result)

with open(location+'magic.out','w') as f:
    for each in results:
        f.write(each+'\n')
                   





    
