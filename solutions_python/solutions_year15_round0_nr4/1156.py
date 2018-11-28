f= open("D-small-attempt0.in","r")
data = f.read().splitlines()
z=int(data[0])


result = ""
counter = 0
for i in range(z):
    counter += 1
    first = data[i+1].split(" ")
    x = int(first[0])
    m = int(first[1])
    n = int(first[2])
    if  (n*m)%x ==0: 
        if x >2 :
            if n*m > x:
                if min(m,n) > float(x/2):
                    result += "Case #" + str(counter) + ": " + "GABRIEL"+ "\n"
                else:
                    result += "Case #" + str(counter) + ": " + "RICHARD" + "\n"
            else:
                result += "Case #" + str(counter) + ": " + "RICHARD" + "\n"
        else:
            if n*m >= x:
                result += "Case #" + str(counter) + ": " + "GABRIEL" + "\n"
            else:
                result += "Case #" + str(counter) + ": " + "RICHARD" + "\n"
    else:
        result += "Case #" + str(counter) + ": " + "RICHARD" + "\n"
        
    
        
hamada2 = open("hamada2.txt", "w")
hamada2.write(result)
hamada2.close()