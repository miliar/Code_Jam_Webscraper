# -*- coding: utf-8 -*-

def get_earnings(coaster_a_day, coaster_size, group_num, groups):
    r = 0
    cnt = 0
    start_list = []
    cur_id = 0
    while(cnt < coaster_a_day):
        if cur_id in start_list:
            loop_val = 0
            loop_coaster_cnt = 0
            riding_num = 0
            start_id = cur_id
            while(True):
                riding_num = 0
                loop_coaster_cnt += 1
                start_id_in_loop = cur_id
                while(True):
                    if (riding_num + int(groups[cur_id])) <= coaster_size:
                        riding_num += int(groups[cur_id])
                        cur_id += 1
                        if cur_id >= group_num:
                            cur_id = 0
                        if cur_id == start_id_in_loop:
                            break
                    else:
                        break
                loop_val += riding_num
                if cur_id == start_id:
                    break
                        
            loop_cnt = (int(coaster_a_day - cnt) / loop_coaster_cnt)
            cnt += (loop_cnt * loop_coaster_cnt)
            r += loop_val * loop_cnt

            if loop_cnt > 0:
                idx = start_list.index(cur_id)
                if cnt >= coaster_a_day:
                    break
                continue
        
        riding_num = 0
        start_id = cur_id
        if not cur_id in start_list:
            start_list.append(cur_id)
        while(True):
            if (riding_num + int(groups[cur_id])) <= coaster_size:
                riding_num += int(groups[cur_id])
                cur_id += 1
                if cur_id >= group_num:
                    cur_id = 0
                if cur_id == start_id:
                    break
            else:
                break
        r += riding_num
        cnt += 1
    return r

if __name__=="__main__":
    import sys
    sys.stdout.flush()
    
    import time
    start = time.time()
    
    cnt = 1
    out = open('C-large.out', 'w')
    first = True
    new_q = True

    coaster_a_day = 0
    coaster_size = 0
    group_num = 0
    groups = []
    for l in open('C-large.in'):
        if first:
            first = False
            new_q = True
            continue
            
        data = l.rstrip("\n").split(' ')
        if new_q:
            if len(data) != 3:
                print 'input error!'
            coaster_a_day = int(data[0])
            coaster_size = int(data[1])
            group_num = int(data[2])
            new_q = False
            print data
            continue
        else:
            groups = data
            new_q = True
            
            out.write('Case #%d: %ld\n' % (cnt, get_earnings(coaster_a_day, coaster_size, group_num, groups)))
            sys.stdout.flush()
            cnt += 1
    out.close()

    end = time.time()
    print 'time = %f' % (end - start)
    """
    coaster_a_day = 4
    coaster_size = 6
    group_num = 4
    groups = [1, 4, 2, 1]
    print get_earnings(coaster_a_day, coaster_size, group_num, groups)
    """
    
    
