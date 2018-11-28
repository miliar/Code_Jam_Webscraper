def min_friends(case, max_shyness, audience_shyness):
    total_people_standing = int(audience_shyness[0])
    friends_needed = 0
    i = 1
    if max_shyness == 0:
        return "Case #{0}: 0\n".format(case)
    
    while i < max_shyness + 1:
        if total_people_standing >= i:
            total_people_standing += int(audience_shyness[i])
        else:
            friends_needed += 1
            total_people_standing += 1 + int(audience_shyness[i])
        i += 1
    return 'Case #{0}: {1}\n'.format(case, friends_needed)
            
        
        
input_file = 'A-small-attempt0.in'
output_file = 'A-small-attempt0.out'
input_f = open(input_file, 'r')
output_f = open(output_file, 'w')
lines = input_f.readlines()
for i in range(1,len(lines)):
    elements = lines[i].split(' ')
    max_shyness = elements[0]
    audience_shyness = elements[1].rstrip()
    output_f.write(min_friends(i, int(max_shyness), audience_shyness))
input_f.close()
output_f.close()
