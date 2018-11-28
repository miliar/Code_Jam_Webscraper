#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);
#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

int N, R, O, Y, G, B, V;
const int maxN = 11111;

void foo(char c1, int t) {
  char c2;
  if (c1 == 'R') c2 = 'G';
  if (c1 == 'Y') c2 = 'V';
  if (c1 == 'B') c2 = 'O';
  printf("%c", c1);
  while (t--) {
    printf("%c%c", c2, c1);
  }
}

bool first[3];

void bar(int i, pair<int, pair<char,int>> p) {
  if (first[i]) {
    foo(p.second.first, p.second.second);
  } else {
    printf("%c", p.second.first);
  }
  first[i] = false;
}

bool solve() {
  if (O == B && O + B == N) {
    for (int i = 1; i <= O; ++i) {
      printf("OB");
    }
    printf("\n");
    return true;
  }

  if (G == R && G + R == N) {
    for (int i = 1; i <= G; ++i) {
      printf("GR");
    }
    printf("\n");
    return true;
  }

  if (V == Y && V + Y == N) {
    for (int i = 1; i <= Y; ++i) {
      printf("VY");
    }
    printf("\n");
    return true;
  }

  if (O != 0 && O >= B) {
    return false;
  }
  if (G != 0 && G >= R) {
    return false;
  }
  if (V != 0 && V >= Y) {
    return false;
  }
  vector<pair<int, pair<char,int>>> ps;

  ps.push_back({R-G, {'R', G}});
  ps.push_back({Y-V, {'Y', V}});
  ps.push_back({B-O, {'B', O}});

  sort(ps.begin(), ps.end());
  reverse(ps.begin(), ps.end());
  if (ps[1].first + ps[2].first < ps[0].first) {
    return false;
  }
  first[0] = first[1] = first[2] = true;
  int couple = ps[1].first + ps[2].first - ps[0].first;
  for (int i = 0; i < ps[0].first; ++i) {
    bar(0, ps[0]);
    if (i < couple) {
      bar(1, ps[1]);
      bar(2, ps[2]);
    } else if (i < ps[1].first) {
      bar(1, ps[1]);
    } else {
      bar(2, ps[2]);
    }
  }
  printf("\n");

  return true;
}

int main() {
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    rd(N, R, O, Y, G, B, V);
    printf("Case #%d: ", tt);
    if (!solve()) {
      puts("IMPOSSIBLE");
    }
  }
  return 0;
}
