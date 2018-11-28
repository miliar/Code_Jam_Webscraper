'''
Created on May 22, 2010

@author: hasmeet
'''
r = open('C:/users/hasmeet/desktop/A-large.in', 'r')

w = open('output.txt', 'w')

numCases = int(r.readline())

for i in range(numCases):
    print i
    answer = 'Case #' + str(i+1) + ': '
    line = r.readline().split(' ')
    N = int(line[0])
    M = int(line[1])
    files = {}
    for n in range(N):
        line = r.readline().split('/')
        del line[0]
        if line[len(line)-1][len(line[len(line)-1]) - 1:] == '\n': line[len(line)-1] = line[len(line)-1][:len(line[len(line)-1]) - 1]
        ok = files
        dumb = 0
        for um in line:
            if dumb or not um in ok: 
                dumb = 1
                ok.update({um: {}})
            ok = ok[um]
    num = 0
    for m in range(M):
        line = r.readline().split('/')
        del line[0]
        if line[len(line)-1][len(line[len(line)-1]) - 1:] == '\n': line[len(line)-1] = line[len(line)-1][:len(line[len(line)-1]) - 1]
        ok = files
        dumb = 0
        for um in line:
            if dumb or not um in ok: 
                num += 1
                dumb = 1
                ok.update({um: {}})
            ok = ok[um]
    answer += str(num) + '\n'
    w.write(answer)
    
    
r.close()
w.close()
print 'done'