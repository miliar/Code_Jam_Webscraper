
#GET DATA SET
file = open("B-small-attempt1.in", "r")
data = file.read().split()
del data[0]
file.close()
        
def see_base(data, i, start):
    no = str(int(data[i])-start)
    no_i =[]
    no_k =[]
    for k in range(len(no)):
        no_i.append(no[k])
        no_k.append(no[k])
    no_i.sort()
    if no_i == no_k:
        return no
    else:
        start += 1
        return see_base(data, i, start)
for i in range(len(data)):
    fileo = open("out.txt", "a")
    fileo.write("Case #" + str(i+1) + ": " + see_base(data, i, 0) + "\n")
    fileo.close()
