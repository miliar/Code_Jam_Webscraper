
in_file = 'A-large.in'
Type = 'large'
out_file = 'A-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

Tt = int(data[0])
del data[0]

OUT = []
for k in range(Tt):
    # Simple loop through (both sides???)
    Seq, K = data[k].split()
    Seq = [1 if l == "+" else 0 for l in Seq]
    Copy_Seq = Seq.copy()
    K = int(K)
    Count = 0
    for P in range(len(Seq) - K + 1):
        if Seq[P] == 0:
            Count += 1
            Seq[P:(P+K)] = [1 - el for el in Seq[P:(P+K)]]
    if sum(Seq) == len(Seq): OUT.append(Count)
    else: OUT.append("IMPOSSIBLE")

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i])) 
