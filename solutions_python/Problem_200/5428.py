def check(k):

    for i in range (len(k)-1):

        if k[i+1] < k[i]:
            return False
        if i > len(k)/2:
            if k[len(k)-i]<k[len(k)-i-1]:
                return False

    return True

n = int(input())

x = []

print (n)


for i in range(n):
    
    a = input()
    x.append(a)

for i in range(n):
    while (check(x[i])==False):

        x[i] = str(int(x[i])-1)

    print ("Case #" + str(i+1) + ": " + str(x[i]))