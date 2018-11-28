#include <cstdio>
#include <cassert>
#include <cmath>
#include <vector>
#include <cstring>


using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)

void solve() {
  int d, n;
  scanf("%d%d", &d, &n);
  vector<int> k(n), s(n);
  vector<int> p(n);
  for (int i = 0; i < n; i++) {
    scanf("%d%d", &k[i], &s[i]);
    p[i] = i;
  }
  double res = 0.;
  for (int i = 0; i < n; i++) {
    res = max(res, 1. * (d - k[i]) / s[i]);
  }
  printf("%.20le\n", d / res);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; test++) {
    printf("Case #%d: ", test);
    solve();
  }
}
