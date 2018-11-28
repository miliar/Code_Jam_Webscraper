

if __name__ == "__main__":
    inn = open("problems/A-large.in", "r")
    out = open("one-large-out", "w")
    l = inn.readline()
    for i in range(0, int(l)):
        o=[]
        b=[]
        t = inn.readline().split(' ')
        nexts = []
        for j in range(1,len(t)):
            if t[j]=='O': 
                o.append(int(t[j+1]))
                nexts.append('O')
            if t[j]=='B': 
                b.append(int(t[j+1]))
                nexts.append('B')
        
        curr_b = 1
        curr_o = 1
        index_b = 0
        index_o = 0
        index = 0
        if len(b) > 0: next_b = b[index_b]
        else: next_b = -1000
        
        if len(o) > 0: next_o = o[index_o]
        else: next_o = -1000
        counter = 0
        complete_b = len(b)==0
        complete_o = len(o)==0
        while index < len(nexts):
            if nexts[index] == 'O':
                dist = abs(curr_o-next_o)+1
                curr_o = next_o
                if not complete_b:
                    if dist > abs(curr_b-next_b): curr_b = next_b
                    elif curr_b > next_b: curr_b = curr_b - dist
                    elif curr_b < next_b: curr_b = curr_b + dist
                index_o += 1
                if index_o < len(o): next_o = o[index_o]
                else: complete_o = True
            
            else:
                dist = abs(curr_b-next_b)+1
                curr_b = next_b
                if not complete_o:
                    if dist > abs(curr_o-next_o): curr_o = next_o
                    elif curr_o > next_o: curr_o = curr_o - dist
                    elif curr_o < next_o: curr_o = curr_o + dist
                index_b += 1
                if (index_b) < len(b): next_b = b[index_b]
                else: complete_b = True
                
            index += 1
            counter += dist
        out.write("Case #" + str(i+1) + ": " + str(counter)+ "\n")
    out.close()
    inn.close()
                
            
        
        
        