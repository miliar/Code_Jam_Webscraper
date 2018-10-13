import os

path = 'A-large.in'
infile = open(path, 'r')
outfile = open(path+'.out', 'w')

t = int(infile.readline())

for i in range(0, t):
    line_parts = infile.readline().split()
    s_max = line_parts[0]
    k_array = []
    for k in line_parts[1]:
        k_array.append( int(k) )
    print(s_max, k_array)

    standing = 0
    friends = 0
    for k, n in enumerate(k_array):
        if( standing < k ):
            friends += k - standing
            standing = k
        standing += n
    outfile.write( 'Case #{}: {}\n'.format( i+1, friends ) )
infile.close()
outfile.close()