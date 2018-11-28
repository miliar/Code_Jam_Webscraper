import math;
file = open("input.in", "r");
def raw_input():
    return file.readline();
out = "";


for k in range(int(raw_input())):

    stalls_n, people = [int(i) for i in raw_input().split(" ")];
    stalls_n = [stalls_n];

    for i in range(people):
        
        index = stalls_n.index(max(stalls_n));
        n = stalls_n[index];

        if n%2:
            stalls_n[index] = n/2;
            stalls_n.insert(index, n/2);
        else:
            stalls_n[index] = n/2-1;
            stalls_n.insert(index, n/2);

        o = str(max(stalls_n[index], stalls_n[index+1])), str(min(stalls_n[index], stalls_n[index+1]))

    print stalls_n
    out = out + "Case #"+str(k+1)+": "+" ".join(o)+"\n";
    
open("outputx.in", "w").write(out[:-1]);

