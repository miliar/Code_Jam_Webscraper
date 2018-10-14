def deceitful_war(list1, list2):
    nwin = 0

    while len(list1) != 0:
        if list1[0] < list2[0]:
            list1.pop(0)
            list2.pop()
        else:
            nwin += 1
            list1.pop(0)
            list2.pop(0)
        
    return nwin

def war(list1f, list2f):
    nwin = 0
    while len(list1f) != 0:
        cur = list1f.pop()
        
        if cur > list2f[len(list2f)-1]:
            list2f.pop(0)
            nwin += 1
            
        else:
            for i in range(len(list2f)):
                if list2f[i] > cur:
                    list2f.pop(i)
                    break

    return nwin                
    
input_f = open('D-large.in', 'r')
output_f = open('D-large.out', 'w')

cases = int(input_f.readline())
case = 0
result = ''

for line in input_f:
    case += 1
    list1 = [float(v) for v in input_f.readline().split()]
    list2 = [float(v) for v in input_f.readline().split()]
    list1.sort()
    list2.sort()
    list1f = list1.copy()
    list2f = list2.copy()

    result += "Case #" + str(case) + ": " + str(deceitful_war(list1, list2)) + " " + str(war(list1f, list2f))
    if case != cases:
        result += "\n"

output_f.write(result)

input_f.close()
output_f.close()
