in_file = open('in', 'r')
out_file = open('out', 'w')

T = int(in_file.readline())

def test(N, K):
    if (K < 2**N -1):
         return False

    for x in range(N):
        if(not K % 2):
            return False
        K = K / 2
    return True

for x in range(T):
    s = in_file.readline()
    N, K = int(s.split()[0]), int(s.split()[1])
    case = 'Case #%d: ' % (x +1)
    case+='ON\n' if test(N, K) else 'OFF\n'
    out_file.writelines(case)

