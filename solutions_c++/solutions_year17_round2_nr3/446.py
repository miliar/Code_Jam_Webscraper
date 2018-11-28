/*
 Created by Saidolda Bayan.
 Copyright (c) 2015 Bayan. All rights reserved.
 LANG: C++
 */
#include <bits/stdc++.h>

#define _USE_MATH_DEFINES
#define y1 lalka
#define right napravo
#define left nalevo
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
using pii = pair<int, int>;
using ll = long long;
using ld = long double;

const int INF = (int)1e9+7, mod = (int)1e9+9, pw = 31, N = (int)1e5+123, M = (int)1e6+123;
const double eps = 1e-11;
const long long inf = 1e18;

enum colors {red, orange, yellow, green, blue, violet};
string what[] = {"R", "O", "Y", "G", "B", "V"};

int n, q;
int d[N];
int s[N];

long long g[111][111];
long double dp[111][111];

void solve() {
    cin >> n >> q;
    for (int i = 1; i <= n; i++)
        cin >> d[i] >> s[i];
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> g[i][j];
            if (g[i][j] == -1)
                g[i][j] = inf;
            if (i == j)
                g[i][j] = 0;
        }
    }
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (d[i] >= g[i][j]) {
                dp[i][j] = (long double) g[i][j] / (long double) s[i];
            } else {
                dp[i][j] = (long double) 1e18;
            }
        }
    }
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
    while (q--) {
        int from, to;
        cin >> from >> to;
        cout << fixed << setprecision(7) << dp[from][to] << ' ';
    }
    cout << endl;
}

int main ()
{
    ios_base::sync_with_stdio(0);cin.tie(NULL);

    freopen("in.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
