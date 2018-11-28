__author__ = 'alessandro.pavesi'

in_file = open("C:\\Users\\alessandro.pavesi\\Downloads\\B-small-attempt1.in", 'r')
out_file = open("C:\\Users\\alessandro.pavesi\\Downloads\\GCJQ1.in", 'w')
t = next(in_file)

def isInAlphabeticalOrder(word):
    return word==''.join(sorted(word))


cont_case = 1
for i in range(int(t)):
    l = 0
    n = next(in_file)
    for j in range(int(n), 0, -1):
        #print (j)
        if isInAlphabeticalOrder(str(j)):
            l = j
            break
    out_file.writelines("Case #{}: {} \n".format(cont_case, l))
    cont_case += 1
