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

string f(long long n, long long k) {
    map<long long, long long> mp;
    mp[n] = 1;
    long long x;
    while (k > 0) {
    	auto tmp = *mp.rbegin();
        k -= tmp.second;
        x = tmp.first;
        
        mp[x / 2] += tmp.second;
        mp[(x - 1) / 2] += tmp.second;
        mp.erase(tmp.first);
    }
    return to_string(x / 2) + " " + to_string((x - 1) / 2);
}

int main() {
    freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        long long n, k;
        cin >> n >> k;
        cout << "Case #" << test << ": ";
        cout << f(n, k) << "\n";
    }
    return 0;
}

