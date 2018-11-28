#include <iostream>
#include <string>
#include <algorithm>

void print(int caseNum, double output) {
  std::cout << std::fixed << "Case #" << caseNum << ": " << output << std::endl;
}

int main() {
  int T;
  std::cin >> T;
  std::cout.precision(10);

  for (int t = 1; t <= T; ++t) {
    int N, K;
    std::cin >> N >> K;

    double U;
    std::cin >> U;

    double P[N];
    for (int n = 0; n < N; ++n) {
      std::cin >> P[n];
    }

    std::sort(P, P+N);

    for (int n = 0; n < N-1; ++n) {
      if (U <= 0.0) break;
      if (P[n] < P[n+1]) {
        if (U >= (P[n+1]-P[n])*(n+1)) {
          U -= (P[n+1]-P[n])*(n+1);
          for (int nn = 0; nn <= n; ++nn) {
            P[nn] = P[n+1];
          }
        } else {
          for (int nn = 0; nn <= n; ++nn) {
            P[nn] += U / (n+1);
          }
          U = 0.0;
        }
      }
    }

    double prop = 1.0;
    if (U > 0.0) {
      for (int n = 0; n < N; ++n) {
        prop *= P[n]+(U/N);
      }
    } else {
      for (int n = 0; n < N; ++n) {
        prop *= P[n];
      }
    }

    print(t, prop);
  }

  return 0;
}
