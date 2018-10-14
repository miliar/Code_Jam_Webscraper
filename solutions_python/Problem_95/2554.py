f = open('A-small-attempt1.in')
lines = f.readlines()


dict = {"a":"y","b":"h","c":"e","d":"s","e":"o","f":"c","g":"v","h":"x","i":"d","j":"u","k":"i","l":\
        "g","m":"l","n":"b","o":"k","p":"r","q":"z","r":"t","s":"n","t":"w","u":"j","v":"p","w":"f","x":"m","y":"a","z":"q"," ":" ", "\n":""}
x = 1
for l in lines[1:]:
    line = list(l)

    for i in range(len(line)):
        line[i] = dict[line[i]]
    
    print("Case #{}:".format(x),"".join(line))
    x = x+1
        
