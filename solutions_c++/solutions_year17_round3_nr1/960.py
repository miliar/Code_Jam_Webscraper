#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <cmath>
using namespace std;

int R[1010], H[1010], order[1010];
double f[1010][1010];
double pi = acos(-1);
int main() {
  int tt;
  cin >> tt;
  for (int tcas = 1; tcas <= tt; tcas++) {
    int N, K;
    cin >> N >> K;
    f[0][0] = 0;
    for (int i = 1; i <= N; i++) {
      cin >> R[i] >> H[i];
      f[i][0] = 0;
      f[0][i] = 0;
      order[i] = i;
    }
    sort(order + 1, order + N + 1, [](int i, int j) {
      return R[i] > R[j];
    });
    for (int i = 1; i <= N; i++) {
      int cur = order[i];
      for (int k = 1; k <= i; k++) {
        f[i][k] = f[i-1][k];
        double val = 2 * pi * R[cur] * H[cur];
        if (k == 1) val += pi * R[cur] * R[cur];
        f[i][k] = max(f[i][k], f[i-1][k-1] + val);
      }
    }
    cout << "Case #" << tcas << ": ";
    printf("%.9lf\n", f[N][K]);
  }
}
