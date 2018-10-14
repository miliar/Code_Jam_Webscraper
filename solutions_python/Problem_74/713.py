# coding=utf8

import sys

trans = {'O': 'B', 'B': 'O'}

if __name__ == '__main__':
    N = int(sys.stdin.readline())
  
    for case, line in enumerate(sys.stdin):
        dist = {'B': [], 'O': []}
        next = []
        parts = line.split()
        curr_point = {'B': 1, 'O': 1}
        for i in xrange(1, len(parts), 2):
            key, value = parts[i], parts[i + 1]
            next.append(key)
            
            dist[key].append(abs(curr_point[key] - int(value)))
            curr_point[key] = int(value)
                
        dist['O'].reverse()
        dist['B'].reverse()
        
        t = 0
        for curr in next:
            t += dist[curr][-1] + 1
            try:
                dist[trans[curr]][-1] = max(0, dist[trans[curr]][-1] - dist[curr][-1] - 1)
            except IndexError:
                pass
            
            dist[curr].pop()
        
        assert not dist['B'] and not dist['O']
        
        sys.stdout.write("Case #%s: %s\n"  % (case + 1, t))
        
            
            
            
        