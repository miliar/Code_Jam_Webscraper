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

enum Color {
  R, O, Y, G, B, V
};

const string kColors {"ROYGBV"};

void HandleCase() {
  int n;
  scanf("%d", &n);
  vector<pair<int, char>> v;
  for (int i = 0; i < 6; ++i) {
    int c;
    scanf("%d", &c);
    v.push_back({c, kColors[i]});
  }
  //ryb, ogv
  sort(v.begin(), v.end());
  reverse(v.begin(), v.end());
  int mc = v[0].first;
  if (n - mc < mc) {
    puts("IMPOSSIBLE");
    return;
  }
  string ans;
  for (int i = 0; i < mc; ++i) {
    ans.push_back(v[0].second);
    if (i < v[1].first) {
      ans.push_back(v[1].second);
    }
    if (i + v[2].first >= mc) {
      ans.push_back(v[2].second);
    }
  }
  assert(len(ans) == n);
  for (int i = 0; i < n; ++i) {
    int j = (i + 1) % n;
    if (ans[i] == ans[j]) {
      fprintf(stderr, "%d = %d\n", i, j);
      throw 1;
    }
  }
  puts(ans.c_str());
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
