file = open("input.in", "r");
def raw_input():
    return file.readline();

def cut(n):
    n = list(n)[:-1];
    for i in range(len(n)-1):
        i = len(n) - i - 1;
        if int(n[i])<int(n[i-1]):
            n[i-1] = str(int(n[i-1])-1);
            n[i:] = ["9"]*(len(n)-i) 
    return str(int("".join(n)));

times = int(raw_input());

out = '';

for k in range(times):
    i = raw_input();
    out = out + "Case #"+str(k+1)+": "+cut(i)+"\n";
    
open("outputx.in", "w").write(out[:-1]);
