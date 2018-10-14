def solve(fout,case,commands,O,B):
    result = 0

    Opos = 1
    Bpos = 1

    while(len(commands)):
        while eval(commands[0]+"pos")!=commands[1]:
            result += 1
            if len(O)>0:
                if Opos>O[0]:
                    Opos -= 1
                elif Opos<O[0]:
                    Opos += 1

            if len(B)>0:
                if Bpos>B[0]:
                    Bpos -= 1
                elif Bpos<B[0]:
                    Bpos += 1
        result += 1
        if O == eval(commands[0]):
            if len(B)>0:
                if Bpos>B[0]:
                    Bpos -= 1
                elif Bpos<B[0]:
                    Bpos += 1
        else:
            if len(O)>0:
                if Opos>O[0]:
                    Opos -= 1
                elif Opos<O[0]:
                    Opos += 1            
        exec(commands[0] +'='+ commands[0]+'[1:]')
        commands = commands[2:]
    
    fout.write("Case #"+str(case)+": "+str(result)+"\n")

def main():
    #setting up
    fin = open("input.txt","r")
    fout = open("output.txt","w")
    
    case = 0
    for line in fin:
        case += 1
        O = [] #Orange Commands
        B = [] #Blue Commands
        commands = line.split()
        commands = commands[1:]
        last = ''
        for i in range(len(commands)):
            if commands[i] == 'O':
                last = 'O'
            elif commands[i] == 'B':
                last = 'B'
            elif last == 'O':
                O.append(int(commands[i]))
                commands[i] = int(commands[i])
                last = ''
            elif last == 'B':
                B.append(int(commands[i]))
                commands[i] = int(commands[i])
                last = ''
        solve(fout,case,commands,O,B)

    fout.close()
    fin.close()

main()
