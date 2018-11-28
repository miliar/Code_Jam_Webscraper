
r = open("input","r")
lines = r.readlines()

w = open("output","w")

T = int(lines[0])

for f in range(0,T):
    i = (f*10)+1
    j = int(lines[i])
    f_matches = lines[i+j].strip().split(" ")
    j = int(lines[i+5])
    s_matches = lines[i+5+j].strip().split(" ")
    cards = [c for c in f_matches if c in s_matches]
    if cards.__len__() == 1:
        w.write("Case #"+str(f+1)+": " + str(cards[0])+"\n")
    elif cards.__len__() == 0:
        w.write("Case #"+str(f+1)+": Volunteer cheated!\n")
    elif cards.__len__() > 1:
        w.write("Case #"+str(f+1)+": Bad magician!\n")
    else:
        w.write("OUPS\n")

r.close()
w.close()
