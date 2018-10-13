f = open ('A-large.in', 'r');

def getNum():
    n = int(f.readline());
    return n;

def getLine():
    s = f.readline();
    return s[:-1];

def getLines(splitter=" "):
    l = f.readline()[:-1];
    l = l.split(splitter);
    return l;

def getNums(splitter=" "):
    l = f.readline()[:-1];
    l = l.split(splitter);
    l = list(map(int, l));
    return l;
##new code below this line





def main():
    
    dist, n = getNums();
    
    slowest = 0;
    for horse in range(1, n+1):
        start, speed = getNums();
        rem = dist - start;
        time = rem/speed;
        slowest = max(slowest, time)
    
    result = dist/slowest;
    
    #print(result)
    return result;

##newcode above this line

output = "";
cases = getNum();
for case in range(1, cases+1):
    output += "Case #" + str(case) + ": ";
    output += str(main());
    output += "\n";

with open('A-large.out', 'w') as o:
    o.write(output)
