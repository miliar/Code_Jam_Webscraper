#include <bits/stdc++.h>

using namespace std;

template<class T> inline T sqr(const T& a) {
  return a * a;
}

template<class T> inline T middle(const T &a, const T &b) {
  return (a + b) / 2;
}

template<class T> inline int len(const T &c) {
  return static_cast<int>(c.size());
}

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 100;

void HandleCase() {
  int d, n;
  scanf("%d%d", &d, &n);
  vector<int> k(n), s(n);
  ld maxt = 0;
  for (int i = 0; i < n; ++i) {
    scanf("%d%d", &k[i], &s[i]);
    ld cur = ld(d - k[i]) / s[i];
    maxt = max(maxt, cur);
  }
  printf("%.9lf\n", double(d / maxt));
}

int main() {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    HandleCase();
  }
  return 0;
}
