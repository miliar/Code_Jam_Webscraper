INPUT = "B-large.in"
OUTPUT = "B-large.out"

def solution():
    in_file = file(INPUT, "r")
    out_file = file(OUTPUT, "w")
    
    lines = in_file.readlines()
    cases_num = int(lines[0])
    
    out_lines = []
    
    for case in range(1,cases_num+1):
        data =  lines[case]
        data = data.strip().split(" ")
        data = [float(i) for i in data]
        C = data[0]
        F = data[1]
        X = data[2]
        total_time = 0
        counter = 0
        end = False
        y = 0

        while not end: 
            t1 = (X - C) / (2 + y * F)
            t2 = ( X / (2 + (y+1)*F))
            
            #print '%d farms time will be %f' % (y , total_time + X / (2 + y * F))
            if t1 <= t2 :
                end = True
                total_time += X / (2 + y*F)
                result = "Case #%d: %s\n" %(case , str(round(total_time,7)))
                out_lines += result
                #print "Case %d farms - %d total time is %s" % (case , counter, str(total_time))
            else:
                total_time += C / (2 + y*F)
                y+=1
                counter += 1
                
    out_file.writelines(out_lines)
    in_file.close()
    out_file.close()
    print 'done'

if __name__ == '__main__':
    solution()