import re

def main():
    words = []
    f = open(r'A-large.in', 'r')
    g = open(r'A-large.out', 'w')
    data = f.readline().split()
    for i in range(0,int(data[1])):
        words.append(f.readline()[:-1])
    for j in range (0,int(data[2])):
        restr = (f.readline())[:-1]
        restr = restr.replace('(','[')
        restr = restr.replace(')',']')
        c = 0
        for word in words:
            if re.match(restr, word):
                c += 1
        ans = "Case #" + str(j+1) + ": " + str(c) + "\n"
        print ans,
        g.write(ans)
    g.close()
    f.close()
    pass

if __name__=="__main__": main()
