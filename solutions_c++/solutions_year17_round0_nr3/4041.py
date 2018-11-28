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

const int MAX_N = 1e6+6;

int l[MAX_N];
int r[MAX_N];

void solve(int start, int end) {
  if (start <= end) {
    int mid = (start + end)/2;
    l[mid] = mid-start;
    r[mid] = end-mid;
    solve(start, mid-1);
    solve(mid+1, end);
  }
}

int main() {
    int T;
    scanf("%d",&T);

    for(int z=1;z<=T;z++) {
      printf("Case #%d: ",z);

      int N, K;
      scanf("%d %d",&N,&K);
      solve(0, N-1);

      vector< pair<pii, int> > v;
      for (int i=0;i<N;i++) {
        v.push_back({{min(l[i], r[i]), max(l[i], r[i])}, -i});
      }
      sort(v.begin(), v.end());
      reverse(v.begin(), v.end());
      printf("%d %d\n",v[K-1].first.second,v[K-1].first.first);
    }

    return 0;
}
