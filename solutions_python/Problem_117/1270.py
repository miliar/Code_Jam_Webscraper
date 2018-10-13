# -*- coding: utf-8 -*-
if __name__ == '__main__':
    ifile = open('B-large.in.txt')
    ofile = open('output.txt', 'w')
    N = ifile.readline()
    
    for case in range(int(N)):
        rect = ifile.readline().rstrip().split(' ')
        n = int(rect[0])
        m = int(rect[1])
        
        a = [[0 for j in range(m)] for i in range(n)]
        now_lawn = [[0 for j in range(m)] for i in range(n)]
        
        for line in range(n):
            a[line] = ifile.readline().rstrip().split(' ')
        
        for i in range(n):
            for j in range(m):
                now_lawn[i][j] = 100
        
        ret = "YES"
        
        for i in range(n):
            max_height = 0
            for j in range(m):
                if int(a[i][j]) > max_height:
                    max_height = int(a[i][j])
            for j in range(m):
                now_lawn[i][j] = max_height
                
        for i in range(m):
            max_height = 0
            for j in range(n):
                if int(a[j][i]) > max_height:
                    max_height = int(a[j][i])
            for j in range(n):
                if now_lawn[j][i] > max_height:
                    now_lawn[j][i] = max_height
                    
        for i in range(n):
            for j in range(m):
                if now_lawn[i][j] != int(a[i][j]):
                    ret = "NO"
                    
        print "Case #" + str(case + 1) + ": " + ret
        ofile.write("Case #" + str(case + 1) + ": " + ret + "\n")
        
    ifile.close()
    ofile.close()
