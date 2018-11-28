def gcd(number_list):
    if len(number_list) == 1:
        return number_list[0]
    elif len(number_list) == 2:
        x, y = tuple(number_list)
        if y == 0:
            return x
        else:
            return gcd([y, x % y])
    else:
        return gcd([number_list[0]] + [gcd(number_list[1:])])
    
def apocalypse(*t):
    min_t = min(*t)
    dt = map(lambda x: x - min_t, t)
    dt.remove(0)
    T = gcd(dt)
    mod_t = min_t % T
    if mod_t == 0:
        return 0
    else:
        return T - mod_t

in_file = open("Test.in", 'r')
out_file = open("Test.out", 'w')

C = eval(in_file.readline())
for i in range(C):
    t = map(eval, in_file.readline().split(" "))
    N = t[0]
    t = t[1:]
    res = apocalypse(*t)
    out_string = "Case #" + str(i+1) + ": " + str(res) + "\n"
    out_file.write(out_string)
    
in_file.close()
out_file.close()