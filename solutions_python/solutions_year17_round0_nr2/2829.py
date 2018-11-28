def digits(n, b = 10):
    if n == 0:
        return []
    else:
        return digits(n//b, b) + [n%b]

def is_tidy(n):
    ds = digits(n)
    for i in range(len(ds)-1):
        if ds[i] > ds[i+1]:
            return False
    return True

def last_tidy_naive(n):
    while not is_tidy(n):
        n -= 1
    return n

def last_tidy(n):
    if not is_tidy(n):
        ds = digits(n)
        lg = len(ds)
        for i in range(lg-1,0,-1):
            if ds[i] != 9:
                return last_tidy(n-(ds[i]+1)*10**(lg-i-1))
    else:
        return n

i = open("i.in")
o = open("o.out", "w")
for line in range(int(i.readline())):
    to_write = last_tidy(int(i.readline()))
    o.write("Case #" + str(line+1) + ": " + str(to_write) + "\n")
