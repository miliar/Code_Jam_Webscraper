#define _USE_MATH_DEFINES

#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int INF = 1000 * 1000 * 1000 + 11;


void modify(ld U, vector<ld> &p) {
    sort(p.begin(), p.end());
    
    ld left = 0.0, right = 1.0;
    while (right - left > 1e-14) {
        ld mid = (left + right) / 2.0;
        
        ld need = 0.0;
        for (ld val : p) {
            if (val >= mid) break;
            need += mid - val;
        }
        
        if (need <= U) {
            left = mid;
        } else {
            right = mid;
        }
    }
    
    ld res = (left + right) / 2.0;
    
    for (ld &val : p) {
        val = max(val, res);
    }
}


ld solve(int n, int k, ld U, vector<ld> &p) {
    modify(U, p);
    
    vector<vector<ld>> dp(n + 1, vector<ld>(n + 1, 0.0));
    dp[0][0] = 1;
    
    for (int i = 1; i <= n; ++i) {
        dp[i][0] = 1.0;
        for (int j = 1; j <= n; ++j) {
            dp[i][j] = dp[i - 1][j - 1] * p[i - 1] + dp[i - 1][j] * (1.0 - p[i - 1]);
            dp[i][0] -= dp[i][j];
        }
    }
    
    /*
    cout << '\n';
    cout.precision(2);
    for (int i = 0; i <= n; ++i) {
        for (int j = 0; j <= n; ++j) {
            cout << dp[i][j] << ' ';
        }
        cout << '\n';
    }
    */
    
    ld res = 0.0;
    for (int i = k; i <= n; ++i) {
        res += dp[n][i];
    }
    
    return res;
}


int main() {
    ios_base::sync_with_stdio(false);
    
    cout.precision(20);
    cout << fixed;
    
    int tests;
    cin >> tests;
    
    for (int test = 0; test != tests; ++test) {
        int n, k;
        cin >> n >> k;
        ld U;
        cin >> U;
        
        vector<ld> p(n);
        for (auto &elem : p) cin >> elem;
        
        cout << "Case #" << test + 1 << ": " << solve(n, k, U, p) << "\n";
    }
    
    return 0;
}