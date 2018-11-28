#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <list>
#include <stack>
#include <tuple>
#include <utility>
#include <complex>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <typeinfo>
using namespace std;

typedef long long lint;
typedef pair<int,int> pii;
typedef pair<lint,lint> pll;

#define REP(i,n) for(int i=0; i<(n); i++)
#define REPA(i,s,e) for(int i=(s); i<=(e); i++)
#define REPD(i,s,e) for(int i=(s); i>=(e); i--)
#define ALL(a) (a).begin(), (a).end()

#define PRT(a) cerr << #a << " = " << (a) << endl
#define PRT2(a, b) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << endl
#define PRT3(a, b, c) cerr << #a << " = " << (a) << ", " << #b << " = " << (b) << ", " << #c << " = " << (c) <<  endl
template <class Ty> void print_all(Ty b, Ty e) {
    cout << "[ ";
    for(Ty p=b; p!=e; ++p) {
        cout << (*p) << ", ";
    }
    cout << " ]" << endl;
}

// -----------------------------------------------------------------------------
// Code starts 
// -----------------------------------------------------------------------------

int N, C, M;
int table[1011][1011];
int cost[1011][1011];
int sum[1011];


const int INF = 1000000;
const int MAX_V = 10000;
const int MAX_E = MAX_V * MAX_V;
struct edge { int to, cap, cost, rev; };

vector<edge> G[MAX_V];
int dist[MAX_V];
int h[MAX_V];
int prevv[MAX_V];
int preve[MAX_V];

int V;

void add_edge(int from, int to, int cap, int cost) {
    edge e1 = {to, cap, cost, G[to].size()};
    G[from].push_back(e1);
    edge e2 = {from, 0, -cost, G[from].size()-1};
    G[to].push_back(e2);
}

int mincost(int s, int t, int f) {
    int res = 0;
    fill(h, h+V, 0);
    while(f > 0) {
        fill(dist, dist+V, INF);
        priority_queue<pii, vector<pii>, greater<pii> > que;
        dist[s] = 0;
        que.push(pii(0, s));
        while(!que.empty()) {
            pii p = que.top();
            que.pop();

            int nv = p.second;
            int nc = p.first;
            if(dist[nv] < nc) continue;

            for(int i=0; i<G[nv].size(); i++) {
                edge& e = G[nv][i];
                int gap = h[nv] - h[e.to];
                if(e.cap > 0 && dist[e.to] > dist[nv] + e.cost + gap) {
                    dist[e.to] = dist[nv] + e.cost + gap;
                    que.push(pii(dist[e.to], e.to));
                    prevv[e.to] = nv;
                    preve[e.to] = i;
                }
            }
        }

        if(dist[t] == INF) return -1;

        for(int v=0; v<V; v++) h[v] += dist[v];

        int d = f;
        for(int v=t; v!=s; v=prevv[v]) {
            d = min(d, G[prevv[v]][preve[v]].cap);
        }
        f -= d;
        res += d * h[t];
        for(int v=t; v!=s; v=prevv[v]) {
            edge& e = G[prevv[v]][preve[v]];
            e.cap -= d;
            G[v][e.rev].cap += d;
        }
    }
    return res;
}

int check(int K) {
    REP(i, MAX_V) {
        G[i].clear();
    }

    int nv = C + 3 * N;
    int S = nv;
    int T = nv + 1;
    V = nv + 2;

    REP(i, C) {
        add_edge(S, i, sum[i], 0);
    }

    REP(i, N) {
        add_edge(C + i, C + 2 * N + i, INF, 0);
        add_edge(C + N + i, C + 2 * N + i, INF, 0);
        add_edge(C + 2 * N + i, T, K, 0);
    }

    REP(i, C) {
        REP(j, N) {
            add_edge(i, C + j, table[i][j], 0);
            add_edge(i, C + N + j, cost[i][j] - table[i][j], 1);
        }
    }

    return mincost(S, T, M);
}

void solve() {
    memset(table, 0, sizeof(table));
    memset(sum, 0, sizeof(sum));

    cin >> N >> C >> M;
    fprintf(stderr, "%d %d %d\n", N, C, M);
    REP(i, M) {
        int P, B;
        cin >> P >> B;
        table[B - 1][P - 1] += 1;
        sum[B - 1] += 1;
    }

    memcpy(cost, table, sizeof(table));
    REP(i, C) {
        for (int j = N - 1; j >= 1; j--) {
            cost[i][j - 1] = cost[i][j] + cost[i][j - 1];
        }
    }

    int maxs = 0;
    REP(i, C) {
        maxs = max(maxs, sum[i]);
    }

    int lo = maxs;
    int hi = M + 1;
    int prom = -1;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        int f = check(mid);
        if (f == -1) {
            lo = mid + 1;
        } else {
            hi = mid;
            prom = f;
        }
    }
    printf("%d %d\n", lo, prom);
}

// -----------------------------------------------------------------------------
// Code ends 
// -----------------------------------------------------------------------------

void coding() {
    int T;
    cin >> T;
    REPA(t,1,T) {
        fprintf(stderr, "%3d / %d\n", t, T);
        printf("Case #%d: ", t);
        solve();
    }
}

#define _LOCAL_TEST 2

int main() {
#if _LOCAL_TEST == 0
    clock_t startTime = clock();
    freopen("b.in", "r", stdin);
#elif _LOCAL_TEST == 1
    freopen("../input/B-small-attempt1.in", "r", stdin);
    freopen("../output/B-small.out", "w", stdout);
#elif _LOCAL_TEST == 2
    freopen("../input/B-large.in", "r", stdin);
    freopen("../output/B-large.out", "w", stdout);
#endif

    coding();

#if _LOCAL_TEST == 0
    clock_t elapsedTime = clock() - startTime;
    cerr << endl;
    cerr << (elapsedTime / 1000.0) << " sec elapsed." << endl;
    cerr << "This is local test" << endl;
    cerr << "Do not forget to comment out _LOCAL_TEST" << endl << endl;
#endif

}
