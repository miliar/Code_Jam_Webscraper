

out_put = ""

def xxx(data):
    no = 0
    level = 0

    persons = list(data)

    for i in range(len(persons)):
        if i > level:
            no += i - level
            level = i
            level += int(persons[i])


        else:
            level += int(persons[i])



    return no


file =  open('A-small-attempt1.in', 'r')
n = int(file.readline())

for i in range(n):
    xxxx = file.readline().split()
    out_put += str("Case #") + str(i+1) +str(": ")  + str(xxx(xxxx[1])) + str("\n")
#print(out_put)

out  = open('output.out','w')
out.write(out_put)
