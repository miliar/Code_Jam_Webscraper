A=100
B=500


def getn(n):
    k = 0
    while(n > 0):
        k = k + 1
        n = n / 10
    return k

def left(n, num):
    num_t = getn(n)
    if num_t < num:
        return (10 * n)
    else:
        high = n / pow(10, num_t - 1)
        n = n - high * pow(10, num_t - 1)
        return ((n * 10) + high)

def cycle(n, B):
    num = getn(n)

    if(num == 1):
        return 0
        
    count = 0
    high = n / pow(10, num - 1)
    n = n - high * pow(10, num - 1)
    num = num - 1
    print(high)

    rec = high
    i = 1
    while num > 0:
        temp = n / pow(10, num - 1)

        if temp > high:
            if((n * pow(10, i) + rec) <= B):
                count = count + 1
        rec = 10 * rec + temp
        
        n = n - temp * pow(10, num - 1)
        num = num - 1
        i = i + 1
    return count

def cycle_bk(n, B):
    num = getn(n)
    true = num
    if(num == 1):
        return 0
    old=[]
    count = 0
    num = num - 1
    ini = n
    while num > 0:
        temp = left(n, true)
        if((temp <= B) and (temp not in old)):
            if temp > ini:
                count = count + 1
                #print(str(ini) + " " + str(temp))
                old.append(temp)
        num = num - 1
        n = temp
    return count

def cycle_2(A, B):
    n = A
    num = 0
    i = 0
    while(n < B):
        num = num + cycle_bk(n, B)
        #print(str(n) + ":" + str(cycle_bk(n, B)))
        n = n + 1
        i = i + 1
    return num

source = open('input.in')
source_str = source.read()
source_list = source_str.split('\n')
source.close()

input_num = int(source_list[0])
source_list = source_list[1 : len(source_list) - 1]

f = open('A-small.out', 'w')
line = 1
for node in source_list:
    data = node.split(' ')
    A = int(data[0])
    B = int(data[1])
    l = cycle_2(A, B)
    f.write("Case #" + str(line) + ": " + str(l) + '\n')
    line = line + 1
f.close()   


    
