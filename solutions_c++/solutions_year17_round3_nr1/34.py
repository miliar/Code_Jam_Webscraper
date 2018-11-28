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
typedef pair<ld,ld> pd;

const ll MOD = (ll)(1e9)+7ll;
const int MAX_N = 1005;

int N, K;
pd pancakes[MAX_N];

int main() {
  int T;
  scanf("%d",&T);

  for (int z=1;z<=T;z++) {
    printf("Case #%d: ",z);

    scanf("%d %d",&N,&K);
    for (int i=0;i<N;i++) {
      ld r, h;
      scanf("%Lf %Lf",&r,&h);
      pancakes[i].first = M_PI * r * r;
      pancakes[i].second = 2.0 * M_PI * r * h;
      D("pancake (r=%Lf,h=%Lf) = {%Lf,%Lf}\n",r,h,pancakes[i].first,pancakes[i].second);
    }

    sort(pancakes, pancakes+N);

    ld ans = 0.0;
    priority_queue< ld, vector<ld>, greater<ld> > pq;
    ld tot = 0.0;
    for (int i=0;i<N;i++) {
      while (pq.size() + 1 > K && pq.top() < pancakes[i].second) {
        tot -= pq.top();
        pq.pop();
      }
      ld here;
      if (pq.size() + 1 <= K) {
        tot += pancakes[i].second;
        pq.push(pancakes[i].second);
        here = tot + pancakes[i].first;
      } else {
        here = tot + pancakes[i].first - pq.top() + pancakes[i].second;
      }
      ans = max(ans, here);
      D("i=%d, here=%Lf, tot=%Lf\n",i,here,tot);
    }
    printf("%.9Lf\n",ans);
  }
  return 0;
}
