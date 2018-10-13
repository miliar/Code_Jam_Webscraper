#Python 3.6
#Jeremiah Gastilo

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n = input()  # read a list of integers, 2 in this case
    for x in range(1, len(n)):
        if n[-x] < n[-(x+1)]:
            n = str(int(n)-(int(n[-x:])+1))
    print("Case #{}: {}".format(i, n))