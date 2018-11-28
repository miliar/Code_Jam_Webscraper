'''
Created on 2010-05-07

@author: lawford
'''

if __name__ == '__main__':
    f = open("/raid/downloads/firefox/A-large.in", "r")
    lines = f.readlines()
    i=1
    fout = open("/tmp/A-large.out", "w")
    for line in lines:
        cols = line.split()
        if len(cols) > 1:
            mod = (int(cols[1])+1)%(2**(int(cols[0])))
            if mod == 0:
                fout.write("Case #"+str(i)+": ON\n")
            else:
                fout.write("Case #"+str(i)+": OFF\n")
            i = i+1
    fout.close()
    f.close()
