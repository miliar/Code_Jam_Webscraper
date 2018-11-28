#include <bits/stdc++.h>
using namespace std;

#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

#define M(x) (((x%MOD)+MOD)%MOD)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const ll MOD = (ll)(1e9)+7ll;

const int MAX_N = 1e3+6;

int N, K;
char buf[MAX_N];
bool side[MAX_N];

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
      scanf(" %s %d ",buf,&K);
      N = strlen(buf);

      for (int i=0;i<N;i++) {
        side[i] = (buf[i] == '+');
      }

      int ans = 0;
      bool pos = true;
      for (int i=0;i<N;i++) {
        if (!side[i]) {
          if (i+K <= N) {
            ans++;
            for (int j=0;j<K;j++) {
              side[i+j] = !side[i+j];
            }
          } else {
            pos = false;
          }
        }
      }
      printf("Case #%d: ",z);
      if (pos) {
        printf("%d\n",ans);
      } else {
        printf("IMPOSSIBLE\n");
      }
    }

    return 0;
}
