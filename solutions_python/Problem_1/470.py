def init_name_table(name_list):
    table = {}
    for name in name_list:
        table[name] = -1
    return table

def calc(name_list, query_list):
    switch_count = 0
    while len(query_list) > 0:
        name_to_first_pos = init_name_table(name_list)
        num_names = len(name_list)
        count = 0
        for q in query_list:
            if name_to_first_pos[q] == -1:
                num_names -= 1
                name_to_first_pos[q] = count
                if num_names == 0:
                    break
            count += 1
        
        if count >= len(query_list) and num_names == 0:
            return switch_count + 1
        elif count >= len(query_list) and num_names > 0:
            return switch_count
        query_list = query_list[count:]
        switch_count += 1
    
    return switch_count

ncases = int(raw_input())

for i in range(ncases):
    search = []
    query = []
    SN = int(raw_input())
    for s in range(SN):
        search.append(raw_input())
    QN = int(raw_input())
    for q in range(QN):
        query.append(raw_input())
    switches = calc(search, query)
    print "Case #" + str(i+1) + ": " + str(switches)

