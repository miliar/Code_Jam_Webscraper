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
#define maxn 105

long long d[maxn][maxn];
int n, q;
int e[maxn], s[maxn];
double f[maxn][maxn][maxn];
bool done[maxn][maxn][maxn];    

struct triple {
    int i, j, k;
};

bool operator <(const triple& x, const triple& y) {
    return 0;
}

priority_queue< pair<double, triple> > qu;

int main() {
    ios_base::sync_with_stdio(0);
    freopen("c_large.inp", "r", stdin);
    freopen("c_large.out", "w", stdout);
    
    int test;
    cin >> test;

    FOR(t, 1, test) {
        cout << "Case #" << t << ": ";

        cin >> n >> q;
        FOR(i, 1, n) cin >> e[i] >> s[i];

        FOR(i, 1, n) FOR(j, 1, n) cin >> d[i][j];
        FOR(i, 1, n) d[i][i] = 0;
        FOR(k, 1, n) FOR(i, 1, n) FOR(j, 1, n)
            if (d[i][k] != -1 && d[k][j] != -1) 
                d[i][j] = d[i][j] == -1 ? d[i][k] + d[k][j] : min(d[i][j], d[i][k] + d[k][j]);

        FOR(i, 1, n) FOR(j, 1, n) FOR(z, 1, n) f[i][j][z] = -1.0;

        while (!qu.empty()) qu.pop();
        RESET(done, false);

        FOR(i, 1, n) {
            f[i][i][i] = 0; 
            triple x;
            x.i = x.j = x.k = i;
            qu.push(make_pair(0, x));
        }

        while (!qu.empty()) {
            pair<double, triple> t = qu.top();
            qu.pop();

            double ti = -t.first;
            triple v = t.second;

            if (done[v.i][v.j][v.k]) continue;
            done[v.i][v.j][v.k] = true;

            FOR(z, 1, n) {
                if (d[v.j][z] >= 0 && e[v.j] >= d[v.j][z]) {
                    triple x;
                    x.i = v.i, x.j = z, x.k = v.j;

                    double newTi = 1.0 * d[x.k][x.j] / s[x.k];

                    if (f[v.i][z][v.j] <= -0.1 || newTi + ti < f[x.i][x.j][x.k]) {
                        f[x.i][x.j][x.k] = newTi + ti;
                        
                        qu.push(make_pair(-f[x.i][x.j][x.k], x));
                    }
                }
            }
        }

        FOR(i, 1, q) {
            int u, v;
            cin >> u >> v;

            double res = -1.0;
            FOR(z, 1, n) if (f[u][v][z] > -0.1)
                res = res < 0 ? f[u][v][z] : min(res, f[u][v][z]);

            printf("%.9lf ", res);
        }

        cout << endl;
    }

    return 0;
}