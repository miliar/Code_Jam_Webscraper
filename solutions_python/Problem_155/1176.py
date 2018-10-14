f = open('A-large.in', 'r')
x = f.read().split('\n')
f.close()
L = []
# reading the file:
x.pop(0)
if x.__contains__(''):
    x.remove('')
for i in x:
    j = i.split(" ")
    h = []
    for k in j[1]:
        h.append(k)
    L.append(h)

Result = []
for p in L:
    c_stand = 0
    f_added = 0
    k=0
    for i in p:
        if k <= c_stand:
            c_stand = c_stand + int(i)
        else:
            f_added = f_added + (k - c_stand)
            c_stand = c_stand + (k - c_stand) + int(i)
        k=k+1
    Result.append(f_added)

# writing the results to file
f = open('file.out', 'w')
j = 1
for i in Result:
    f.write('Case #' + str(j) + ': ' + str(i) +'\n') # python will convert \n to os.linesep
    j=j+1
f.close()
