palmas=range(31)
palmas[1]=1
for i in range(2,31):
    total=0
    for k in range(1,i):
        total+=palmas[k]
    palmas[i]=total+i

t=input()
for i in range(t):
    x=raw_input()
    x=x.split()

    if palmas[int(x[0])] == int(x[1])%(palmas[int(x[0])]+1):
        ligado=1
    else:
        ligado=0
    if ligado:
        print("Case #" + str(i+1) + ":" + " ON")
    else:
        print("Case #" + str(i+1) + ":" + " OFF")
