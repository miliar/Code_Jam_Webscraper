#include <cstdio>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
#define REP(i, N) for (int i = 0; i < N; i++)
#define FOR(i, a, b) for (int i = a; i <= b; i++)
typedef pair<int, int> pii;

int T, Hd, Ad, Hk, Ak, B, D;
struct state {
  int hd, ad, hk, ak;
  bool operator <(const state& o) const {
    return topair() < o.topair();
  }
  pair<pii,pii> topair() const {
    return make_pair(pii(hd,ad), pii(hk, ak));
  }
};

state attack(state x) {
  state y = x;
  y.hk -= x.ad;
  y.hd -= x.ak;
  return y;
}
state buff(state x) {
  state y = x;
  y.ad += B;
  y.hd -= y.ak;
  return y;
}
state cure(state x) {
  state y = x;
  y.hd = Hd;
  y.hd -= y.ak;
  return y;
}
state debuff(state x) {
  state y = x;
  y.ak = max(0, y.ak - D);
  y.hd -= y.ak;
  return y;
}

int main() {
  scanf("%d", &T);
  FOR(cn, 1, T) {
    printf("Case #%d: ", cn);
    scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);

    set<state> done;
    queue<pair<state, int> > Q;
    Q.push({{Hd, Ad, Hk, Ak}, 0});
    int ans = -1;
    while (!Q.empty()) {
      auto x = Q.front(); Q.pop();
      state s = x.first;
      int d = x.second;
      if (d > 1000) break;
      if (s.ad >= s.hk) {
        ans = d + 1;
        break;
      }
      state at = attack(s);
      state bu = buff(s);
      state cu = cure(s);
      state de = debuff(s);
      if (at.hd > 0 && !done.count(at)) { done.insert(at); Q.push({at, d+1}); }
      if (bu.hd > 0 && !done.count(bu)) { done.insert(bu); Q.push({bu, d+1}); }
      if (cu.hd > 0 && !done.count(cu)) { done.insert(cu); Q.push({cu, d+1}); }
      if (de.hd > 0 && !done.count(de)) { done.insert(de); Q.push({de, d+1}); }
    }
    if (ans == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }
  return 0;
}
