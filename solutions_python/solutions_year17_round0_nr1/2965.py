
def pancake_flipper(seq, n):
    newseq=seq
    nseq=seq
    count = 0
    for i in range(len(seq)):
        s = seq[i]
        if s == '-':
            newseq = seq[0:i] + "+"
            for j in range(1, n):
                
                if i+n-1 < len(seq):
                    if seq[i+j] == "+":
                        newseq += "-"
                    else:
                        newseq += "+"
                else:
                    return "IMPOSSIBLE"
            newseq += seq[i+n:len(seq)]
            seq = newseq
            count += 1
    return(count)

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    seq, n = input().split(" ")  # read a list of integers, 2 in this case
    
    res = pancake_flipper(seq, int(n))
    
    print("Case #{}: {}".format(i, res))

