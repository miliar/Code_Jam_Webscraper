

def tidy_num(n):
    n = n[:-1]
    length = len(n)
    s = list(n)
    first_i = 0
    i= 0
    while i < length-1:
        if ord(s[i]) > ord(s[i+1]):
            break
        i += 1
        if s[first_i] != s[i]:
            first_i = i

    if i == length-1:
        return n
    
    if s[i] == '1':
        return '9'*(length-1)

    else:
        to_add = chr(ord(s[i])-1)
        n = n[:first_i]+to_add
        while len(n) != length:
            n = n+'9'
        return n

if __name__ == "__main__":
    out = open("out", "w+")
    with open("B-large.in", "r") as f:
        for i in range(int(f.readline())):
            out.write("Case #{0}: {1}\n".format(i+1, tidy_num(f.readline())))
    out.close()
            
