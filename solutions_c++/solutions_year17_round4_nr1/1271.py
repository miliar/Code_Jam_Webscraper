#include <bits/stdc++.h>

using namespace std;

template<class T> inline T sqr(const T& a) {
  return a * a;
}

template<class T> inline int len(const T &c) {
  return static_cast<int>(c.size());
}

template<class T> inline bool maximize(T &r, const T c) {
  if (r < c) {
    r = c;
    return true;
  }
  return false;
}

template<class T> inline bool minimize(T &r, const T c) {
  if (r > c) {
    r = c;
    return true;
  }
  return false;
}

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

const ld EPS = 1e-9;
const ld PI = 2 * acos(0.0);
const int N = 100;

void HandleCase() {
  int n, p;
  scanf("%d%d", &n, &p);
  vector<int> c(p, 0);
  for (int i = 0; i < n; ++i) {
    int x;
    scanf("%d", &x);
    ++c[x % p];
  }
  int ans = c[0];
  if (p == 2) {
    ans += c[1] - c[1] / 2;
  } else if (p == 3) {
    int t = min(c[1], c[2]);
    ans += t;
    c[1] -= t;
    c[2] -= t;
    if (c[1]) {
      ans += c[1] / 3;
      if (c[1] % 3) {
        ++ans;
      }
    } else if (c[2]) {
      ans += c[2] / 3;
      if (c[2] % 3) {
        ++ans;
      }
    }
  } else if (p == 4) {
    int t = c[2] / 2;
    ans += t;
    c[2] -= t * 2;
    t = min(c[1], c[3]);
    ans += t;
    c[1] -= t;
    c[3] -= t;
    if (c[2] && c[1]) {
      if (c[1] >= 2) {
        ++ans;
        --c[2];
        c[1] -= 2;
        if (c[1]) {
          ans += c[1] / 4;
          if (c[1] % 4) {
            ++ans;
          }
        }
      } else {
        ++ans;
      }
    } else if (c[2] && c[3]) {
      if (c[3] >= 2) {
        ++ans;
        --c[2];
        c[3] -= 2;
        if (c[3]) {
          ans += c[3] / 4;
          if (c[3] % 4) {
            ++ans;
          }
        }
      } else {
        ++ans;
      }
    } else if (c[2]) {
      ++ans;
    } else if (c[1]) {
      ans += c[1] / 4;
      if (c[1] % 4) {
        ++ans;
      }
    } else if (c[3]) {
      ans += c[3] / 4;
      if (c[3] % 4) {
        ++ans;
      }
    }
  } else {
    throw 1;
  }
  printf("%d\n", ans);
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
