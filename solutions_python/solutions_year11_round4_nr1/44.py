def int_input():
    return int(raw_input())

def list_int_input():
    return map(int, raw_input().split())

def list_char_input():
    return list(raw_input())

def table_int_input(h):
    return [list_int_input() for i in range(h)]

def table_char_input(h):
    return [list_char_input() for i in range(h)]

def run_plain(x, s, r, t, ways):
    ways.sort(key=lambda i: i[0])
    
    len_plain = 0
    last_end = 0
    
    for way in ways:
        len_plain += way[0] - last_end
        last_end = way[1]
    
    len_plain += x - last_end
    
    run_time = min(t, float(len_plain) /r)
    run_distance = run_time * r
    walk_distance = len_plain - run_distance
    walk_time = float(walk_distance) / s
    time = run_time + walk_time
    
    return (time, run_time)

def run_on_ways(x, s, r, t, ways):
    ways.sort(key=lambda i: i[2])
    
    time = 0
    
    for way in ways:
        way_distance = way[1] - way[0]
        
        run_way_speed = r + way[2]
        walk_way_speed = s + way[2]
        
        run_time = min(t, float(way_distance) / run_way_speed)
        run_distance = run_time * run_way_speed
        walk_distance = way_distance - run_distance
        walk_time = float(walk_distance) / walk_way_speed
        
        t -= run_time
        time += run_time + walk_time
    
    return time

def solve(case):
    x, s, r, t, n = list_int_input()
    ways = [list_int_input() for i in range(n)]
    
    time, run_time = run_plain(x, s, r, t, ways)
    time += run_on_ways(x, s, r, t - run_time, ways)
    
    print 'Case #%d: %.10f' % (case, time)

def main():
    for i in range(int_input()):
        solve(i+1)

main()

