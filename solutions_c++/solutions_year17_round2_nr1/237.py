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
char a[maxn][maxn], x[maxn][maxn];
int ns;

int main() {
    ios_base::sync_with_stdio(0);
    freopen("a_large.inp", "r", stdin);
    freopen("a_large.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ": ";

        double d, n, k, s;
        double maxx = -1.0;

        cin >> d >> n;
        FOR(i, 1, n) {
            cin >> k >> s;
            maxx = max(maxx, (d-k) / s);
        }

        printf ("%.9lf\n", d / maxx);
    }

    return 0;
}