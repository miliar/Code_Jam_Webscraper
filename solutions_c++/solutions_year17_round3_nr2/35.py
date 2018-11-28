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
const int INF = (1 << 29);

const int MINS = 24 * 60;
const int MAX_T = MINS + 105;
const int OFFSET = MINS+3;

int block[MAX_T];
int cache[2][MAX_T][MAX_T*2][2];

int main() {
  int T;
  scanf("%d",&T);

  for (int z=1;z<=T;z++) {
    printf("Case #%d: ",z);

    fill(block, block+MAX_T, 0);

    for(int k=0;k<2;k++) {
      for(int t=0;t<MAX_T;t++) {
        for (int i=0;i<MAX_T*2;i++) {
          for(int j=0;j<2;j++) {
            cache[k][t][i][j] = INF;
          }
        }
      }
    }
    for (int i=0;i<2;i++) {
      cache[i][MINS][OFFSET][i] = 0;
    }

    int A, B;
    scanf("%d %d",&A,&B);

    for (int i=0;i<A+B;i++) {
      int s, e;
      scanf("%d %d",&s,&e);
      for (int j=s;j<e;j++) {
        if (i < A) {
          block[j] = -1;
        } else {
          block[j] = 1;
        }
      }
    }

    for (int k=0;k<2;k++) {
      for (int t=MINS-1;t>=0;t--) {
        int b = block[t];
        for (int off=OFFSET-MINS;off<=OFFSET+MINS;off++) {
          for (int p=0;p<2;p++) {
            int pp = (p*2) - 1;
            // Same
            if (b != pp) {
              cache[k][t][off][p] = min(cache[k][t][off][p],
                  cache[k][t+1][off + pp][(pp+1)/2]);
            }
            // Swap
            if (b != (-pp)) {
              cache[k][t][off][p] = min(cache[k][t][off][p],
                  cache[k][t+1][off - pp][(1-pp)/2] + 1);
            }
          }
        }
      }
    }
    int ans = INF;
    for (int i=0;i<2;i++) {
      ans = min(ans, cache[i][0][OFFSET][i]);
    }
    printf("%d\n",ans);
  }
  return 0;
}
