#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
#include <deque>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <complex>
#include <cstring>
#include <cassert>
#include <bitset>

using namespace std;
#define rep(i, a, b) for(int i = (a); i < (b); i++)
#define repd(i, a, b) for(int i = (a); i > (b); i--)
#define forIt(it, a) for(__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define forRev(it, a) for(__typeof((a).rbegin()) it = (a).rbegin(); it != (a).rend(); it++)
#define ft(a) __typeof((a).begin())
#define ll long long
#define ld long double
#define fi first
#define se second
#define mk make_pair
#define pb push_back
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define Rep(i,n) for(int i = 0; i < (n); ++i)
#define bitcount(n) __builtin_popcountll(n)

typedef complex<ld> cplex;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef vector<ii> vii;
typedef vector<iii> viii;

const int N = 2000 + 7;
const int M = 20;
const int inf = 1000000007;
const long long linf = 1e18 + 7;
const double pi = acos(-1);
const double eps = 1e-9;
const bool multipleTest = 1;

template <typename T>
class MinCostMaxFlow {
    const static int MAXE = 1000007;
    const static int MAXV = 2007;
    const static int inf = 1000000007;

    int adj[MAXE], link[MAXE], head[MAXV];
    T cap[MAXE], flow[MAXE], cost[MAXE];
    T pot[MAXV];
    int n, s, t, E;
    int which[MAXV], can[MAXV], dist[MAXV] ;
    int qu[MAXE];

    T maxFlow, minCost;

    bool spfa() {
        for(int i = 0; i < n; ++i) {
            dist[i] = inf;
            can[i] = 0;
        }
        dist[s] = 0;
        int top = 0;
        qu[top++] = s; can[s] = 1;

        for(int i = 0; i < top; ++i) {
            int u = qu[i];

            for(int e = head[u]; e != -1; e = link[e]) {
                int v = adj[e];

                if (flow[e] < cap[e]) {

                    if (dist[v] > dist[u] + cost[e]) {
                        dist[v] = dist[u] + cost[e];
                        which[v] = e;
                        if (!can[v]) {
                            can[v] = 1;
                            qu[top++] = v;
                        }
                    }
                }

            }
            can[u] = 0;
        }

        return dist[t] < inf;
    }



public:

    MinCostMaxFlow() {

    }

    MinCostMaxFlow(int _n, int _s, int _t) {
        n = _n;
        s = _s;
        t = _t;
        E = 0;

        for(int i = 0; i < n; ++i) head[i] = -1;
        maxFlow = minCost = 0;
    }

    void reset(int _n, int _s, int _t) {
        n = _n;
        s = _s;
        t = _t;
        E = 0;


        for(int i = 0; i < n; ++i) head[i] = -1;
        maxFlow = minCost = 0;
    }

    void add(int u, int v, T cap0, T cost0) {
        adj[E] = v; flow[E] = 0; cap[E] = cap0; cost[E] = cost0; link[E] = head[u]; head[u] = E++;
        adj[E] = u; flow[E] = 0; cap[E] = 0; cost[E] = -cost0; link[E] = head[v]; head[v] = E++;
    }


    T process(T desiredFlow = inf) {
        maxFlow = minCost = 0;
        while (maxFlow < desiredFlow) {

            //            cout << "hrere " << "\n";
            if (!spfa()) return 0;
            int delta = desiredFlow - maxFlow;
            for(int v = t, e = which[v]; v != s; v = adj[e ^ 1], e = which[v]) {
                delta = min(delta, cap[e] - flow[e]);
            }
            //            cout << delta << "\n";
            for(int v = t, e = which[v]; v != s; v = adj[e ^ 1], e = which[v]) {
                flow[e] += delta;
                flow[e ^ 1] -= delta;
            }

            maxFlow += delta;
            minCost += delta * dist[t];
        }
        return 1;
    }

    T getCost() {
        return minCost;
    }

    T getFlow() {
        return maxFlow;
    }

};

MinCostMaxFlow<int> maxFlow;

vi a[N];

int n, m, c;

int cnt[2];

void solve() {
    cin >> n >> c >> m;
    for (int  i = 0; i <= c; ++i) {
        a[i].clear();
        cnt[i] = 0;
    }
    for (int i = 1; i <= m; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        a[v - 1].push_back(u);
        if (u == 1) cnt[v - 1]++;
    }

    if (n == 1) {
        cout << m << " 0\n";
        return;
    }



    maxFlow.reset(m + 2, 0, m + 1);
    for (int i = 0; i < a[0].size(); ++i) {
        for (int j = 0; j < a[1].size(); ++j) {
            if (a[0][i] != a[1][j]) {
                maxFlow.add(i + 1, j + 1 + a[0].size(), 1, 0);
            } else {
                if (a[0][i] != 1) {
                    maxFlow.add(i + 1, j + 1 + a[0].size(), 1, 1);
                }
            }
        }
    }
    for (int i = 0; i < a[0].size(); ++i) maxFlow.add(0, i + 1, 1, 0);
    for (int i = 0; i < a[1].size(); ++i) maxFlow.add(i + 1 + a[0].size(), m + 1, 1, 0);

    maxFlow.process(inf);

//    cout << a[0].size() << ' ' << a[1].size() << '\n';

    cout << a[0].size() + a[1].size() -  maxFlow.getFlow() << ' ' << maxFlow.getCost() << '\n';



}

int main() {
#ifdef _LOCAL_
    freopen("in.txt", "r", stdin);
#endif
        freopen("out.txt", "w", stdout);
    int Test = 1;
    if (multipleTest) {
        cin >> Test;
    }
    for(int i = 0; i < Test; ++i) {
        printf("Case #%d: ", i + 1);
        solve();
    }
#ifdef _LOCAL_
//    cout<<"\n" << 1.0 * clock() / CLOCKS_PER_SEC;
#endif
}


// fu = fk + ck^2 * (k - u + 1)  + cu * (n - k ... n - u) - hk
// - ck^2 * u - ck (1 .. u)
// - 2cu * n * u + cu * u * (u - 2) = ck * [u * (u - 2 - 2 * n)] + g(x)
