with open('A-small-attempt0.in','r') as tfile:
    input_text = tfile.read()
lines = input_text.split('\n')
result = ''
lines[0] = int(lines[0])
for i in range(1,lines[0]+1):
    max_shy = int(lines[i][0])
    lines[i] = lines[i][2:]
    audience = []
    for j in range(max_shy+1):
        audience.append(int(lines[i][j]))
    num_standing = 0
    friends = 0
    for shy_level, num_people in enumerate(audience):
        new_friends = 0
        if num_standing < shy_level and num_people:
            new_friends = shy_level - num_standing
            friends += new_friends
        num_standing += num_people + new_friends
    result += 'Case #{}: {}\n'.format(i, friends)
result = result[:len(result)]
with open('output.txt','w') as tfile:
    tfile.write(result)

        
    