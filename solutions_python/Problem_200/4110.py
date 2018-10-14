def prefill():
    N = 1000
    with open('b_ans.txt','w') as f:
        for i in range(N):
            x = i + 1
            a = int(get_rev_num(x))
            f.write('{}\n'.format(a))

def validate():
    counter = 0
    o = []
    with open('b_small.txt', 'r') as f:
        for data in f:
            data = int(data.strip())
            if counter == 0:
                T = data
                counter += 1
            else:
                a = int(get_rev_num(data))
                #print(a)
                o.append(a)
            
    with open('b_out.txt', 'w') as f:
        for idx, val in enumerate(o):
            f.write('Case #{}: {}\n'.format(idx + 1, val))

def computex():
    counter = 0
    o = []
    with open('b_small.txt', 'r') as f:
        for data in f:
            data = int(data.strip())
            if counter == 0:
                T = data
                counter += 1
            else:
                a = process_rev(data)# int(get_rev_num(data))
                #print(a)
                o.append(a)
            
    with open('b_out.txt', 'w') as f:
        for idx, val in enumerate(o):
            f.write('Case #{}: {}\n'.format(idx + 1, val))
            
def process_rev(n):
    n_s = str(n)
    x = []
    is_rev = False
    if len(n_s) == 1:
        x = str(n)
    for i in range(len(n_s) - 1):
        if n_s[i] > n_s[i+1]:
            a = int(n_s[i]) - 1
            if a == -1:
                a = 9
            a = str(a)
            print('1 = {}'.format(a))
            x.append(a)
            is_rev = True
            break
        else:
            x.append(n_s[i])
            if i == len(n_s) - 2:
                x.append(n_s[i+1])
                
    if is_rev:
        f = len(n_s) - len(x)
        for i in range(f):
            x.append('9')
    print(x)
    return int(''.join(x[:]))        
            
def get_rev_num(n):
    ans = n
    n1 = n
    while True:
        if is_rev_ok(n1):
            ans = n1
            break
        else:
            n1 = n1 - 1
    return ans

def is_rev_ok(n):
    n_s = str(n)
    for i in range(len(n_s) - 1):
        if n_s[i] > n_s[i+1]:
            return False
    return True

computex()
#prefill()