#include<iostream>
using namespace std;


typedef long long int lli;

lli nums[20];
int digit_num;
lli res;

void divs(lli n) {
    digit_num = 0;
    while(n) {
        nums[digit_num++] = n;
        n/=10;
    }
}


bool eval(lli cur, bool smaller, int step) {
    int last_digit = cur % 10;
    int last_second_digit = (cur / 10) % 10;
    if(last_second_digit > last_digit) return false;

    if(step == digit_num) {
        res = cur;
        return true;
    }

    if(smaller) return eval(cur*10+9, true, step+1);
    if(eval(nums[digit_num-step-1], false, step+1)) return true;
    for(int i = last_digit-1; i >= last_second_digit; i--) 
        if(eval(cur - (cur % 10) + i, true, step)) return true;
    

    return false;
}



int main(int argc, char const* argv[]) {
    int t;
    cin >> t;
    for(int i=1;i<=t;i++) {
        lli n;
        cin >> n;
        divs(n);
        eval(nums[digit_num-1], false, 1);
        cout << "Case #" << i << ": " << res << endl;
    }
    
    return 0;
}
