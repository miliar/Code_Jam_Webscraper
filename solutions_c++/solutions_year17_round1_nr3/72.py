#include <bits/stdc++.h>

using namespace std;

struct A {
  int h1, h2, a1, a2;
  friend bool operator<(const A& x, const A& y) {
    auto t1 = make_pair(make_pair(x.h1, x.h2), make_pair(x.a1, x.a2));
    auto t2 = make_pair(make_pair(y.h1, y.h2), make_pair(y.a1, y.a2));
    return t1 < t2;
  }
};

int main(int argc, const char* argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    int hd, ad, hk, ak, b, d;
    cin >> hd >> ad >> hk >> ak >> b >> d;
    map<A, int> mp;
    mp[A{hd, hk, ad, ak}] = 1;
    queue<A> q;
    q.push(A{hd, hk, ad, ak});
    int ans = -1;
    while (!q.empty()) {
      auto x = q.front();
      q.pop();
      auto y = x;
      y.h2 -= y.a1;
      if (y.h2 <= 0) {
        ans = mp[x] + 1;
        break;
      }
      y.h1 -= y.a2;
      if (y.h1 > 0 && !mp[y]) {
        mp[y] = mp[x] + 1;
        q.push(y);
      }

      y = x;
      y.a1 += b;
      y.h1 -= y.a2;
      if (y.h1 > 0 && !mp[y]) {
        mp[y] = mp[x] + 1;
        q.push(y);
      }

      y = x;
      y.h1 = hd;
      y.h1 -= y.a2;
      if (y.h1 > 0 && !mp[y]) {
        mp[y] = mp[x] + 1;
        q.push(y);
      }

      y = x;
      y.a2 -= d;
      y.a2 = max(y.a2, 0);
      y.h1 -= y.a2;
      if (y.h1 > 0 && !mp[y]) {
        mp[y] = mp[x] + 1;
        q.push(y);
      }
    }
    printf("Case #%d: ", cas);
    ans == -1 ? puts("IMPOSSIBLE") : printf("%d\n", ans - 1);
  }
  return 0;
}
