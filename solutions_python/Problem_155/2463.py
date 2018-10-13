__author__ = 'austinrhodes'

file_in = open('A-large.in','r');
file_out = open('A-large.out','w')
T = int(file_in.readline());
for i in range(0,T):
    N = file_in.readline().split()
    temp = N[1]
    S = list()
    for j in range(0,len(temp)):
        S.append(int(temp[j]))
    standing = 0
    extras = 0
    for k, group in enumerate(S):
        if k <= standing:
            standing += group
        else:
            extras += (k - sum(S[0:k]))
            standing += (k - sum(S[0:k])) + group
            S[k - 1] += k - sum(S[0:k])
    print ("Case #{:d}: {:d}".format((i + 1), extras))
    file_out.write("Case #{:d}: {:d}\n".format((i + 1), extras))
file_in.close()
file_out.close()
