f = open('A-large.in')
q = open('output.txt','w')
lines =[]
cases = []

def all_same(L):
  return all(x == L[0] for x in L)

def check(to_check):
    if all_same(to_check) and "." not in to_check:
            return to_check[0]
    elif "T" in to_check:
        temp = [m for m in to_check if m!="T"]
        if len(temp)==3 and all_same(temp) and temp[0]!=".":
            return temp[0]
    return 0

def check_case(case):
    verify3=check(case[0::5])
    if verify3!=0:
        return verify3
    verify4=check(case[3:-1:3])
    if verify4!=0:
        return verify4    
    for k in range(4):
        verify1=check(case[4*k:4*k+4])
        verify2=check(case[k::4])
        if verify1!=0:
            return verify1
        if verify2!=0:
            return verify2
    if "." not in case:
        return 0
    else:
        return 1

for line in f:
    lines.append(line)

amount_of_cases=int(lines[0])
for k in range(amount_of_cases):
    temp = lines[5*k+1][:-1]+lines[5*k+2][:-1]+lines[5*k+3][:-1]+lines[5*k+4][:-1]
    cases.append(temp)
k=1
for case in cases:
    if check_case(case)==0:
        q.write("Case #"+str(k)+": Draw\n")
    elif check_case(case)==1:
        q.write("Case #"+str(k)+": Game has not completed\n")
    else:
        q.write("Case #"+str(k)+": "+str(check_case(case))+" won\n")
    k+=1
q.close()
