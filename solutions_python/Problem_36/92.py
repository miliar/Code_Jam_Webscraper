#!/usr/bin/env python

def main():
    data = [];
    mod_str = "welcome to code jam";
    NUM = 19;
    note = [];
    f = open("C-large.in", "r");
    fout = open("output.out","w");
    n = int(f.readline());
#    print n;

    for i in range(n):
        data = f.readline()[:-1];
        note = [];
        for j in range(data.__len__()):
            note.append([]);
            for k in range(NUM):
                note[j].append(0);
            if data[j] == mod_str[0]:
                note[j][0] = 1;
            for k in range(1,NUM):
                if data[j] == mod_str[k]:
                    for l in range(j-1, -1, -1):
                        if data[l] == mod_str[k-1]:
                            note[j][k] += note[l][k-1];
                            note[j][k] = note[j][k] % 10000;
#            if j == 25:
#                for k in range(NUM):
#                    print note[j][k];
#                    print "---"
        sum = 0;
        for j in range(data.__len__()):
            sum += note[j][NUM - 1];
        sum = sum % 10000;
        if sum >= 1000:
            fout.write("Case #{0}: {1}\n".format(i+1,sum));
        elif sum >= 100:
            fout.write("Case #{0}: 0{1}\n".format(i+1,sum));
        elif sum >= 10:
            fout.write("Case #{0}: 00{1}\n".format(i+1,sum));
        else:
            fout.write("Case #{0}: 000{1}\n".format(i+1,sum));

#    for i in range(n, -1, -1):
#        print i;
#    for i in range(n):
#        print "%s" % data[i];


if __name__ == '__main__':
    main();
