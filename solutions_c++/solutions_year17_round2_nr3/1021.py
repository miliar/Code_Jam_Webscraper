#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <map>
#include <functional>
#include <cassert>
#include <ctime>
#include <chrono>
using namespace std;
typedef long long ll;
typedef pair<int,int> pr;
#define REP(i,m,n) for (int i=(m); i<(n); ++i)
#define RREP(i,m,n) for (int i=(m)-1; i>=n; --i)

int n;
ll line[102] = {0,};
int e[102], s[102]; // horse: maximum total distance, constant speed
double cache[102][1002];

double dfs(int idx, int speed, int rem) {
    if (cache[idx][speed] >= -(1e-9)) return cache[idx][speed];
    if (idx == n-1) return 0.0;

    double m = DBL_MAX / 3.0;
    for (int i=idx+1; i<n; i++) {
        ll dist = line[i] - line[idx];
        // change to new one
        if (line[i] - line[idx] <= e[idx]) { // reachable
            if (e[idx] - dist >= 0)
                m = min(m, (double)dist / s[idx] + dfs(i, s[idx], e[idx] - dist));
        }
        // keep going
        if (line[i] - line[idx] <= rem) {
            if (rem - dist >= 0)
                m = min(m, (double)dist / speed + dfs(i, speed, rem - dist));
        }
    }

    return cache[idx][speed] = m;
}

int main()
{
#ifdef MICRO_LOCAL
    freopen("in.put", "r", stdin);
    chrono::time_point<chrono::high_resolution_clock> timer_start, timer_end;
    timer_start = chrono::high_resolution_clock::now();
#endif
/*----------------------------------------------------------------------------*/
    int T, TT; scanf("%d", &T);
    TT = T;
    while (T--) {
        int q; scanf("%d%d", &n, &q); // cities, pairs (mail)
        ll d[102][102]; // distance matrix
        REP(i,0,n) scanf("%d%d", e+i, s+i);
        REP(i,0,n) REP(j,0,n) scanf("%lld", &d[i][j]);

        REP(i,1,n) line[i] = d[i-1][i] + line[i-1];
        REP(i,0,q) {
            int u, v; // for small: 1 to n
            scanf("%d%d", &u, &v);
        }
        REP(i,0,102) {
            fill(cache[i], cache[i]+1002, -1.0);
        }
        double ans = dfs(0, s[0], e[0]);

        printf("Case #%d: %lf\n", TT-T, ans);
    }
/*----------------------------------------------------------------------------*/
#ifdef MICRO_LOCAL
    timer_end = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = timer_end - timer_start;
    printf("\nElapsed time: %.5lfms\n", elapsed_seconds.count()*1000.);
#endif
    return 0;
}
