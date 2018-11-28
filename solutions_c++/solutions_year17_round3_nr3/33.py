#include <bits/stdc++.h>
using namespace std;

#undef DEBUG
#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

#define M(x) (((x%MOD)+MOD)%MOD)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef long double ld;

const ll MOD = (ll)(1e9)+7ll;
const ld EPS = 1e-6;

const int MAX_N = 55;

int N, K;
ld p[MAX_N];

int main() {
  int T;
  scanf("%d",&T);

  for (int z=1;z<=T;z++) {
    printf("Case #%d: ",z);

    scanf("%d %d",&N,&K);
    ld U;

    scanf("%Lf",&U);
    for (int i=0;i<N;i++) {
      scanf("%Lf",&p[i]);
    }
    sort(p, p+N);
    p[N] = 1.0;

    for (int i=1;i<=N && U > EPS;i++) {
      ld ii = i;
      ld req = (p[i] - p[i-1]) * ii;
      ld spend = min(req, U);
      for (int j=0;j<i;j++) {
        p[j] += spend / ii;
      }
      U -= spend;
    }

    ld prod = 1.0;
    for (int i=0;i<N;i++) {
      D("p[%d] = %Lf\n",i,p[i]);
      prod *= p[i];
    }
    printf("%.9Lf\n",prod);
  }
  return 0;
}
