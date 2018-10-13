filename = "A-large.in"
rows = [i.strip() for i in file(filename).readlines()][1::]
i = 1


def calc1(s,k,step):
    curr_s = s
    while (True):
        s = s.strip('+')
        if (len(s) == 0):
            return str(step)
        
        if (len(s) < k):
            return 'IMPOSSIBLE'
        #where 
        if (s[:k:].count("-") > s[-k:0:].count("-")):
            to_flip = s[:k:]
            s = s[k::]
            to_flip = to_flip.replace("+", "a").replace("-", "+").replace("a", "-")
            s = to_flip + s
            step += 1
        else:
            to_flip = s[-k:0:]
            s = s[:-k:]
            s = s + to_flip
            step += 1


with open("out_small2.out", "w+") as outf:
    for row in rows:
        s,k = row.split(' ')
        k = int(k)
        write_str = "Case #" + str(i) + ": " + str(calc1(s,k,0)) + "\n"
        print write_str
        outf.write(write_str)
        i += 1
