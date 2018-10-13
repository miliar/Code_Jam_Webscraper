a="abcdefghijklmnopqrstuvwxyz "
b="yhesocvxduiglbkrztnwjpfmaq "
d=dict(zip(a,b))

for c in range(1,input()+1): print"Case #%d:"%c, "".join(map(d.get,raw_input()))


