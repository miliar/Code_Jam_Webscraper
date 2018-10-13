import JamFiles as Files

def check(pancakes):
    return (True and "-" not in pancakes)

def parsePan(line):
    first = line.split(" ")
    second = (first)
    if len(first)>1:
        second = [[x for x in first[0]],int(first[1])]
    return second

def flip(pancakes, k, i):
    for x in range(i,k+i):
        if pancakes[x] == "-":
            pancakes[x] = "+"
        else:
            pancakes[x] = "-"
    return pancakes

def iterate(N):
    k = N[1]
    pan = N[0]
    count = 0
    for test in range(1000):
        for i in range(0, len(pan)-k+1):
            if pan[i] == "-":
                #print ("b: "  , pan)
                pan = flip(pan, k, i)
                #print("a: " , pan)
                count += 1

        #for i in range(len(pan)-1, k-1):
        #    if pan[i] == "-":
         #       pan = flip(pan, k, i-k)
          #      count += 1
                
        if check(pan):
            return count
    return "IMPOSSIBLE"

contents = Files.readToContents(parsePan, "p2.in")
ans = []

for N in contents[1:]:
    ans.append(iterate(N))

#print (ans)

Files.writeFile(ans, Files.syntax, "Outpancakes.txt")

N = [["-","-","-","+","-","+","+","-"],3]
pan = N[0]
k = N[1]
print (pan)
pan = flip(pan, k, 0)
print (pan)
pan = flip(pan, k, 4)
print (pan)
pan = flip(pan, k, 5)
print (pan)
print (check(pan))
N = [["-","+","-","+","-"],4]
pan = N[0]
k = N[1]
print (iterate(N))

#print (Files.readToContents(parsePan, "p1.in"))
