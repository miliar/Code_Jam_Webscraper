#include <bits/stdc++.h>

using namespace std;

typedef long long     LL;
typedef pair<int,int> pii;

double PI  = acos(-1);
double EPS = 1e-7;
int INF    = 1000000000;
LL INFLL   = 1000000000000000000LL;

#define fi            first
#define se            second
#define mp            make_pair
#define pb            push_back

#define input(in)     freopen(in,"r",stdin)
#define output(out)   freopen(out,"w",stdout)

#define MIN(a, b)     (a) = min((a), (b))
#define MAX(a, b)     (a) = max((a), (b))

#define RESET(a, b)   memset(a,b,sizeof(a))
#define ALL(a)        (a).begin(), (a).end()
#define SIZE(a)       (int)a.size()
#define SORT(a)       sort(ALL(a))
#define UNIQUE(a)     (a).erase( unique( ALL(a) ), (a).end() )
#define FOR(a, b, c)  for (int (a)=(b); (a)<=(c); (a)++)
#define FORD(a, b, c) for (int (a)=(b); (a)>=(c); (a)--)
#define FORIT(a, b)   for (__typeof((b).begin()) a=(b).begin(); a!=(b).end(); a++)

int mx[8] = {-1,1,0,0,-1,-1,1,1};
int my[8] = {0,0,-1,1,-1,1,-1,1};

// ----- //

pair<int, int> horse[105];
int dst[105][105];
long long sp[105][105];
long long big = (long long)1e15;
double dp[105];

int main() {
  int t = 0;
  scanf("%d", &t);
  while(t--) {
    static int tc; tc++;
    printf("Case #%d:", tc);
    int n, q;
    scanf("%d%d", &n, &q);
    for(int i = 0; i < n; i++) {
      scanf("%d%d", &horse[i].fi, &horse[i].se);
    }
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        scanf("%d", &dst[i][j]);
        if (dst[i][j] == -1) {
          sp[i][j] = big;
        } else {
          sp[i][j] = dst[i][j];
        }
        if (i == j) {
          sp[i][j] = 0;
        }
      }
    }
    for(int i = 0; i < n; i++) {
      for(int j = 0; j < n; j++) {
        for(int k = 0; k < n; k++) {
          MIN(sp[j][k], sp[j][i] + sp[i][k]);
        }
      }
    }
    while(q--) {
      fill(dp, dp + n, big);
      int ss, st;
      scanf("%d%d", &ss, &st);
      ss--; st--;

      priority_queue<pair<double, int>, vector<pair<double, int>>, greater<pair<double, int>>> pq;
      dp[ss] = 0;
      pq.push(mp(dp[ss], ss));
      while(!pq.empty()) {
        double cost = pq.top().fi;
        int u = pq.top().se;
        //cout << cost << " " << u << endl;
        pq.pop();
    
        if (dp[u] == cost) {
          for(int v = 0; v < n; v++) {
            if (u == v || sp[u][v] > horse[u].fi)
              continue;
            double extra = 1.0 * sp[u][v] / horse[u].se;
            if (cost + extra < dp[v]) {
              MIN(dp[v], cost + extra);
              pq.push(mp(dp[v], v));
            }
          }
        }
      }
      printf(" %.8lf", dp[st]);
    }
    printf("\n");




  }
}