def cross_reference(line1, line2):
    matches = 0
    
    for i in range(0,4):
        for j in range(0,4):
            if line1[i] == line2[j]:
                match = line1[i]
                matches += 1

    if matches == 0:
        return "Volunteer cheated!"
    elif matches == 1:
        return str(match)
    elif matches > 1:
        return "Bad magician!"
                

input_f = open('A-small-attempt0.in', 'r')
output_f = open('A-small.out', 'w')

cases = int(input_f.readline())

case = 0
arr1 = 0
arr2 = 0
line1 = []
line2 = []
count = 0

result = ''

for line in input_f:
    if not count%10:
        if count != 0:
            result += "Case #" + str(case) + ": " + cross_reference(line1, line2) + '\n'
        
        case += 1
        arr1 = 0
        arr2 = 0
        line1 = []
        line2 = []
        
        row1 = int(line)
        
    elif not count%5:
        row2 = int(line)
        
    else:
        if arr1 < 4:
            arr1 += 1
            if arr1 == row1:
                line1 = line[:len(line)-1].split()
        else:
            arr2 += 1
            if arr2 == row2:
                line2 = line.split()
    
    count += 1

result += "Case #" + str(case) + ": " + cross_reference(line1, line2)

output_f.write(result)

input_f.close()
output_f.close()
