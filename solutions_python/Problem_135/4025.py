
inf = open('infile.txt', 'r')
lines = [x.strip() for x in inf.readlines()]
inf.close()

outfile = open('outfile.txt', 'w')

T = int(lines[0])

base = 1
for case_num in range(1, T+1):
    answer1 = int(lines[base])-1
    set1 = [x.split(' ') for x in lines[base+1:base+5]]
    answer2 = int(lines[base+5])-1
    set2 = [x.split(' ') for x in lines[base+6:base+10]]
    base += 10
    
    card = 0
    found = 0
    for value in set1[answer1]:
        if value in set2[answer2]:
            found += 1
            card = value
    outfile.write("Case #%d: %s\n" % (case_num, card if found == 1 else ('Bad magician!' if found > 1 else 'Volunteer cheated!')))
outfile.close()
