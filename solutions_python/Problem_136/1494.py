f = open('B-large.in', 'r')
outf = open('output2large.txt', 'w')

T = int(f.readline())

def find_shortest(C, F, X):
    shortest = X / 2
    farm_num = 0
    build_farm_time = 0
    while True:
        build_farm_time += C / (2 + F * farm_num)
        farm_num += 1
        new_finish_time = build_farm_time + X / (2 + F * farm_num)
        if new_finish_time < shortest:
            shortest = new_finish_time
        else:
            break
    return shortest
    

for test_ind in range(T):
    tmp = f.readline()
    C, F, X = map(float, tmp.split())
    shortest = find_shortest(C, F, X)
    out_str = 'Case #' + str(test_ind + 1) + ': ' + str(shortest) + '\n'
    outf.write(out_str)

f.close()
outf.close()
