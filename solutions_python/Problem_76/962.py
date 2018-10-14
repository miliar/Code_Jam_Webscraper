#!/usr/bin/python

infile = open("C.in", "rt")
outfile = open("C.out", "wt")

ii = int(infile.readline())

for i in range(ii):
    jj = int(infile.readline())
    kk = [int(_) for _ in infile.readline().split(' ')]
    
    xorn = 0
    sumn = 0
    minn = kk[0]

    for k in kk: 
        xorn ^= k
        sumn += k
        if minn > k: minn = k

    if xorn != 0:
        outfile.write("Case #%s: NO\n" % (i + 1))
    else:
        outfile.write("Case #%s: %s\n" % (i + 1, sumn - minn))


        
