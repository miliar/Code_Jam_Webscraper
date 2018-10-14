cases = []

with open('B-large.in','r') as infile:
    for row in infile:
        cases.append(row.strip())

cases = cases[1:]

def check_inc(st,ed,num):
    if st == ed:
        return True
    if ed-st == 1:
        return num[st] <= num[ed]
    mid = st + (ed - st) / 2
    if num[mid] < num[st] or num[mid] > num[ed]:
        return False
    return check_inc(mid,ed,num) and check_inc(st,mid,num)

def get_next(n):

    '''
    :param number:
    :return: string
    start from first char
    '''
    if n[-1] == '0':
        return str(int(n)-1)

    num = list(n)
    num.reverse()
    N = len(num)-1
    for i in range(len(num)):
        if i < len(num)-1 and num[i] < num[i+1]:
            num[i+1] = str(int(num[i+1])-1)
            for j in range(i+1):
                num[j] = '9'
            break

    return "".join(num[::-1])

def rem(n):
    i = 0
    while n[i] == '0':
        i += 1
    return n[i:]

ans = []
test = []
for i,case in enumerate(cases):
    test.append(case)
    print 's',case
    while not check_inc(0,len(case)-1,case):
        print case
        case = get_next(case)
    print 'e', case
    ans.append('Case #'+str(i+1)+': '+rem(case))


with open('B-large.out','w') as outfile:
    for row in ans:
        outfile.write(row+'\n')

with open('infile4.txt','w') as outfile:
    for row,roww in zip(test,ans):
        outfile.write(row+' '+roww+'\n')
