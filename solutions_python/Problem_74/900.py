if __name__ == '__main__':
    infile = open('A-large.in').readlines()
    T = int(infile[0].strip())
    wfile = open('result', 'w')
    for j in range(1, T+1):
        s = 0
        line = infile[j].strip()
        tmp = line.split()[1:]
        if tmp[0] == 'B':
            last_bot = 'O'
        else:
            last_bot = 'B'
        lastO = lastB = 1
        last_bot_time = 0
        for i in range(len(tmp)/2):
            bot = tmp[i*2]
            next_pos = int(tmp[i*2+1])
            if bot == 'O':
                next_step = abs(next_pos - lastO)
                lastO = next_pos
            else:
                next_step = abs(next_pos - lastB)
                lastB = next_pos
            
            if bot == last_bot:
                s += next_step + 1
                last_bot_time += next_step + 1
            else:
                more_time = next_step - last_bot_time
                if more_time < 0:
                    more_time = 0
                last_bot_time = more_time + 1
                s += more_time + 1
            
            last_bot = bot
            
        wfile.write('Case #' + str(j) + ': ' + str(s) + '\n')
    wfile.close()