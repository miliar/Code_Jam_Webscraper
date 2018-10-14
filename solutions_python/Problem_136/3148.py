'''
Created on Apr 12, 2014

@author: Ved

Codejam Qualifying Round B

It makes no sense to wait to buy a factory, if we are going to buy we should always just buy immediately
Thus we only need to check when we reach C cookies
In order to check we need to see how long it would take to exceed the cookie count as opposed to continuing with current cookie rate
'''

def main():
    fo = open('B-large.in', 'r');
    fw = open('B_large.out','w');

    T = int(fo.readline());

    for case in range(T):
        C,F,X = map(float, fo.readline().split());
        rate = 2;
        s = 0;
        cookies = 0;
        while True:
            #Compute how long it would take to finish our goal at current rate
            current_finish = (X-cookies) / rate;
            #If we wait C / rate seconds and buy another factory, how long will that take us?
            possible_finish = C / rate;
            #Plus the updated rated 
            possible_finish += X / (rate + F);
            
            if possible_finish < current_finish: #If buying does us good, then buy and update the rate, cookies, and how long it is taking us
                cookies = 0;
                s += C / rate; #How long it took to buy the factory
                rate += F;
            else: #Don't buy it and continue to the finish
                s += current_finish;
                break;
        
        fw.write("Case #%s: %s" % (str(case+1), str(s)));
        if case < T-1:
            fw.write("\n");
        
        #print (s);       
        
    fo.close();
    fw.close(); 
                

if __name__ == "__main__":
    main();
