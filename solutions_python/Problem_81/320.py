from decimal import *
inf = open('A-large.in', 'r')
outf = open('A-large.out', 'w')

T = int(inf.readline())
for case in range(1, T+1):
    N = int(inf.readline())
    gms = []
    wp = []
    for n in range(0,N):
        gms.append(list(inf.readline().rstrip()))
        wp.append(Decimal(gms[n].count('1')) / (Decimal(gms[n].count('1')) + Decimal(gms[n].count('0'))))

    owp = []
    for n in range(0,N):
        owp.append(0)
        cnt = 0
        for n2 in range(0,N):
            if n == n2:
                continue
            ngms = []
            ngms.extend(gms[n2])

            if ngms[n] == '.':
                continue
            ngms[n] = '.'
            cnt += 1
            owp[n] += Decimal(ngms.count('1')) / (Decimal(ngms.count('1')) + Decimal(ngms.count('0')))
        owp[n] /= cnt

    
    oowp = []
    for n in range(0,N):
        oowp.append(0)
        cnt = 0
        for n2 in range(0,N):
            if n == n2 or gms[n][n2] == '.':
                continue
            oowp[n] += owp[n2]
            cnt += 1
        oowp[n] /= cnt
    
    outf.write('Case #' + str(case) + ':\n')
    for n in range(0,N):
        outf.write(str(Decimal(Decimal('0.25') * wp[n]) + Decimal(Decimal('0.5') * owp[n]) + Decimal(Decimal('0.25') * oowp[n])).rstrip('0'))
        outf.write('\n')
  #  print 'Case #' + str(case) + ': '

outf.close()
inf.close()
