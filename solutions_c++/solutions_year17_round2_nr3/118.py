#include<bits/stdc++.h>
#define FOR(i,a,b) for (int i=(a),_b=(b);i<=_b;i=i+1)
#define FORD(i,b,a) for (int i=(b),_a=(a);i>=_a;i=i-1)
#define REP(i,n) for (int i=0,_n=(n);i<_n;i=i+1)
#define FORE(i,v) for (__typeof((v).begin()) i=(v).begin();i!=(v).end();i++)
#define ALL(v) (v).begin(),(v).end()
#define fi   first
#define se   second
#define MASK(i) (1LL<<(i))
#define BIT(x,i) (((x)>>(i))&1)
#define div   ___div
#define next   ___next
#define prev   ___prev
#define left   ___left
#define right   ___right
#define __builtin_popcount __builtin_popcountll
using namespace std;
template<class X,class Y>
    void minimize(X &x,const Y &y) {
        if (x>y) x=y;
    }
template<class X,class Y>
    void maximize(X &x,const Y &y) {
        if (x<y) x=y;
    }
template<class T>
    T Abs(const T &x) {
        return (x<0?-x:x);
    }

/* Author: Van Hanh Pham */

/** END OF TEMPLATE - ACTUAL SOLUTION COMES HERE **/

#define MAX   333
const long long INF = (long long)1e18 + 7LL;
const double EPS = 1e-9;

int lim[MAX], speed[MAX];
long long dist[MAX][MAX];
int n, q;
double minDist[MAX];
bool used[MAX];

void loadGraph(void) {
    scanf("%d%d", &n, &q);
    FOR(i, 1, n) scanf("%d%d", &lim[i], &speed[i]);
    FOR(i, 1, n) FOR(j, 1, n) dist[i][j] = INF;
    FOR(i, 1, n) FOR(j, 1, n) {
        int x; scanf("%d", &x);
        if (x >= 0) minimize(dist[i][j], x);
    }
    FOR(i, 1, n) minimize(dist[i][i], 0);
}

void floyd(void) {
    FOR(k, 1, n) FOR(i, 1, n) FOR(j, 1, n)
        minimize(dist[i][j], dist[i][k] + dist[k][j]);
}

double answer(int s, int t) {
    FOR(i, 1, n) minDist[i] = INFINITY;
    FOR(i, 1, n) used[i] = false;
    minDist[s] = 0;

    REP(love, n + 7) {
        int id = -1;
        FOR(i, 1, n) if (!used[i] && (id < 0 || minDist[id] > minDist[i] + EPS)) id = i;
        if (id < 0) break;

        FOR(j, 1, n) if (dist[id][j] <= lim[id])
            minimize(minDist[j], minDist[id] + 1.0 * dist[id][j] / speed[id]);
        used[id] = true;
    }

    return minDist[t];
}

void process(int tc) {
    printf("Case #%d:", tc);
    REP(pmp, q) {
        int s, t; scanf("%d%d", &s, &t);
        printf(" %.9lf", answer(s, t));
    }
    printf("\n");
}

int main(void) {
    int t; scanf("%d", &t);
    REP(pmp, t) {
        cerr << pmp + 1 << endl;
        loadGraph();
        floyd();
        process(pmp + 1);
    }
    return 0;
}

/*** LOOK AT MY CODE. MY CODE IS AMAZING :D ***/
