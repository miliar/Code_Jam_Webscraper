file = open("input.in", "r");
def input():
    return file.readline();

out = '';
for x in range(int(input())):
    dist, n_horses = input().split(" ");
    dist = int(dist);
    horses = [];
    for m in range(int(n_horses)):
        horses.append(input().split(" "));
        horses[-1][0] = int(horses[-1][0]);
        horses[-1][1] = int(horses[-1][1]);
    tim = max([float(dist-horses[i][0])/horses[i][1] for i in range(len(horses)) ]);
    out+="Case #"+str(x+1)+": "+str(dist/tim)+"\n";
open("outputx.in", "w").write(out[:-1]);
