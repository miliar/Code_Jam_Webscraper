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

bool Good(li t) {
  li prev = 9;
  while (t) {
    li d = t % 10;
    if (d > prev) {
      fprintf(stderr, "d %lld, prev %lld\n", d, prev);
      return false;
    }
    prev = d;
    t /= 10;
  }
  return true;
}

void HandleCase() {
  li n;
  scanf("%lld", &n);
  vector<int> v;
  li t = n;
  int total = 0;
  while (t) {
    int d = int(t % 10);
    v.push_back(d);
    t /= 10;
    ++total;
  }
  reverse(v.begin(), v.end());
  int id = -1;
  for (int i = 0; i + 1 < len(v); ++i) {
    if (v[i] > v[i + 1]) {
      id = i;
      break;
    }
  }
  if (id == -1) {
    assert(Good(n));
    printf("%lld\n", n);
    return;
  }
  if (v[id] == 1) {
    li ans = 0;
    for (int i = 0; i < total - 1; ++i) {
      ans = ans * 10 + 9;      
    }
    assert(ans <= n && Good(ans));
    printf("%lld\n", ans);
    return;
  }
  while (id && v[id - 1] == v[id])
    --id;
  --v[id];
  assert(v[id]);
  for (int i = id + 1; i < len(v); ++i) {
    v[i] = 9;
  }
  li ans = 0;
  for (int d : v) {
    ans = ans * 10 + d;
  }
  //fprintf(stderr, "%d: %lld\n", __LINE__, ans);
  assert(ans <= n && Good(ans));
  printf("%lld\n", ans);
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
