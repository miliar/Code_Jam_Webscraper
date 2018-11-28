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

int n, q;
int e[111], s[111], a[111], b[111];
int dd[111][111];

long long dist[111];

map<int, double> dp[111][1111];

double gg(int v, int can, int speed, int goal) {
    if (v == goal) return 0;
    
    double ans = 1e18;
    if (dd[v][v+1] <= can) {
        ans = min(ans, gg(v+1, can - dd[v][v+1], speed, goal) + (1.0 * dd[v][v+1]) / speed);
    }
    // if (e[v] <= can && s[v] <= speed) return ans;
    // if (dist[v] <= can && s[v] <= speed) return ans;
    
    can = e[v]; speed = s[v];
    if (dd[v][v+1] <= can) {
        ans = min(ans, gg(v+1, can - dd[v][v+1], speed, goal) + (1.0 * dd[v][v+1]) / speed);
    }
    return ans;
}

double f(int a, int b) {
    for (int i = 1; i <= n; ++i)
        for (int sp = 0; sp <= 1000; ++sp)
            dp[i][sp].clear();
    
    dist[n] = 0;
    for (int i = n-1; n >= 1; --n)
        dist[i] = dist[i+1] + dd[i][i+1];
    
    return gg(a, e[a], s[a], b);
}

int main() {
    srand(31415);
   freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> n >> q;
        for (int i = 1; i <= n; ++i)
            cin >> e[i] >> s[i];
        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j)
                cin >> dd[i][j];
        for (int i = 0; i < q; ++i)
            cin >> a[i] >> b[i];
        cout << "Case #" << t << ":";
        
        cout.precision(6);
        for (int i = 0; i < q; ++i) {
            cout << " " << fixed << f(a[i], b[i]);
        }
        cout << "\n";
    }
    return 0;
}
