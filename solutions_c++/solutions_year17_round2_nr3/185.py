/*
 * (c) fushar (Ashar Fuadi)
*/

#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

typedef long long ll;

const int MAXN = 101;
const ll oo = 1000000000000000ll;

int T;
int N, Q;
ll D[MAXN][MAXN], E[MAXN], S[MAXN];

double dist[MAXN];
bool seen[MAXN];

int main() {
    cin >> T;
    REP(tc, T) {
        cin >> N >> Q;
        REP(i, N) {
            cin >> E[i] >> S[i];
        }
        REP(i, N) REP(j, N) {
            cin >> D[i][j];
            if (D[i][j] == -1) {
                D[i][j] = oo;
            }
        }

        REP(k, N) REP(i, N) REP(j, N) {
            D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
        }

        printf("Case #%d:", tc+1);

        REP(q, Q) {
            int u, v;
            cin >> u >> v;
            u--, v--;

            REP(i, N) {
                dist[i] = (double)oo;
                seen[i] = false;
            }

            priority_queue<pair<double, int>> pq;

            dist[u] = 0;
            pq.push(make_pair(0, u));

            while (!pq.empty()) {
                double d;
                int x;
                tie(d, x) = pq.top();
                pq.pop();

                if (seen[x]) {
                    continue;
                }
                seen[x] = true;

                REP(y, N) if (E[x] >= D[x][y]) {
                    double t = (double) D[x][y] / S[x];
                    if (dist[y] > dist[x] + t) {
                        dist[y] = dist[x] + t;
                        pq.push(make_pair(-dist[y], y));
                    }
                }
            }

            printf(" %.7lf", dist[v]);
        }
        printf("\n");

    }
}
