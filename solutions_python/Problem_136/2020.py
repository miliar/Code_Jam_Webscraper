import math

def read_int():
    return int(raw_input());

def read_cfx():
    return ([float(x) for x in raw_input().split()]);

def stop_buying_at(target, cost, base_rate, additional_rate):
#target is the targeted number of cookies, X in the problem
#cost is the cost of a cookie farm, C in the problem
#base_rate is the rate of cookie production from the giant cookie
#additional_rate is the rate addition for a new farm, F
    f = (target * additional_rate - base_rate * cost - \
            additional_rate * cost)/ (cost * additional_rate)
    return int(math.floor(f)+1);

def calc_total_time(target, cost, base_rate, additional_rate):
    stop = stop_buying_at(target, cost, base_rate, additional_rate);
    time_taken = 0;
    rate = base_rate;
    for x in xrange(stop):
        time_taken += cost/rate;
        rate += additional_rate;
    time_taken += target/rate;
    return time_taken;

def main():
    nocases = read_int();
    base_rate = 2;
    for test_case in xrange(1, nocases+1):
        cost, additional_rate, target = read_cfx();
        print ("Case #%d: %.7f" % (test_case, \
                calc_total_time(target, cost, base_rate, additional_rate)));


if __name__ == "__main__":
    main();
