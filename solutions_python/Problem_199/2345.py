
def numFlips(s, n):
    s = list(s)
    count = 0
    if len(s) < n and '-' in s:
        return  "IMPOSSIBLE"
        
    for i in range(len(s)-n+1):
        if s[i] == '-':
            count += 1
            for j in range(n):
                if s[i+j] == '-':
                    s[i+j] = '+'
                elif s[i+j] == '+':
                    s[i+j] = '-'
    if s[-n:] == list('+'*n):
        return str(count)
    elif s[-n:] == list('-'*n):
        return str(count + 1)
    else:
        return "IMPOSSIBLE"


if __name__ == "__main__":
    out = open('out', 'w+')
    with open("A-large.in", 'r') as f:
        for i in range(int(f.readline())):
            line = f.readline()
            pancakes, k = line.split()
            out.write("Case #"+str(i+1)+": "+numFlips(pancakes, int(k)))
            out.write("\n")

    out.close()
            
