#include <bits/stdc++.h>
using namespace std;
#define FOR(i, n) for(int i = 1; i <= n; i++)
#define REP(i, n) for(int i = 0; i < n; i++)
#define MP make_pair
#define FI first
#define SE second
#define VI vector<int>
#define CLR(x) memset(x, 0, sizeof(x))
#define SZ(x) (x.size())
#ifdef QWERTIER
#define err(x) cerr<<x<<endl;
#else
#define err(x)
#endif
typedef long long LL;


LL n, k;
int main() {
#ifdef QWERTIER
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    scanf("%lld%lld", &n, &k);
    printf("Case #%d: ", kase);
    map<LL, LL> cnt;
    cnt[n] = 1;
    // printf("%lld %lld\n", cnt.begin()->FI, cnt.rbegin().base()->FI);
    while (k > 0) {
      pair<LL, LL> cur = *cnt.rbegin();
      // printf("%lld\n", cnt.rbegin().base()->FI);
      // return 0;
      cnt.erase(cur.FI);
      // cur.FI/2, (cur.FI+1)/2
      if (k <= cur.SE) {
        printf("%lld %lld\n", (cur.FI-1+1)/2, (cur.FI-1)/2);
        break;
      }
      k -= cur.SE;
      cnt[(cur.FI-1+1)/2]+=cur.SE;
      cnt[(cur.FI-1)/2]+=cur.SE;
    }
  }
  return 0;
}
