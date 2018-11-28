#include <bits/stdc++.h>
using namespace std;

int T, C = 1;
long long N, K;

struct node {
  long long l, r;
  node(long long _l, long long _r): 
    l(_l), r(_r) {}

  bool operator<(const node& _n) const {
    return (r - l - 1) == (_n.r - _n.l - 1) ? (l > _n.l) : (r - l - 1) < (_n.r - _n.l - 1);
  }
};


int main() {
	freopen("../in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
  for(scanf("%d", &T); T--; ++C) {
    scanf("%lld %lld", &N, &K);
    printf("Case #%d: ", C);
    map<long long, long long> mp1;
    --N, --K, mp1[N / 2] = 1; mp1[N - N / 2] += 1;
    pair<long long, long long> ans({N / 2, N - N / 2});
    while(K) {
      if(!mp1.size()) { ans = {0, 0}; break; }
      auto it = mp1.begin();
      long long f = it->first, fc = it->second, s = -1, sc = -1;
      if((++it) != mp1.end()) {
        s = it->first;
        sc = it->second;
      }
      assert(mp1.size() <= 2);
      mp1.clear();
      if(s > 0 && K) {
        K -= min(K, sc);  
        s--;
        if(s / 2) mp1[s / 2] += sc;
        if(s - s / 2) mp1[s - s / 2] += sc;
        ans = {s / 2, s - s / 2};
      }

      if(f > 0 && K) {
        K -= min(K, fc);
        f--;
        if(f / 2) mp1[f / 2] += fc;
        if(f - f / 2) mp1[f - f / 2] += fc;
        ans = {f / 2, f - f / 2};
      }
    }

    if(ans.first < ans.second) swap(ans.first, ans.second);
    printf("%lld %lld\n", ans.first, ans.second);
  }
}