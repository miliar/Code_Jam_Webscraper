import sys

def isTidy(n):
    tidy = True
    n_str = str(n)
    j = len(n_str) - 1
    
    while j > 0 and tidy:
        if n_str[j] < n_str[j-1]:
            tidy = False
        j -= 1

    return tidy
    
inputFile = sys.argv[1]
output = []

with open(inputFile, 'r') as f:
    lines = f.readlines()
    
    for i in range(1, len(lines)):

        number_str = lines[i].strip()
        k = 0
        j = 1
        tidy = True

        while j < len(number_str) and tidy:
            if number_str[j-1] < number_str[j]:
                if number_str[k] < number_str[j-1]:
                    k = j-1
                j += 1
            elif number_str[j-1] > number_str[j]:
                if number_str[k] < number_str[j-1]:
                    k = j-1
                tidy = False
            else:
                j += 1
        
        if tidy:
            print 'Case #%d: %s' % (i, number_str)
            output.append('Case #%d: %s' % (i, number_str))
        else:
            sub = int(number_str[k+1:]) + 1
            number = int(number_str)
            tidy_number = number - sub
            print 'Case #%d: %d' % (i, tidy_number)
            output.append('Case #%d: %d' % (i, tidy_number))


with open('output.txt', 'w') as f:
    f.write('\n'.join(output))