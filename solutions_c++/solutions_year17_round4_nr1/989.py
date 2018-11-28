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

int p;
int c[11];

map<int, int> dp[11];

int f(int r) {
    int d = 0, v = 1;
    for (int i = 0; i < p; ++i) {
        d += v * c[i];
        v *= 101;
    }
    if (d == 0) return 0;
    
    if (dp[r].count(d)) return dp[r][d];
    
    int ans = 0;
    for (int i = 0; i < p; ++i)
    if (c[i] > 0) {
        c[i]--;
        ans = max(ans, f((p - i + r + p + p) % p));
        c[i]++;
    }
    return dp[r][d] = ans + (r == 0);
}

int main() {
    srand(31415); ios::sync_with_stdio(0);
   freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    // T = 100;
    for (int t = 1; t <= T; ++t) {
    	cerr << t << "\n";
        int n, a;
        cin >> n >> p;
        // n = 100; p = 4;
        for (int i = 0; i < p; ++i) {
            dp[i].clear();
            c[i] = 0;
        }
        for (int i = 0; i < n; ++i) {
            cin >> a;
            // a = i + 1;
            c[a % p]++;
        }
        
        cout << "Case #" << t << ": ";
        
        cout << f(0) << "\n";
    }
    return 0;
}
