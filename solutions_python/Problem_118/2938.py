datain = open('C-small-attempt0.in', 'r')
dataout = open('dataout.txt', 'w')

def palindrome(i):
    i = str(i)
    if i == i[::-1]:
        return True
    return False

for length in range(int(datain.readline())):

    input = map(int, datain.readline().split())
    
    final = []
    for i in range(input[0], input[1]+1):
        d = int(i**.5)
        if d**2 == i and palindrome(i):
            final.append(i)
    
    final2 = []
    for i in final:
        d = int(i**.5)
        if d**2 == i and palindrome(d):
            final2.append(i)


    dataout.write('Case #' + str(length+1) + ': ' + str(len(final2)) + '\n')

datain.close()
dataout.close()