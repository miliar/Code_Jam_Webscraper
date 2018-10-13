input_file = open('A-large.in','r')
raw_input = input_file.read()

lines = raw_input.split('\n')

num_cases = int(lines[0])
case_num = 1

output_text = ''
output_file = open('A.out','w')

debug=0

while case_num<=num_cases:
    S_max=int(lines[case_num].split(' ')[0])
    S_list=list(map(int,list(lines[case_num].split(' ')[1])))
    S_lower = [0] #incremental sum of those with lower level
                  #S_lower[i] is sum of S_list[0:i-1]
    
    for i in range(S_max):
        S_lower.append(S_lower[i]+S_list[i])

    if debug:
        print('\nCase #'+str(case_num)+': S_max, S_list, S_lower')
        print(S_max,S_list,S_lower)

    peeps_needed = 0
    for i in range(S_max+1):
        if S_lower[i]<i:  #??
            gap = i - S_lower[i]
            peeps_needed += gap
            for j in range(i+1,S_max+1):
                S_lower[j] += gap

    if debug:
        print('peeps needed: ',peeps_needed)

    output_text += 'Case #'+str(case_num)+': '+str(peeps_needed)+'\n'
    case_num += 1

if debug: print(output_text)
output_file.write(output_text)
input_file.close()
output_file.close()
