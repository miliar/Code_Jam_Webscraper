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

char s[1005];

int main() {
  int tc;
  scanf("%d",&tc);
  for(int i = 1; i <= tc; i++) {
    scanf("%s", s);
    int n = strlen(s);
    int k;
    scanf("%d", &k);
    printf("Case #%d: ", i);
    int ans = 0;
    for(int j = 0; j < n; j++) {
      if (s[j] == '-') {
        if (j <= n-k) {
          ans++;
          for(int kk = j; kk < j + k; kk++) {
            if (s[kk] == '+') {
              s[kk] = '-';
            } else {
              s[kk] = '+';
            }
          }
        } else {
          ans = -1;
          break;
        }
      }
    }
    if (ans == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }
}