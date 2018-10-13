f = open("A-large.in",'r')
fw = open('a-large_out.txt','w')


N = f.readline()

for i in range(1,int(N)+1):
    sequence = f.readline()
    s = sequence.split()
    bp = 1
    op = 1
    
    K = s[0]
    ap = 1
    
    tm = 1
    b_order = []
    b_button = []
    o_order = []
    o_button = []
    
    button_count = 0
    
    bot = ''
    for m in s[1:]:
        
        if m == 'B' or m == 'O':
            bot = m
        else:
            if bot.strip() == 'O':
                button_count = button_count + 1
                o_order.append(button_count)
                o_button.append(m)
            else:
                button_count = button_count + 1
                b_order.append(button_count)
                b_button.append(m)            
    b_button_count = 0
    o_button_count = 0
    
    bot = s[ap]
    button = s[ap+1]
    b_to_press = 1
    
   
    while 1:
        button_pressed = 0
        
        if o_button_count <= len(o_button)-1:
            if op == int(o_button[o_button_count]):
                if int(o_order[o_button_count]) == b_to_press and button_pressed == 0:
                    button_pressed = 1
                    b_to_press = b_to_press + 1
                    o_button_count = o_button_count + 1

                if b_to_press > int(K):
                    break
            else:
                if op > int(o_button[o_button_count]):
                    op = op -1
                else:
                    op = op +1


        if b_button_count <= len(b_button)-1:                
            if bp == int(b_button[b_button_count]):
                if int(b_order[b_button_count]) == b_to_press and button_pressed == 0:
                    button_pressed = 1
                    b_to_press = b_to_press + 1
                    b_button_count = b_button_count + 1

                if b_to_press > int(K):
                    break
            else:
                if bp > int(b_button[b_button_count]):
                    bp = bp -1

                else:
                    bp = bp +1                
        tm = tm + 1        

        
        
        
    print('Case ' + str(i) + ' tm: ' + str(tm))    
    fw.write('Case #%i: %i\n' % (i,tm))











f.close()
fw.close()

