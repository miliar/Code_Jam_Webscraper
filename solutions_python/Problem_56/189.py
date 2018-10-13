


def join(w,k,lines):
    start_line = w-1
    for i in range(w):
        line = lines[i]
        if line.find('R') >= 0 or line.find('B') >= 0:
            start_line = i
            break

    for i in range(start_line,w):
        line = lines[i]
        line = line.replace('.','')
        lines[i] = line[::-1]

    hor_R_match = ''
    for i in range(k):
        hor_R_match = hor_R_match + 'R'

    hor_B_match = ''
    for i in range(k):
        hor_B_match = hor_B_match + 'B'

    B_win = False
    R_win = False
    
    print lines
    
    for i in range(start_line,w):
        if lines[i].find(hor_B_match) >= 0:
            B_win = True
        elif lines[i].find(hor_R_match) >= 0:
            R_win = True

    v_lines = ['' for i in range(w)]
    
    for i in range(w):
        line = ''
        for j in range(start_line,w):
            t = lines[j]
            if len(t) > i:
                line = line+t[i]
            else:
                line = line + '.'
                
        v_lines[i] = line


    
    for i in range(w):
        if v_lines[i].find(hor_B_match) >= 0:
            B_win = True
        elif v_lines[i].find(hor_R_match) >= 0:
            R_win = True
            
    l_lines = ['' for i in range(2*w)]

    for i in range(w):
        line = ''
        for j in range(start_line,w):
            y = i + j - start_line
            t = lines[j]
            if y >= w:
                break
            if y >= len(t):
                line = line + '.'
            else:
                line = line + t[y]
            
        l_lines[i] = line

    for i in range(w+1,2*w):
        line = ''
        s = i-w
        
        for j in range(start_line+s,w):
            y = j - start_line - s
            t = lines[j]
            if y >= w:
                break
            if y >= len(t):
                line = line + '.'
            else:
                line = line + t[y]
            
        l_lines[i] = line

    print l_lines
    
    for i in range(2*w):
        if l_lines[i].find(hor_B_match) >= 0:
            B_win = True
        elif l_lines[i].find(hor_R_match) >= 0:
            R_win = True

    r_lines = ['' for i in range(2*w)]

    for i in range(w):
        line = ''
        for j in range(start_line,w):
            t = lines[j]
            y = i - j + start_line
            
            if y < 0 or y >= w:
                break
            if y >= len(t):
                line = line + '.'
            else:
                line = line + t[y]

        r_lines[i] = line

    for i in range(w+1,w*2):
        s = i-w
        line = ''
        for j in range(w-1,start_line+1,-1):
            t = lines[j]
            y = start_line + s
            
            if y < 0 or y >= w:
                break
            if y >= len(t):
                line = line + '.'
            else:
                line = line + t[y]

        r_lines[i] = line

    print r_lines
    
    for i in range(2*w):
        if r_lines[i].find(hor_B_match) >= 0:
            B_win = True
        elif r_lines[i].find(hor_R_match) >= 0:
            R_win = True
            
    if R_win and B_win:
        return 'Both\n'
    elif R_win:
        return 'Red\n'
    elif B_win:
        return 'Blue\n'
    else:
        return 'Neither\n'
    

f = open('A-small-attempt1.in')
#f = open('A-small-attempt0(2).in')
fw = open('result.out','w+')

n = int(f.readline())

for i in range(1,n+1):
    fw.write('Case #')
    fw.write(str(i))
    fw.write(': ')
    line = f.readline().replace('\n','')
    data = line.split(' ')
    width = int(data[0])
    k = int(data[1])
    lines = []
    for j in range(width):
        lines.append(f.readline().replace('\n',''))
    
    l = join(width,k,lines)
    fw.write(l)

f.close()
fw.close()
