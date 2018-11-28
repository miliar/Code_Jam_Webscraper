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
#define maxn 30

int m, n;
char a[maxn][maxn], x[maxn][maxn], c[maxn];
int ns;
int coun[maxn], minx[maxn], maxx[maxn], miny[maxn], maxy[maxn], indx[300];

int main() {
    ios_base::sync_with_stdio(0);
    freopen("a_large.inp", "r", stdin);
    freopen("a_large.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ":" << endl;

        cin >> m >> n;
        ns = 0;
        FOR(i, 1, m) FOR(j, 1, n) cin >> a[i][j];

        FOR(i, 1, m) {
            FOR(j, 2, n) if (a[i][j] == '?' && a[i][j-1] != '?') a[i][j] = a[i][j-1];
            DOW(j, n-1, 1) if (a[i][j] == '?' && a[i][j+1] != '?') a[i][j] = a[i][j+1];
        }
        FOR(j, 1, n) {
            FOR(i, 2, m)   if (a[i][j] == '?' && a[i-1][j] != '?') a[i][j] = a[i-1][j];
            DOW(i, m-1, 1) if (a[i][j] == '?' && a[i+1][j] != '?') a[i][j] = a[i+1][j];
        }

        FOR(i, 1, m) {
            FOR(j, 1, n) cout << a[i][j];
            cout << endl;
        }
    }

    return 0;
}