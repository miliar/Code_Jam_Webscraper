def solve_war(naomi, ken):
    cur_pos_naomi = 0
    cur_pos_ken   = 0
    n = len(ken)
    while True:
        while (ken[cur_pos_ken] < naomi[cur_pos_naomi]):
            cur_pos_ken += 1
            if (cur_pos_ken >= n):
                return (n - cur_pos_naomi)
        cur_pos_ken +=1
        cur_pos_naomi += 1
        if (cur_pos_ken >= n):
            return (n - cur_pos_naomi)

def solve_dec(naomi, ken):
    cur_pos_naomi = 0
    cur_pos_ken   = 0
    n = len(ken)
    while True:
        while (naomi[cur_pos_naomi] < ken[cur_pos_ken]):
            cur_pos_naomi += 1
            if (cur_pos_naomi >= n):
                return cur_pos_ken
        cur_pos_ken +=1
        cur_pos_naomi += 1
        if (cur_pos_naomi >= n):
            return cur_pos_ken
    
f_input  = open('d:\gjam\D-large.in', 'r')
f_output = open('d:\gjam\decwar_output.txt', 'w')

n_test = int(f_input.readline())

for i in range(n_test):
    
    n = int(f_input.readline())
    t = f_input.readline()
    naomi = list(map(float, t.split(' ')))
    t = f_input.readline()
    ken   = list(map(float, t.split(' ')))
    naomi.sort()
    ken.sort()

    war_optimal = solve_war(naomi, ken)
    dec_optimal = solve_dec(naomi, ken)
  
    f_output.write('Case #' + str(i+1) + ': ' + str(dec_optimal) + ' ' + str(war_optimal) + '\n')

f_input.close()
f_output.close()
