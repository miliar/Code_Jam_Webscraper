#include <cmath>
#include <cstdio>
#include <vector>
#include <queue>
#include <iterator>
#include <numeric>
#include <memory>
#include <set>
#include <map>
#include <unordered_map>
#include <cstring>
#include <climits>
#include <iostream>
#include <algorithm>
using namespace std;

// #define DEBUG

int num_of_digit(uint64_t n) {
    int i = 0;
    while (n != 0) {
        n = n / 10;
        i ++;
    }
    return i;
}

uint64_t generate_num(uint8_t * arr, int digits){
    int i = 0;
    uint64_t res = 0;
    for (i = 0; i < digits; ++i) {
        res += arr[i];
        if (i == digits - 1) {
            break;
        }
        res = res * (uint64_t) 10;
    }
    return res;
}

uint64_t input;
void solve(int Tn){
    uint64_t N;
    uint64_t ans = 0;
    
    cin >> N;


    int digits = num_of_digit(N);

    #ifdef DEBUG
    cout << "num digit: " << digits << endl;
    #endif

    // extract
    uint8_t num[digits];
    uint64_t temp = N;
    int i;
    for (i = 0; i < digits; ++i) {
        num[digits - i - 1] = temp % 10;
        temp /= 10;
    }

    #ifdef DEBUG
    cout << "digits: ";
    for (i = 0; i < digits; ++i) {
        cerr << (int)num[i] << " ";
    }
    cout << endl;
    #endif

    if (digits == 1) {
        ans = N;
        #ifdef DEBUG
        cout << "single digit!" << endl;
        #endif
        cout << "Case #" << Tn + 1 << ": " << ans << endl;
        return;
    }

    // find first decreasing
    int first_decreasing_prev_num = -1;
    for (i = 1; i < digits; ++i) {
        if (num[i] < num[i-1]) {
            first_decreasing_prev_num = num[i-1];
            break;
        }
    }

    if (first_decreasing_prev_num == -1) {
        ans = N;
        cout << "Case #" << Tn + 1 << ": " << ans << endl;
        return;
    }

    int first_nonincreasing_index_with_fdpn = 0;
    for (i = 0; i < digits; ++i) {
        if (num[i] == first_decreasing_prev_num) {
            first_nonincreasing_index_with_fdpn = i;
            break;
        }
    }

    #ifdef DEBUG
    cout << "first_nonincreasing_index_with_fdpn = " << i << endl;
    #endif

    num[first_nonincreasing_index_with_fdpn] --;
    for (i = first_nonincreasing_index_with_fdpn+1; i < digits; ++i) {
        num[i] = 9;
    }
    ans = generate_num(num, digits);

    cout << "Case #" << Tn + 1 << ": " << ans << endl;
}
int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int T;
    cin >> T;
    int i;
    for (i = 0; i < T; ++i) {
        solve(i);
        #ifdef DEBUG
        cout << endl;
        #endif
    }
    return 0;
}

