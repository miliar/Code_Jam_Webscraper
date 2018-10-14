# Google Code Jam 2017 Qualification Round
# Problem C. Bathroom Stalls

def stall(N, K):
    current = [[i, N - (i + 1)] for i in range(N)]
    for i in range(K):
        minimum = 0
        places = []
        for j in range(N):
            if current[j] != 'x':
                if min(current[j]) >= minimum:
                    if min(current[j]) == minimum:
                        places += [j]
                    else:
                        minimum = min(current[j])
                        places = [j]
        maximum = max(current[places[0]])
        new = places[0]
        for j in places[1:]:
            if current[j] != 'x':
                if max(current[j]) > maximum:
                    maximum = max(current[j])
                    new = j
        final = [max(current[new]), min(current[new])]
        current[new] = 'x'
        switch = new + 1
        while switch < N and current[switch] != 'x':
            if current[switch][0] > switch - (new + 1):
                current[switch][0] = switch - (new + 1)
            else:
                break
            switch += 1
        switch = new - 1
        while switch >= 0 and current[switch] != 'x':
            if current[switch][1] > new - (switch + 1):
                current[switch][1] = new - (switch + 1)
            else:
                break
            switch -= 1
    return str(final[0]) + ' ' + str(final[1])

def stalls():
    f = open('stall.txt', 'r')
    g = open('stalls.txt', 'w')
    line = 0
    for i in f:
        if line == 0:
            T = int(i)
            line = 1
        else:
            space = False
            N = ''
            K = ''
            for j in i:
                if j == ' ':
                    space = True
                else:
                    if space:
                        K += j
                    else:
                        N += j
            g.write('Case #' + str(line) + ': ')
            g.write(stall(int(N), int(K)))
            g.write((line != T)*'\n')
            print line
            line += 1
    f.close()
    g.close()
        
    
    
