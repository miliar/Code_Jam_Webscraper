def invitees(string):
    invitations = 0
    tmp = []
    for i in range(2,len(string)):
        tmp.append(int(string[i]))
    standing = tmp[0]
    for i in range(1,len(tmp)):
        shylevel = i
        people = tmp[i]
        if(people > 0 and standing < shylevel):
            invitations = invitations + (shylevel - standing)
            standing = standing + invitations + people
        else:
            standing = standing + people 
    return (invitations)

file = open('A-small-attempt4.in','r')
buffer = file.readlines()

T = int(buffer[0])
#print(T)

for i in range(1,T+1):
    Slevels = str(buffer[i]).replace("\n","")
    #print(Slevels)
    opt = "Case #" + str(i) + ": " + str(invitees(Slevels)) + "\n"
    #print(opt)
    with open('A-small-attempt4.out', 'a') as out:
        out.writelines(opt)
    out.close()

file.close()
