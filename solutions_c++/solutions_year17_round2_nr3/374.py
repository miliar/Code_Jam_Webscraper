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
  int n, q;
  scanf("%d%d", &n, &q);
  vector<int> e(n), s(n);
  for (int i = 0; i < n; ++i) {
    scanf("%d%d", &e[i], &s[i]);
  }
  vector<vector<int>> d1(n, vector<int>(n));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      scanf("%d", &d1[i][j]);
    }
  }
  vector<vector<ld>> d2(n, vector<ld>(n));
  vector<int> d3(n);
  vector<bool> used(n);
  for (int start = 0; start < n; ++start) {
    for (int i = 0; i < n; ++i) {
      d3[i] = -1;
      used[i] = false;
    }
    d3[start] = 0;
    while (true) {
      int v = -1;
      for (int i = 0; i < n; ++i) {
        if (!used[i] && d3[i] >= 0 && (v == -1 || d3[v] > d3[i])) {
          v = i;
        }
      }
      if (v == -1) break;
      used[v] = true;
      for (int to = 0; to < n; ++to) {
        int w = d1[v][to];
        if (w == -1) continue;
        int nval = d3[v] + w;
        if (nval > e[start]) continue;
        if (d3[to] == -1 || d3[to] > nval) {
          d3[to] = nval;
        }
      }
    }
    ld denom = s[start];
    for (int i = 0; i < n; ++i) {
      if (d3[i] == -1 || i == start) {
        d2[start][i] = -1;
      } else {
        d2[start][i] = d3[i] / denom;
        //fprintf(stderr, "time from %d to %d: %.9lf\n", start, i, double(d2[start][i]));
      }
    }
  }
  vector<ld> d4(n);
  for (int it = 0; it < q; ++it) {
    int start, end;
    scanf("%d%d", &start, &end);
    --start, --end;
    for (int i = 0; i < n; ++i) {
      d4[i] = -1;
      used[i] = false;
    }
    d4[start] = 0;
    while (true) {
      int v = -1;
      for (int i = 0; i < n; ++i) {
        if (!used[i] && d4[i] > -0.5 && (v == -1 || d4[v] > d4[i])) {
          v = i;
        }
      }
      if (v == -1) break;
      used[v] = true;
      for (int to = 0; to < n; ++to) {
        ld w = d2[v][to];
        if (w < -0.5) continue;
        ld nval = d4[v] + w;
        if (d4[to] < -0.5 || d4[to] > nval) {
          d4[to] = nval;
        }
      }
    }
    assert(d4[end] > EPS);
    printf("%.9lf ", double(d4[end]));
  }
  puts("");
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
