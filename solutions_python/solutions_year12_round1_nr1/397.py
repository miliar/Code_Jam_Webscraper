f = open('A-small-attempt.in','r')
o = open('A-small-attempt.out','w')

num1 = int(f.readline())

def poserrors(errors):
    if len(errors) == 1:
        return [errors[0], 1-errors[0]]
    else:
        l1 = poserrors(errors[1:]) * 2
        for x in range(0, len(l1)/2):
            l1[x] = l1[x] * errors[0]
            l1[x+len(l1)/2] = l1[x+len(l1)/2] * (1-errors[0])
        return l1
        
def generate(num):
    if num == 1:
        return ["1","0"]
    else:
        l1 = generate(num-1) * 2
        for x in range(0,len(l1)/2):
            l1[x] = "1" + l1[x]
            l1[x+len(l1)/2] = "0" + l1[x + len(l1)/2]
        return l1

for a in range(0,num1):
    typed, total = f.readline().split()
    typed = int(typed)
    total = int(total)
    base = generate (typed)
    errors = f.readline().split()
    for b in range(0,len(errors)):
        errors[b] = float(errors[b])

    per = []
    perrors = poserrors(errors)
    for b in range(0, typed + 2):
        if b == 0:
            count = 0
            for c in range(0,len(perrors)):
                if c == 0:
                    count += (total-typed+1) * perrors[c]
                else:
                    count += (2*total-typed+2) * perrors[c]
            per.append(count)
            
        elif b == typed + 1:
            per.append(total+2)
        else:
            count = 0
            for c in range(0, len(perrors)):
                if ('0' in base[c][:typed-b]):
                    count += (2*total-typed+2 + 2*b) * perrors[c]
                else:
                    count += (total-typed+1 + 2*b) * perrors[c]
            per.append(count)  
    o.write("Case #" + str(a+1) + ": " + str(min(per)) + "\n")

f.close()
o.close()
        
