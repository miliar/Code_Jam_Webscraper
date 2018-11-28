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


#define N 1010
int n, c, m, p[N], b[N];
multiset<int> st[3];
int proc(multiset<int> &s, multiset<int> &t) {
  int res = 0;
  while (s.size() > 0) {
    int x = *s.begin();
    if (t.upper_bound(x) != t.end()) {
      int y = *t.upper_bound(x);
      s.erase(s.lower_bound(x));
      t.erase(t.lower_bound(y));
      res++;
    } else
      break;
  }
  return res;
}
int main() {
#ifdef QWERTIER
  // freopen("in.txt", "r", stdin);
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("B-small-attempt0.out", "w", stdout);
  // freopen("-large.in", "r", stdin);
  // freopen("-large.out", "r", stdin);
#endif
  int T;
  scanf("%d", &T);
  FOR (kase, T) {
    printf("Case #%d: ", kase);
    scanf("%d%d%d", &n, &c, &m); // seats, customers, tickets
    st[1].clear();
    st[2].clear();
    FOR (i, m) {
      scanf("%d%d", &p[i], &b[i]);
      st[b[i]].insert(p[i]);
    }
    int ans = 0;
    ans += proc(st[1], st[2]);
    ans += proc(st[2], st[1]);
    if (st[1].size() > 0 && st[2].size() > 0) {
      if (*st[1].begin() == 1) {
        printf("%d %d\n", ans + st[1].size() + st[2].size(), 0);
        // puts("1");

      } else {
        printf("%d %d\n", ans + max(st[1].size(), st[2].size()), min(st[1].size(), st[2].size()));
        // puts("2");
      }
    } else {
      printf("%d %d\n", ans + st[1].size() + st[2].size(), 0);
      // puts("3");
    }
  }
  return 0;
}
