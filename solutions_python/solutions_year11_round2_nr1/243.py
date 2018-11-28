T = int(raw_input())

def get_wp(stats, team_number):
    return float(stats[team_number]['w']) / (float(stats[team_number]['w']+stats[team_number]['l']))
    
def get_owp(schedule, stats, team_number):
    
    wp_sum = 0
    count = 0
    
    for i in range(len(schedule.items())):
        if i == team_number:
            continue
        s = schedule[i]
       
        w   = stats[i]['w']
        l   = stats[i]['l']
        
        if s[team_number] == '.':
             continue
        elif s[team_number] == '1': # if team won against team_number
             w -= 1
        elif s[team_number] == '0': # if lost
             l -= 1
        
        wp_sum += float(w) / (w+l)
        count += 1
     
     
    return float(wp_sum) / count

def calc_oowp(oowpsum, owps, i, N):
   return float(oowpsum - owps[i]) / (N-1)
   
def calc_oowp_slow(schedule, owps, i):
    s = 0
    count = 0
    for (j, owp) in owps.items():
       if i == j:
          continue
       if schedule[i][j] == '.':
          continue
       s += owp
       count += 1
    
    return float(s) / count
def get_rpi (wp, owp, oowp):
   
   return 0.25 * wp + 0.50 * owp + 0.25 * oowp
   
for test_case in range(T):

   N = int(raw_input())
   
   schedule = {}
   team_stats = {}
   
   
 
   for i in range(N):
       schedule[i] = {}
       team_stats[i] = { 'w' : 0, 'l' : 0 }
             
       line = raw_input();
       
       for (j, val) in enumerate(line):
           schedule[i][j] = val
           if val == '1':
              team_stats[i]['w'] += 1;
           elif val == '0':
              team_stats[i]['l'] += 1;
       
   
    
   wps = {}
   owps = {}
   oowps = {}
   
   oowpsum = 0
   for i in range(N):
       wps[i] = get_wp(team_stats, i)
       owps[i] = get_owp(schedule, team_stats, i)
       oowpsum += owps[i]    
   
   for i in range(N):
       #oowps[i] = calc_oowp(oowpsum, owps, i, N) 
       
       oowps[i] = calc_oowp_slow(schedule, owps, i)
                
   print "Case #%s:" % (test_case + 1)
   for i in range(N):
       print get_rpi(wps[i], owps[i], oowps[i])
       
