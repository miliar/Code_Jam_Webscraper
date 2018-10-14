fo = open('A-large.in','r')
fw = open('output_file','w')

num_tc = int(fo.readline())

output_str = ''
for tci in xrange(1,num_tc+1):
    smax, strn = fo.readline().strip('\n').split(' ')
    
    num_standing = 0
    num_new = 0
    for num_req in xrange(len(strn)):
        if num_req > (num_standing + num_new):
            num_new += (num_req - (num_standing + num_new))
        
        num_standing += int(strn[num_req])
    
    output_str += 'Case #' + str(tci) + ': ' + str(num_new) + '\n'

fw.write(output_str)
