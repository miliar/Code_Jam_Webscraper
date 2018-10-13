f=open("input.txt","r")
g=open("proba.txt","r")
h=open("task.txt","r")
r=open("output.txt","w+")
coded=[]
real=[]
zapis=[]
new=[]
for i in h:
    zapis.append(i)
for i in zapis:
    new.append(str(i).rstrip("\n"))
for i in g:
    real.append(i)
real="".join(real)
real=str(real).split()
real="".join(real)
for i in f:
    coded.append(i)
coded="".join(coded)
coded=str(coded).split()
coded="".join(coded)
#print coded
#print real
dict={}
for i in range(len(coded)):
    dict[coded[i]]=real[i]
dict[' ']=' '
print dict.keys()
for i in range(1,len(new)):
    var=[]
    var.append("Case #")
    var.append(str(i))
    var.append(": ")
    for j in new[i]:
        var.append(dict[j])
    if(i!=len(new)-1):
        var.append("\n")
    var="".join(var)
    r.write(var)
    print var
raw_input()
