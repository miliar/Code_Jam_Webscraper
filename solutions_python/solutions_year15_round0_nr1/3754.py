# Jethro Muller
# 11 April 2015
# Problem A. Standing Ovation

answers = {}
case = 0
with open('in.in') as in_file:
    for line in in_file.readlines()[1:]:
        case += 1
        stand_count = 0
        friend_count = 0
        max_shy = int(line.split(' ')[0])
        values = (int(i) for i in line.split(' ')[1] if i!='\n')
        # print values
        
        for value, num in zip(values, xrange(max_shy+1)):
            if stand_count >= max_shy:
                break
            if value == 0:
                continue            
            if stand_count <= num:
                friend_count += num - stand_count
                stand_count += num - stand_count
                
            stand_count += value

        answers.update({case: friend_count})

with open('out.out', 'w') as out_file:
    for key, value in answers.iteritems():
        print 'Case #%d: %d' % (key, value)
        out_file.write('Case #%d: %d\n' % (key, value))
