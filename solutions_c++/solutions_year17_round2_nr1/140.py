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

int dst[1005];
int spd[1005];

int main() {
  int t = 0;
  scanf("%d", &t);
  while(t--) {
    static int tc; tc++;
    printf("Case #%d: ", tc);
    double ans = 1e18;
    int d, n;
    scanf("%d%d", &d, &n);
    for(int i = 0; i < n; i++) {
      scanf("%d%d", &dst[i], &spd[i]);
    }
    dst[n] = d;

    for(int i = 0; i <= n; i++) {
      for(int j = 0; j < n; j++) {
        if (dst[j] < dst[i]) {
          MIN(ans,d / (1.0*(dst[i]-dst[j]) / spd[j]));
        }
      }
    }
    printf("%.8lf\n", ans);
  }
}