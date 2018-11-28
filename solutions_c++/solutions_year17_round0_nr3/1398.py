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
  li n, k;
  scanf("%lld%lld", &n, &k);
  map<li, li> q;
  q.insert({-n, 1});
  for (li done = 0; done < k; ) {
    auto start = q.begin();
    li w = -start->first;
    li c = start->second;
    q.erase(start);
    li rg = w / 2;
    li lf = w - rg - 1;
    //fprintf(stderr, "w %lld, c %lld: %lld %lld\n", w, c, lf, rg);
    if (done + c >= k) {
      printf("%lld %lld\n", max(lf, rg), min(lf, rg));
      return;
    }
    if (lf)
      q[-lf] += c;
    if (rg)
      q[-rg] += c;
    done += c;
  }
  throw 1;
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
