'''
def Calc_Tidy(n):
    for i in range(n, 1, -1):
        Sort_Num = int(''.join(sorted(list(str(i)))))
        if Sort_Num == i: return(Sort_Num)
'''

in_file = 'B-large.in'
Type = 'large'
out_file = 'B-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

Tt = int(data[0])
del data[0]

def Calc_Tidy_Quick(n):
    if n < 9: return(n)
    Sort_Num = [int(j) for j in list(str(n))]
    if Sort_Num == sorted(Sort_Num): return(n)
    # Find the first decrease
    Test = int(''.join(str(i) for i in Sort_Num))-1
    Test = [int(j) for j in list(str(n))]
    while Test != sorted(Test):
        Found = False
        for el in range(1, len(Sort_Num)):
            if Found:
                Sort_Num[el] = 0
                continue
            if Sort_Num[el] < Sort_Num[el - 1]:
                Sort_Num[el] = 0
                Found = True
        Test = int(''.join(str(i) for i in Sort_Num))-1
        Sort_Num = [int(j) for j in list(str(Test))]
        Test = [int(j) for j in list(str(Test))]
        #print(n, Test, Sort_Num)
    return(int(''.join(str(i) for i in Test)))

OUT = []
for k in range(Tt):
    OUT.append(Calc_Tidy_Quick(int(data[k])))

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i])) 
