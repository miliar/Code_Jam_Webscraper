from queue import Queue
def load_file(filename):
    f = open(filename, "r")
    n = int(f.readline()[:-1])
    cases = [row.replace('\n','').split(" ") for row in f.readlines()]
    return n, cases


n, cases = load_file("sample.txt")

def copy(a):
    n = [0]*len(a)
    for i in range(len(a)):
        n[i] = a[i]
    return n

def str_(a):
    s = ""
    for i in a:
        s += i
    return s

def search(s, k):
    fathers = dict()
    q = Queue()
    q.put(s)
    fathers[s] = s
    visited = set()
    visited.add(s)
    while(not(q.empty())):

        a = q.get()
        if not('-' in a):
            #target
            count = 0
            f = fathers[a] 
            while(f != a):
                count += 1
                a = f 
                f = fathers[a]
            return count
        t_a = list(a)
        for i in range(len(t_a) - k + 1):
            new_a = copy(a)
            for j in range(i, i+ k):
                if new_a[j] == '+':
                    new_a[j] = '-'
                else:
                    new_a[j] = '+'
            x = str_(new_a)
            if not(x in visited):
                visited.add(x)
                fathers[x] = a
                q.put(x)
    return "IMPOSSIBLE"
            

    

f = open("faccette.txt", "w")
i = 1
for case in cases:
    s = case[0]
    k = int(case[1])
    f.write("Case #{}: {}\n".format(i, search(s, k)))
    i += 1
f.close()
