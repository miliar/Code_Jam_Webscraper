__author__ = 'irish'


with open('input_large.txt', 'r') as fin:
    fout = open('output.txt', 'w')
    t = int(fin.readline())
    for i in range(0, t):
        tmp = fin.readline().strip('\n').split(' ')
        smax = int(tmp[0])
        enabled = 0
        cnt = 0
        for j in range(0, len(tmp[1])):
            if enabled < j:
                cnt += (j - enabled)
                enabled = j
            enabled += int(tmp[1][j])
        fout.write("Case #" + str(i+1) + ": " + str(cnt) + "\n")

print("Done.")





