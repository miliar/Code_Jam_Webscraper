

def find_flipped(sequence, m):
    count=0
    sequence=[i for i in sequence]
    for i in range(len(sequence)):
        if sequence[i]=='-':
            count+=1
            if i+m>len(sequence):
                return 'IMPOSSIBLE'
            for j in range(m):
                if sequence[i+j]=='-':
                    sequence[i+j]='+'
                else:
                    sequence[i+j]='-'
    return count


def main():
  t = int(raw_input())  # read a line with a single integer
  for i in xrange(1, t + 1):
    sequence, m = [s for s in raw_input().split(" ")]
    m=int(m)
    n=find_flipped(sequence,m)
    print "Case #{}: {}".format(i,n)

main()