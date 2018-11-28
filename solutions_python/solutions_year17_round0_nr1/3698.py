casos = []
T=input()
for i in range(T):
    casos.append(raw_input())

def todosMas(s):
    j = 0
    while (j < len(s) and s[j] == "+"):
        j += 1
    if (j == len(s)):
        return True
    else: return False

for i in range(len(casos)):
    s,k=casos[i].split(" ")
    k = int(k)
    s = list(s)
    if(todosMas(s)):
        print 'Case #'+ str(i+1)+': '+ "0"
    else:
        tamS = len(s)
        j=0
        y=0
        while (j <= tamS - k):
            if (s[j] == "-"):
                for l in range(j, j + k):
                    if s[l] == "+":
                        s[l] = "-"
                    else:
                        s[l] = "+"
                y+=1
            j += 1
        if (todosMas(s)):
            print 'Case #'+ str(i+1)+ ': '+ str(y)
        else:
            print 'Case #'+ str(i+1)+ ': '+ "IMPOSSIBLE"