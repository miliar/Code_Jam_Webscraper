#include<iostream>
using namespace std;

typedef long long int lli;


int add[100];
int digit_num;

void pre_eval(int digit, lli num) {
    for(int i=digit-1;i>0;i--) {
        lli lim = (1 << (i + 1)) - 1;
        if(lim - num < (1 << ( i - 1))) {
            add[i-1] = 1;
            num = lim / 2 - (lim - num);
        } else num = num - (1 << (i-1));
    }
}

int calc_bit(lli num) {
    int res = 0;
    digit_num = 0;
    while(num) {
        if(num & 1) res++;
        num >>= 1;
        digit_num++;
    }
    return res;
}


int main(int argc, char const* argv[]) {
    int t;
    cin >> t;

    for(int i=1;i<=t;i++) {
        lli n,k;
        cin >> n >> k;
        for(int j=0;j<100;j++) add[j] = 0;
        calc_bit(k);
        pre_eval(digit_num, k);
        lli mx = n / 2;
        lli mn = (n-1) / 2;
        lli step = 1;
        for(int j=0;j<digit_num-1;j++) {
            lli next_min;
            lli next_max;
            if(add[j]) {
                next_max = mn / 2;
                next_min = (mn-1)/2;
            } else {
                next_max = mx / 2;
                next_min = (mx-1)/2;
            }
            mx = next_max;
            mn = next_min;
        }
        cout << "Case #" << i << ": ";
        cout << mx << " " << mn << endl;
    }
    return 0;
}
