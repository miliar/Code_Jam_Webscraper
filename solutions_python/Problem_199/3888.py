
def flip(string,amount,location):
    #at location flip amount
    if location == 0:
        s1 = ""
    else:
        s1 = string[:location]
##    print(s1)
    toflip = string[location:location+amount]
##    print(toflip)
    flipped = ""
    for letter in toflip:
        if letter == "+":
            flipped += "-"
        else:
            flipped += "+"
    s1 += flipped
    s1 +=(str(string[location+amount:]))
##    print(string[location+amount:])
####    print(len(s1))
    return s1

def next_flip(string,amount):
    if len(string) > 16:
        while True:
            x = 1
    #Finds largest line of -
    max_amount = 0
    max_loaction = 0
    count = 0
    minus = False
    for i in range(len(string)):
        if not minus:
            if string[i] == "-":
                count +=  1
                minus = True
        else:
            if string[i] == "-":
                count += 1
            else:
                if count > max_amount:
                    max_amount = count
                    max_loaction = i-count

                count = 0
                minus = False
    if count > max_amount:
        max_amount = count
        max_loaction = len(string)-count
    while len(string) - max_loaction < amount:
        max_loaction -= 1
    return flip(string,amount,max_loaction)

def get_min_flips(string,amount):
    final_string = ""
    A = string
    for i in range(100):
        if A == "+"*len(string):
            return str(i)
        A = next_flip(A,amount)
    return "IMPOSSIBLE"

infile = open("INPUT.in")
outfile = open("OUTPUT.txt","w")
amount = []
skip = True
for line in infile:
    if skip:
        skip = False
    else:
        temp = line.strip()
        temp = temp.split()
        temp[1] = int(temp[1])
        amount.append(temp)

result = []
for cake in amount:
    result.append(get_min_flips(cake[0],cake[1]))

for i in range(len(result)):
    outfile.write("Case #"+str(i+1)+": "+result[i]+"\n")

outfile.close()




    
