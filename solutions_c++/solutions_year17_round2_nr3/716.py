#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

#define For(i, n) for(int i = 0; i < (n); i++)

const int N = 105;
ll dist[N][N];
double distTime[N][N];

void floyd(int n, auto d) {
    For (k, n)
        For (i, n)
            For (j, n) {
                if (d[i][j] > d[i][k] + d[k][j])
                    d[i][j] = d[i][k] + d[k][j];
            }
}

void solve(int n, vector<pii> & hs, vector<pii> & qs) {
    floyd(n, dist);

    For (i, n)
        For (j, n) {
            if (i != j)
                distTime[i][j] = (1LL << 50);
            else 
                distTime[i][j] = 0;
        }

    For (i, n) {
        auto h = hs[i];

        For (j, n) 
            if (i != j && h.first >= dist[i][j])
                distTime[i][j] = min(distTime[i][j], (double)dist[i][j] / h.second);
    } 
    
    floyd(n, distTime);

    for (auto q : qs) 
        printf("%.6lf ", distTime[q.first - 1][q.second - 1]);
}

int main () {
    int t;
    scanf("%d", &t);

    For (i, t) {
        int n, q;
        scanf("%d %d", &n, &q);
        
        vector<pii> hs(n);

        For (i, n)
            scanf("%lld %lld", &hs[i].first, &hs[i].second);

        For (i, n)
            For (j, n) {
                scanf("%lld", &dist[i][j]);
                if (dist[i][j] == -1)
                    dist[i][j] = (1LL << 50);
            }

        For (i, n)
            dist[i][i] = 0;

        vector<pii> qs(q);
        For (i, q)
            scanf("%lld %lld", &qs[i].first, &qs[i].second);

        printf("Case #%i: ", i + 1);
        solve(n, hs, qs);
        puts("");
    }
}