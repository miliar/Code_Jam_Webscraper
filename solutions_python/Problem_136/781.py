OUT_STR = 'Case #%d: %0.7f'    
def time_to_win(target, speed):
    return target/speed

def do_task(cost, grow, target):
    speed = 2
    time = 0
    while True:
        if (cost/speed+time_to_win(target, speed+grow))<time_to_win(target,speed):
            time += cost/speed
            speed += grow
        else: return time+time_to_win(target, speed)


def read_case(number, in_fl, out_fl):
    (cost, grow, target) = map(float, in_fl.readline().strip().split())
    out_fl.write(OUT_STR%(number, do_task(cost, grow, target)))
    
input_fl = open('B-large.in','r')
output_fl = open('B-large.out', 'w')
cases = int(input_fl.readline().strip())
for n in range(1, cases+1):
    read_case(n, input_fl, output_fl)
    if n!=cases: output_fl.write('\n')
input_fl.close()
output_fl.close()
