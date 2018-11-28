def run():
    t = int(raw_input());
    op = [];
    for i in range(t):
        ln = raw_input().split(' ');
        a = int(ln[0]);
        b = int(ln[1]);
        c = int(ln[2]);
        ct = 0;
        for j in range(a):
            for k in range(b):
                if((j & k) < c):
                    ct += 1;
        op.append("Case #" + str(i+1) + ": " + str(ct));
    f = open("C:\\b.txt",'w');
    for x in op:
        f.write(x + "\n");
    f.close();

run()
