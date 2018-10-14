# Import the file
in_file = 'B-large.in'
Type = 'small' if in_file.count('small') > 0 else 'large' if in_file.count('large') > 0 else 'test'
out_file = 'B-{0}.out'.format(Type)

with open(in_file,'r') as f:
    data = f.readlines()

data2 = data.copy()
# Format the data
Tt = int(data[0])
del data[0]

OUT = []
for k in range(Tt):
    # Enter code here
    K,L,S = list(map(int,data[0].split(' ')))
    Keys = data[1].replace('\n','')
    Target = data[2].replace('\n','')
    #print(Keys,Target)
    del data[:3]
    # Check if it is possible to get the word from the keys
    Temp = set(Target)
    Temp.difference_update(set(Keys))
    if len(Temp) > 0:
        OUT.append(0)
        continue
    # Otherwise work out the probability of getting the target word
    Probs = {}
    for l in Target:
        Probs[l] = Keys.count(l)/len(Keys)
    # Probability of the word appearing
    P = [Probs[t] for t in Target]
    pi = 1
    for p in P: pi*=p
    # Expected number
    E = (S - len(Target)+1)*pi
    #print(Probs,E)
    # Maximum possible
    N = len(Target)
    Rep = 0
    for i in range(1,N):
        #print(Target,Target[i:],Target[:(N-i)])
        if Target[i:] == Target[:(N-i)]:
            Rep = i
            break
    #print(Rep)
    if Rep == 0:
        M = S//N
    else:
        Temp = Target
        Count = 1
        while len(Temp) + len(Target[(N-Rep):]) <= S:
            Count += 1
            Temp += Target[(N-Rep):]
        M = Count
    #print(M,E)
    OUT.append(M-E)
    pass

with open(out_file,'w') as f:
    for i in range(Tt):
        f.write('Case #{0}: {1}\n'.format(i+1,OUT[i]))
