//#include "testlib.h"
//#include <spoj.h>

#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
#include <assert.h>
#include <time.h>
#include <memory.h>
#include <set>
#include <numeric>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <unordered_map>

using namespace std;

//bool tidy(long long n) {
//    int l = 9, ll;
//    while (n > 0) {
//        ll = n % 10;
//        if (ll > l) return false;
//        l = ll;
//        n /= 10;
//    }
//    return true;
//}
//
//long long brutf(long long n) {
//    while (!tidy(n)) {
//        n--;
//    }
//    return n;
//}

long long get(long long n) {
    string s = to_string(n);
    bool go = 1;
    while (go) {
        go = 0;
        for(int i = 0; i+1 < s.size(); ++i) {
            if (s[i] > s[i+1]) {
                s[i]--;
                for(int j = i+1; j < s.size(); ++j)
                    s[j] = '9';
                go = 1;
                break;
            }
        }
        while (s[0] == '0' && s.size() > 1) {
            s.erase(s.begin());
        }
    }
    return stoll(s);
}

int main() {
//    for(int i = 1; i < 100000; ++i) {
//        if (i % 1000 == 0) {
//            cout << i << "\n";
//        }
//        if (get(i) != brutf(i)) {
//            cout << i << ": Sol: " << get(i) << ", Brutf: " << brutf(i) << "\n";
//            return 0;
//        }
//    }

    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        long long n;
        cin >> n;
        cout << "Case #" << test << ": ";
        cout << get(n) << "\n";
    }
    return 0;
}

