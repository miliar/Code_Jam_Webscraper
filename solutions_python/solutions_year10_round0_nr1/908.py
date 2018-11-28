import StringIO

f = StringIO.StringIO("""4
1 0
1 1
4 0
4 47""")

f = open('A-small-attempt0.in', 'r')

cases = int(f.readline())

def toggle(status):
    all_on = True
    for key, value in status.items():
        if all_on and not status[key]:
            status[key] = True
            all_on = False
            break
        else:
            status[key] = not status[key]
    
    return status

for i in range(cases):
    answer = True
    
    case = f.readline()
    snappers, snapped = case.split()
    
    status = {}
    for j in range(int(snappers)):
        status[j] = False
        
    for j in range(int(snapped)):
        status = toggle(status)
        
    for j in status.values():
        if not j:
            answer = False
            break
    
    print "Case #%d: %s" % (i + 1, "ON" if answer else "OFF")

f.close()