#Round 1a 2017 Problem A

def main():
    t = int(raw_input())
    for i in xrange(1, t+1):
        r, c = [int(s) for s in raw_input().split(" ")]
        table = []
        for j in xrange(r):
            table.append(list(raw_input()))
        print "Case #{}:".format(i)
        result = cake(table)
        for j in xrange(r):
            print ''.join(result[j])
def cake(table):
    letter = ''
    empty = []
    for i in xrange(len(table)):
        if table[i] == ['?']*len(table[i]):
            empty.append(i)
            continue
        for j in xrange(len(table[i])):
            if table[i][j] != '?':
                letter = table[i][j]
            else:
                table[i][j] = letter
        for j in xrange(len(table[i])):
            if table[i][len(table[i])-1-j] != '':
                letter = table[i][len(table[i])-1-j]
            else:
                table[i][len(table[i])-1-j] = letter
        letter = ''
    k = 1
    for i in empty:
        for j in xrange(len(table[i])):
            while i+k < len(table):
                if table[i+k][j] != '?':
                    table[i][j] = table[i+k][j]
                    break
                else:
                    k += 1
            k = 1
            while i-k >= 0:
                if table[i-k][j] != '?':
                    table[i][j] = table[i-k][j]
                    break
                else: k+=1
            k = 1

    return table

if __name__ == '__main__':
    main()
