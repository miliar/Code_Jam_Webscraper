#!/usr/bin/python3

def main():
    t = int(input());

    for i in range(t):
        c,f,x = input().split()
        c = float(c);
        f = float(f);
        x = float(x);

        out = c + f + x;
        default = 2.0;  #default rate
        time = 0.0;
        max_time = x/default;
        tmin = x/default;
        done = False;
        rate = default
        prev_current = max_time;
        while not done:
            time += c/rate
            rate = rate+f;
#             print(c,'/',rate,'=',time);
#             print('Time at this rate',x/rate)
            current = time + x/rate
#             print('Current:',current);
            if current > prev_current:
                out = prev_current;
                done = True;
            else:
                prev_current = current;
#             if current < tmin:
#                 out = current;
#             if rate >= c or time > max_time:
#                 done = True;
        print('Case #%d: %.7f'%(i+1,out), sep='');
    return 0;

if __name__ == '__main__':
    main();
