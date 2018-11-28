def solution(infile, outfile):
    cases = int(infile.readline())
    for i in range(1, cases + 1):
        data = infile.readline().rstrip().split(' ')
        smax = int(data[0])
        audience = [int(x) for x in data[1]]
        ovators, fakes = 0, 0
        for shyness in range(0, smax + 1):
            if ovators < shyness:
                fakes += (shyness - ovators)
                ovators = shyness
            ovators += audience[shyness]
        outfile.write('Case #%s: %s\n' %(i, fakes))

# file_path = 'A-small-attempt1.in'
file_path = 'A-large.in'
# file_path = 'A-tiny.in'
infile = open(file_path, 'r')
outfile = open(file_path + '.out', 'w')
solution(infile, outfile)
infile.close()
outfile.close()
