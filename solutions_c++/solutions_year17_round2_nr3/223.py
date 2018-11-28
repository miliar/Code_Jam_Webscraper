#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef pair<double, int> pdi;
const double INF = 1e20, EPS = 1e-6;
#define x first
#define y second

const int N = 1024;
double d[N];
double g[N][N];
double e[N], s[N];

int n, q;

int main() {
    int T; scanf("%d", &T); FOE(ca, 1, T) {
        scanf("%d%d", &n, &q);
        FOR(i, 0, n) scanf("%lf%lf", e + i, s + i);
        FOR(i, 0, n) FOR(j, 0, n) {
            scanf("%lf", &g[i][j]);
            if (i == j) g[i][j] = 0;
            else if (g[i][j] < 0) g[i][j] = INF;
        }

        // all pair
        FOR(k, 0, n) FOR(i, 0, n) FOR(j, 0, n) g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
        /*
        FOR(i, 0, n) {
            FOR(j, 0, n) printf(" %f", g[i][j]);
            puts("");
        }
        */
        printf("Case #%d:", ca);
        while (q--) {
            int u, v; scanf("%d%d", &u, &v); --u; --v;
            FOR(i, 0, n) d[i] = INF;

            priority_queue<pdi, vector<pdi>, greater<pdi> > pq;
            d[u] = 0.0;
            pq.push(pdi(0.0, u));

            while (!pq.empty()) {
                int src = pq.top().y;
                double cur = pq.top().x;
                pq.pop();
                //printf("(%f %d\n", cur, src);

                if (cur > d[src] + EPS)  continue;
                FOR(i, 0, n) {
                    if(g[src][i] < e[src] + EPS) {
                        double tmp = d[src] + (g[src][i] / s[src]);
                        //printf("Exp %d->%d tmp=%f cur=%f\n", src+1, i+1, tmp, d[i]);
                        if (tmp < d[i] - EPS) {
                            d[i] = tmp;
                            pq.push(pdi(tmp, i));
                        }
                    }
                }
            }
            printf(" %.9f", d[v]);
        }
        puts("");
    }
    return 0;
}
