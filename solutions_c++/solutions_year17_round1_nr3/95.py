#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

#define pii pair<int, int>
#define ppi pair<pii, pii>

int hd,ad,hk,ak,b,d;
map<ppi, int> Map;
queue<ppi> q;

inline void solve () {
  Map.clear ();
  while (not q.empty ()) {
    q.pop ();
  }

  scanf ("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &b, &d);

  ppi u = ppi (pii (hd, ad), pii (hk, ak));
  Map[u] = 0;
  q.push (u);
  while (not q.empty ()) {
    u = q.front ();
    q.pop ();
    int c = Map[u];

    // printf ("( %d %d ) ( %d %d ) %d\n", u.first.first, u.first.second, u.second.first, u.second.second, c);

    if (u.second.first == 0) {
      printf ("%d\n", c);
      return;
    }
    if (u.first.first == 0) {
      continue;
    }

    c ++;
    // attack
    ppi v = u;
    v.second.first = max (0, v.second.first - v.first.second);
    v.first.first = max (0, v.first.first - v.second.second);
    if (Map.find (v) == Map.end ()) {
      Map[v] = c;
      q.push (v);
    }
    // buff
    v = u;
    v.first.second += b;
    v.first.first = max (0, v.first.first - v.second.second);
    if (Map.find (v) == Map.end ()) {
      Map[v] = c;
      q.push (v);
    }
    // cure
    v = u;
    v.first.first = hd;
    v.first.first = max (0, v.first.first - v.second.second);
    if (Map.find (v) == Map.end ()) {
      Map[v] = c;
      q.push (v);
    }
    // debuff
    v = u;
    v.second.second = max (0, v.second.second - d);
    v.first.first = max (0, v.first.first - v.second.second);
    if (Map.find (v) == Map.end ()) {
      Map[v] = c;
      q.push (v);
    }
  }
  printf ("IMPOSSIBLE\n");
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: ", i);
    solve ();
  }
}
