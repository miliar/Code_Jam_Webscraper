import codecs

with codecs.open('B-large.in','r','utf-8') as f_in:
    for j in range(int(f_in.readline())):
        data = f_in.readline().strip().split(' ')
        
        #C F X
        c = float(data[0])
        f = float(data[1])
        x = float(data[2])
        s = 2.0
        t_total = 0.0
        while True:
            t_x = x/s
            t_c = c/s + x/(s+f)
            
            if(t_x <= t_c):
                t_total += t_x
                break
            else:
                t_total += c/s
                s += f

        print('Case #%d: %0.7f' % (int(j)+1, t_total))
        