//#include <bits/stdc++.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
using namespace std;
#define FOR(i, a, b) for(int i = a; i <= b; i ++)
#define DOW(i, a, b) for(int i = a; i >= b; i --)
#define RESET(c, val) memset(c, val, sizeof(c))
#define oo 1e9
#define eps 1e-9
#define base 1000000007
#define maxn 150

int n, p, a[maxn], x, k;

int main() {
    ios_base::sync_with_stdio(0);
    freopen("a_large.inp", "r", stdin);
    freopen("a_large.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ": ";

        cin >> n >> p;

        RESET(a, 0);
        FOR(i, 1, n) cin >> x, a[x%p] ++;

        if (p == 2) {
            cout << a[0] + (a[1] + 1) / 2 << endl;
        } else if (p == 3) {
            int k1 = a[0];
            int k2 = min(a[1], a[2]);
            int k3 = (max(a[1], a[2]) - min(a[1], a[2])) / 3;
            int res = k1 + k2 + k3 + ((k1 + k2*2 + k3*3) < n);
            cout << res << endl;
        } else if (p == 4) {
            int k1 = a[0];
            int k2 = min(a[1], a[3]) + (a[2] / 2);
            int rest13 = max(a[1], a[3]) - min(a[1], a[3]);
            int rest2 = a[2] % 2;

            int k3 = 0;
            if (rest13 >= 2 && rest2 == 1) k3 = 1, rest13 -= 2, rest2 = 0;

            int k4 = rest13 / 4;
            int res = k1 + k2 + k3 + k4 + ((k1 + k2*2 + k3*3 + k4*4) < n);
            cout << res << endl;
        }
    }

    return 0;
}