in_t = "6 2 8 29 20 8 18 18 21"

def get_max(in_t):
    in_t = in_t.split(' ')
    num = int(in_t[0])
    sus = int(in_t[1])
    p = int(in_t[2])

    if(p == 0):
        return num

    usr = 0

    in_t = in_t[3 : len(in_t)]
    for node in in_t:
        n = int(node)

        if(n == 0):
            continue
    
        if((n % 3) == 0):
            best = n / 3
            if(best >= p):
                usr = usr + 1
            else:
                if(sus > 0):
                    best = n / 3
                    best = best + 1
                    if(best >= p):
                        usr = usr + 1
                        sus = sus - 1
        elif(((n + 2) % 3) == 0):
            best = (n + 2) / 3
            if(best >= p):
                usr = usr + 1
        elif(((n - 2) % 3) == 0):
            best = (n - 2) / 3
            best = best + 1
            if(best >= p):
                usr = usr + 1
            else:
                if(sus > 0):
                    best = (n + 1) / 3
                    best = best + 1
                    if(best >= p):
                        usr = usr + 1
                        sus = sus - 1

    return usr

source = open('input_large.in')
source_str = source.read()
source_list = source_str.split('\n')
source.close()

input_num = int(source_list[0])
source_list = source_list[1 : len(source_list) - 1]

f = open('A-large.out', 'w')
line = 1
for node in source_list:
    l = get_max(node)
    f.write("Case #" + str(line) + ": " + str(l) + '\n')
    print(line)
    line = line + 1
f.close()
        
                
