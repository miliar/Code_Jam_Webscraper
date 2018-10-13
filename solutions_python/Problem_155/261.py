
def parse_input(inp_file):
    cases = []
    with open(inp_file) as f:
        num_cases = int(f.readline()[:-1])
        for i in range(num_cases):
            tmp = f.readline()
            if "\n" in tmp:
                tmp = tmp[:-1]
            smax, entries = tmp.split(" ")
            entries = [int(i) for i in entries]
            cases.append([int(smax), entries])
    return cases


def standing_ovation(cases):
    with open('data.out', 'w') as f:
        for i,case in enumerate(cases):
            ret =  exec_case(case)
            f.write("Case #%d: %d\n" %(i+1,ret))
            #print("Case #%d: %d\n" %(i+1,ret))
    f.close()
        
def exec_case(case):
    smax, entries = case
    #print smax, entries
    tot = 0
    tot_deficit = 0
    add_to_deficit= 0 
    for i in range(1,len(entries)):
        tot = tot + entries[i-1] 
        if entries[i]!=0:
            if i > tot:
                add_to_deficit = i - tot
                tot_deficit = add_to_deficit + tot_deficit
                tot = tot + add_to_deficit
        #print tot, entries[i], tot_deficit
    #print tot_deficit
    #print "--------------------"
    return tot_deficit

if __name__ == '__main__':
    cases = parse_input('data.in')
    standing_ovation(cases)

