if __name__ == "__main__":
    with open('/home/roberta/Documenti/gcj/A_small0.in', 'r') as filein:
        lines = filein.readlines()
        output = open('/home/roberta/Documenti/gcj/A_small0.txt', 'w')
        for p, line in enumerate(lines[1:]):
            ll = line.split()
            seq = [el for el in ll[0]]
            k = int(ll[1])
            i = 0
            count = 0
            while i < len(seq)-k:
                if seq[i] == '-':
                    count += 1
                    for j in range(k):
                        seq[j+i] = '+' if seq[j+i] == '-' else '-'
                i+=1
            if '+' not in seq[-k:]:
                seq[-k:] = ['+' for el in seq[-k:]]
                count += 1
            if '-' in seq:
                res = 'IMPOSSIBLE'
            else:
                res = str(count)
            output.write('Case #' + str(p + 1) + ': ' + str(res) + '\n')