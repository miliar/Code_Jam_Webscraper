f = open("B-large.in")
T = int(f.readline())

def next_permutation(seq, pred=cmp):
    first = 0
    last = len(seq)
    seq = seq[:]

    if last == 1:
        return [seq[0] + "0"]

    while 1:
        next = last - 1

        while 1:
            next1 = next
            next -= 1
            
            if pred(seq[next], seq[next1]) < 0:
                mid = last - 1
                while not (pred(seq[next], seq[mid]) < 0):
                    mid -= 1
                seq[next], seq[mid] = seq[mid], seq[next]
                
                seq = seq[:next1] + seq[next1:last][::-1] + seq[last:]

                return seq[:]
                break

            if next == first:
                seq.sort()
                i = 0
                while seq[i] == '0':
                    i += 1
                new = [seq[i], "0"]
                [new.append(seq[x]) for x in range(i)]
                [new.append(seq[x]) for x in range(i+1, len(seq))]
                return new

fout = open("B-large.out", "w")
for case in range(1, T+1):
    n = int(f.readline().strip())
    next = next_permutation(list(str(n)))


    
    fout.write("Case #%d: %s\n" % (case, ''.join(next)))
fout.close()
