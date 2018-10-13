
def compute_friends(smax, s):
    size = get_audience_size(s)
    clapping = 0
    friends = 0
    
    for i in range(0,len(s)):
        
        Si = int(s[i])
    
        if clapping < i:
            delta = i - clapping
            friends = friends + delta
            clapping = i
            
        clapping = clapping + Si
    return friends



def get_audience_size(s):
    count = 0
    for i in range(0,len(s)):
        count = count + int(s[i])
    return count
    
    
import sys
f = open(sys.argv[1],'r')
contents = f.read()

lines = contents.split('\n')
num_of_cases = lines.pop(0)
case_no = 1
output = open('output.txt','w')
outs = ""
for line in lines:
    test_case = line.split()
    if len(test_case) < 2:
        continue
    smax = test_case[0]
    audience = test_case[1]
    friends = compute_friends(smax, audience)
    outs = outs + "Case #" + str(case_no) + ": " + str(friends) + "\n"
    case_no += 1

output.write(outs)

