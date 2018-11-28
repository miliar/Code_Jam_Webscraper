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
#define maxn 100005
#define maxx 10000000

int nto[maxx];
int a, b, k;

int main() {
    ios_base::sync_with_stdio(0);
    freopen("a_large.inp", "r", stdin);
    freopen("a_large.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ": ";

        string s;
        int n, res = 0;
        cin >> s >> n;

        FOR(i, 0, s.length() - n) {
            if (s[i] == '-') {
                res ++;
                FOR(j, i, i+n-1) s[j] = s[j] == '-' ? '+' : '-';
            }
        }

        FOR(i, s.length() - n + 1, s.length() - 1)
            if (s[i] == '-') res = -1;

        if (res > -1) cout << res << endl; else cout << "IMPOSSIBLE" << endl;
    }

    return 0;
}