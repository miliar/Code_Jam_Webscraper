//
// Created by Xuren Zhou on 8/4/2017.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long tinyNumbers(long n) {
    vector<long> digit;
    long cur_n = n;
    while(cur_n > 0L) {
        long d = cur_n % 10L;
        digit.push_back(d);
        cur_n /= 10L;
    }
    reverse(digit.begin(), digit.end());
    int end = 0;
    bool flag = false;
    for(int i=1; i < digit.size(); i++) {
        if(digit[i] > digit[i-1])
            end = i;
        else if(digit[i] < digit[i-1]) {
            flag = true;
            break;
        }
    }

    if(flag) {
        digit[end] --;
        for(int i=end + 1; i < digit.size(); i++) {
            digit[i] = 9L;
        }
    }

    long res = 0;
    for(int i=0; i < digit.size(); i++) {
        res = res * 10L + digit[i];
    }
    return res;
}


int main() {
    int t;
    cin >> t;
    for(int i=1; i <= t; i++) {
        long n;
        cin >> n;
        long res = tinyNumbers(n);
        cout << "Case #" << i << ": " << res << endl;
    }

    return 0;
}

