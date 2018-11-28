#include <iostream>
#include <string>

void print(int caseNum, double output) {
  std::cout << std::fixed << "Case #" << caseNum << ": " << output << std::endl;
}

int main() {
  int T;
  scanf("%d", &T);

  for (int t = 1; t <= T; ++t) {
    long D, N;
    scanf("%ld %ld", &D, &N);

    double maxTime = 0.0;
    for (int n = 0; n < N; ++n) {
      long K, S;
      scanf("%ld %ld", &K, &S);
      double time = (1.0 * (D-K)) / S;
      if (time > maxTime) {
        maxTime = time;
      }
    }

    print(t, (1.0 * D) / maxTime);
  }

  return 0;
}
