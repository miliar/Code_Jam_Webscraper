f = open("A-large.in")

line = f.readline()
N = int(line[:-1])

for i in range(N):
    line = f.readline()
    L = line[:-1] if line[-1] == '\n' else line
    L = L.split(" ")
    Sm = int(L[0])
    people = L[1]
    
    cnt = int(people[0])
    need = 0
#   print("cnt is", cnt)
    for num in range(1, Sm+1):
 #       print("|",people,"|")
        
        current = int(people[num])
#        print(current)
        
        while num > cnt+need:
#            print("+1")
            need += 1
        cnt += current
#        print("cnt is", cnt)

    print("Case #%d: %d"%((i+1), need) )

f.close()
