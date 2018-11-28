#include <algorithm>
#include <cassert>
#include <cstdio>
#include <vector>
using namespace std;

double const kEps = 1e-9;

double Solve(int n, int k, double u, vector<double> ps) {
  assert(n == k);

  sort(ps.begin(), ps.end());
  ps.push_back(1.0);

  double prev = ps[0];
  for (int i = 1; i <= n; ++i) {
    double const curr = ps[i];

    double const delta = curr - prev;
    double const spend = min(i * delta, u);
    double const single = spend / i;

    for (int j = 0; j < i; ++j)
      ps[j] += single;

    prev = curr;
    u -= spend;
  }

  double result = 1.0;
  for (int i = n; i >= 0; --i)
    result *= ps[i];
  return result;
}

int main() {
  int numTests;
  scanf("%d", &numTests);
  for (int testNum = 1; testNum <= numTests; ++testNum) {
    int n, k;
    double u;
    scanf("%d%d%lf", &n, &k, &u);

    vector<double> ps(n);
    for (int i = 0; i < n; ++i)
      scanf("%lf", &ps[i]);
    printf("Case #%d: %.6lf\n", testNum, Solve(n, k, u, ps));
  }
  return 0;
}
