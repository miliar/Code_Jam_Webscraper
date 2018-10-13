f_in = open ('c:/temp/codejam/qualification/A-large.in')
f_out = open ('c:/temp/codejam/qualification/A-large.out','w')

T = int(f_in.readline())
for case in range(T):
    N,K = [int(x) for x in f_in.readline().split()]
    if (K+1) % (2**N) == 0:
        f_out.write ('Case #' + str(case+1) + ': ON\n')
    else:
        f_out.write ('Case #' + str(case+1) + ': OFF\n')

f_in.close()
f_out.close()
