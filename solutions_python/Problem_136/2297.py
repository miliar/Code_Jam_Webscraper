location = 'D:\\Saved Stuff\\'

inp=[]
results=[]
cases=0

with open(location+'cookie.in','r') as f:
    count = 0
    for each in f:
        if count!=0:
            inp.append(each[:-1])
        else:
            cases=int(each)
        count+=1

inpp=[]
for each in inp:
    x=each.split()
    x=[float(i) for i in x]
    inpp.append(x)

def cookiesolve(case):
    c = case[0]
    f = case[1]
    x = case[2]
    rate = 2.0
    seconds = 0
    while x/rate > ((c/rate)+((x/(rate+f)))):
        seconds += c/rate
        rate += f
    seconds += x/rate
    return seconds
    

for each in inpp:
    result = cookiesolve(each)
    result = 'Case #'+str(inpp.index(each)+1)+': '+str(result)
    results.append(result)


with open(location+'cookie.out','w') as f:
    for each in results:
        f.write(each+'\n')
                   





    
