n = int(input())
tc = []
l = []
print('\n\n\n\n')
for x in range(0,n):
    tc.append(int(input()))
counter = 1
for t in tc:
    for a in range(t,0, -1):
        b = [int(x) for x in str(a)]
        if b == sorted(b):
            print("Case #"+str(counter) + ': ' + str(a) )
            counter = counter + 1
            break
print(l)
