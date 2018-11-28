#include <set>
#include <queue>
#include <cstdio>
#include <iostream>

using namespace std;

int Hd, Ad, Hk, Ak, B, D;

struct State {
  int dist;
  int hd, ad, hk, ak;

  bool operator<(const State &s) const {
    if (hd != s.hd) return hd < s.hd;
    if (ad != s.ad) return ad < s.ad;
    if (hk != s.hk) return hk < s.hk;
    if (ak != s.ak) return ak < s.ak;
    return false;
  }
};

int solve() {
  cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
  queue<State> q;
  State initial = {0, Hd, Ad, Hk, Ak};
  set<State> inQ;
  inQ.insert(initial);
  q.push(initial);
  while (!q.empty()) {
    State p = q.front();
    q.pop();
    if (p.ad >= p.hk) {
      return p.dist + 1;
    }
    // 1
    State sA = {p.dist+1, p.hd - p.ak, p.ad, max(0, p.hk - p.ad), p.ak};
    if (sA.hd > 0 && !inQ.count(sA)) {
      inQ.insert(sA);
      q.push(sA);
    }
    // 1
    State sB = {p.dist+1, p.hd - p.ak, p.ad + B, p.hk, p.ak};
    if (sB.hd > 0 && !inQ.count(sB)) {
      inQ.insert(sB);
      q.push(sB);
    }
    // 2
    State sC = {p.dist+1, Hd - p.ak, p.ad, p.hk, p.ak};
    if (sC.hd > 0 && !inQ.count(sC)) {
      inQ.insert(sC);
      q.push(sC);
    }
    // 3
    int nd = max(0, p.ak - D);
    State sD = {p.dist+1, p.hd - nd, p.ad, p.hk, nd};
    if (sD.hd > 0 && !inQ.count(sD)) {
      inQ.insert(sD);
      q.push(sD);
    }
  }
  return -1;
}

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    printf("Case #%d: ", i);
    int ans = solve();
    if (ans == -1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", ans);
  }
}
