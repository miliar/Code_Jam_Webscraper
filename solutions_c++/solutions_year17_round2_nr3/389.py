#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>

#include <queue>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

typedef pair<double,int> PDI;

#define MP make_pair
#define PB push_back
#define FF first
#define SS second

#define FORN(i, n) for (int i = 0; i <  (int)(n); i++)
#define FOR1(i, n) for (int i = 1; i <= (int)(n); i++)
#define FORD(i, n) for (int i = (int)(n) - 1; i >= 0; i--)

#define DEBUG(X) { cout << #X << " = " << (X) << endl; }
#define PR0(A,n) { cout << #A << " = "; FORN(_,n) cout << A[_] << ' '; cout << endl; }

#define MOD 1000000007
#define INF 2000000000

int GLL(LL& x) {
    return scanf("%lld", &x);
}

int GI(int& x) {
    return scanf("%d", &x);
}

const double EPS = 1e-9;

int T, n, q;

const int MAXN = 105;
double e[MAXN], s[MAXN], edge[MAXN][MAXN], adj[MAXN][MAXN], dist[MAXN];

priority_queue<PDI> pq;

void getadj(int start) {
    pq = priority_queue<PDI>();
    pq.push(MP(0.0, start));

    double maxtime = e[start] / s[start];

    while (pq.size() > 0) {
        auto t = pq.top(); pq.pop();

        if (adj[start][t.SS] <= -EPS) {
            adj[start][t.SS] = -t.FF;

            FOR1(v, n) {
                if (adj[start][v] <= -EPS && edge[t.SS][v] > EPS) {
                    double arrive = adj[start][t.SS] + edge[t.SS][v] / s[start];

                    if (arrive <= maxtime + EPS) {
                        pq.push(MP(-arrive, v));
                    }
                }
            }
        }
    }
}

double getdist(int start, int finish) {
    pq = priority_queue<PDI>();
    pq.push(MP(0.0, start));

    while (pq.size() > 0) {
        auto t = pq.top(); pq.pop();

        if (dist[t.SS] <= -EPS) {
            dist[t.SS] = -t.FF;

            FOR1(v, n) {
                if (dist[v] <= -EPS && adj[t.SS][v] > EPS) {
                    double arrive = dist[t.SS] + adj[t.SS][v];
                    pq.push(MP(-arrive, v));
                }
            }
        }
    }

    return dist[finish];
}

void solve() {
    cin >> n >> q;

    FOR1(i, n) {
        cin >> e[i];
        cin >> s[i];
    }

    FOR1(i, n) {
        FOR1(j, n) {
            cin >> edge[i][j];
        }
    }

    FOR1(i, n) {
        FOR1(j, n) {
            adj[i][j] = -1.0;
        }
    }

    FOR1(i, n) {
        getadj(i);
    }

    /*
    FOR1(i, n) {
        FOR1(j, n) {
            cout << adj[i][j] << " ";
        }
        cout << endl;
    }
    */

    int u, v;

    while (q--) {
        GI(u);
        GI(v);

        FOR1(i, n) dist[i] = -1.0;

        cout << setprecision(12) << getdist(u, v) << " ";
    }
    cout << "\n";
}

int main() {
    GI(T);

    for (int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    
    return 0;
}
