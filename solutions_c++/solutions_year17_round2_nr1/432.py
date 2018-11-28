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

void solve() {
    int finish, n;
    cin >> finish >> n;
    ld maxspeed = 1e18;
    for (int i = 1; i <= n; i++) {
        ld x, v;
        cin >> x >> v;
        ld t = (finish - x) / v;
        maxspeed = min(maxspeed, (x + v * t) / t);
    }
    cout << fixed << setprecision(6) << double(maxspeed) << endl;
}

int main ()
{
    ios_base::sync_with_stdio(0);cin.tie(NULL);

    freopen("in.txt","r",stdin);
    //freopen("ans.txt","w",stdout);
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    
    return 0;
}
