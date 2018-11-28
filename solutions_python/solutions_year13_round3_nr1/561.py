charactors = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vowls = ['a', 'e', 'i', 'o', 'u']
def containsConstants(sub, n):
    count = 0

    for i in range(0, len(sub)):
        if count == n: return True
        
        if sub[i] in vowls:
            count = 0
        else:
            count += 1

    if count == n: return True

    return False


i = open("A-small-attempt.in", "r+")
o = open("output.txt", "w+")

text = i.readlines()

i.close()

T = int(text[0])
del[text[0]]

for i in range(0, T):
    print(i)
    temp = text[0].split(' ')
    del[text[0]]
    
    s = temp[0]
    n = int(temp[1])

    nameVal = 0

    for k in range(n, len(s)+1):
        start = 0
        end = k

        while end < len(s) + 1:
            sub = s[start:end]
            if containsConstants(sub, n):
                nameVal += 1
                #print(sub)
            start += 1
            end += 1

    o.write("Case #" + str(i+1) + ": " + str(nameVal) + "\n")

o.close()
