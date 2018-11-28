def prefill():
    N = 1000
    with open('b_ans.txt','w') as f:
        for i in range(N):
            x = i + 1
            a = get_rev_num(x)
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

validate()
#prefill()