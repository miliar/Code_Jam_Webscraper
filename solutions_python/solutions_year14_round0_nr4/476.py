output = []
with open('D-large.in.txt') as file:
    T = int(file.readline().split()[0])
    for i in xrange(T):
        N = int(file.readline().split()[0])
        nao = sorted([float(x) for x in file.readline().split()])
        ken = sorted([float(x) for x in file.readline().split()])
        ken_left = ken[:]
        nao_left = nao[:]
        
        j = 0
        while j < len(nao) and ken_left:
            ken_left = [x for x in ken_left if x > nao[j]]
            if ken_left:
                j += 1
                ken_left.remove(ken_left[0])
        
        k = 0
        while k < len(ken) and nao_left:
            nao_left = [x for x in nao_left if x > ken[k]]
            if nao_left:
                k += 1
                nao_left.remove(nao_left[0])
        output += ['Case #' + str(i + 1) + ': ' + str(k) +  ' ' + str(len(nao) - j)]

with open('output.txt', 'w') as f:
    f.write('\n'.join(output))