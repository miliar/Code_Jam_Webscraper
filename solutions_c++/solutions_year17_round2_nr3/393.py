#include <cstdio>
#include <cassert>
#include <cmath>
#include <vector>
#include <cstring>


using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

void solve() {
  int n, q;
  scanf("%d%d", &n, &q);
  vector<int> e(n), s(n);
  vector<vector<long double>> w(n, vector<long double>(n));
  vector<vector<long double>> r(n, vector<long double>(n, 1. / 0.));
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &e[i], &s[i]);
  }

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      int x;
      scanf("%d", &x);
      if (x == -1) {
        w[i][j] = 1. / 0.;
      } else {
        w[i][j] = x;
      }
      w[i][i] = 0;
    }
  }

  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
          w[i][j] = min(w[i][j], w[i][k] + w[k][j]);
      }
    }
  }
  for (int i = 0; i < n; i++) r[i][i] = 0.;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      if (w[i][j] == -1) w[i][j] = (int)1e9 + 2;
      if (e[i] >= w[i][j]) {
        r[i][j] = 1. * w[i][j] / s[i];
        assert(r[i][j] >= 0.);
      }
    }
  }
  for (int k = 0; k < n; k++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        r[i][j] = min(r[i][j], r[i][k] + r[k][j]);
      }
    }
  }
  for (int it = 0; it < q; it++) {
    int a, b;
    scanf("%d%d", &a, &b);
    a--, b--;
    printf("%.10lf%c", (double)r[a][b], " \n"[it + 1 == q]);
  }
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    printf("Case #%d: ", test);
    solve();
  }
}
