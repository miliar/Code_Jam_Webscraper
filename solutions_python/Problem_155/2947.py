
def parseIt(num,array):
    total = 0
    amount = 0
    array = [int(i) for i in array]
    for n, i in enumerate(array):
        if n == 0:
            total += i
            continue
        if i != 0:
            #print("n,i: ", n,i)
            #print("total: ", total)
            good = 0
            if total < n:
                good = n - total
                amount += good
            #print("amount: ", amount)
            #print()
            total += i + good

    return amount

#print(parseIt(9, "0010030103"))

g = open("output.txt","w")
f = open("A-large.in","r")
amount = int(f.readline())
for i in range(amount):
    names = list(f.readline().split())
    num = int(names[0])
    people = list(names[1])
    x = ("Case #"+ str(i+1)+ ": "+  str(parseIt(num, people))) + "\n"
    g.write(x)

g.close()
