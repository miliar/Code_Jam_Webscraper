infile = open('d_in.txt', 'r')
outfile = open('d_out.txt', 'w')
num_cases = int(infile.readline().strip())

for i in xrange(num_cases):
    war_pts = 0
    deceitful_war_pts = 0
    num_blocks = int(infile.readline().strip())
    naomi = [float(j) for j in infile.readline().strip().split()]
    ken = [float(j) for j in infile.readline().strip().split()]
    naomi.sort()
    ken.sort()
    d_naomi = naomi[:]
    d_ken = ken[:]

    # war
    for j in xrange(num_blocks):
        if ken[-1] > naomi[-1]:
            index = -1
            while index > -len(ken) and ken[index-1] > naomi[-1]:
                index -= 1
            naomi.pop(-1)
            ken.pop(index)
        else:
            war_pts += 1
            naomi.pop(-1)
            ken.pop(0)
        
    # deceitful war
    for j in xrange(num_blocks):
        if d_ken[-1] > d_naomi[-1]:
            d_ken.pop(-1)
            d_naomi.pop(0)
        else:
            deceitful_war_pts += 1
            d_ken.pop(-1)
            d_naomi.pop(-1)
    
    outfile.write('Case #' + str(i+1) + ': ' + str(deceitful_war_pts) + ' ' + \
            str(war_pts) + '\n')

infile.close()
outfile.close()
