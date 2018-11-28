#include <cstdio>
#include <algorithm>

std::pair<int, int> RH[1001];
double X[1001];

int main() {
  int T = 1, TT;
  scanf("%d", &TT);
  while (T <= TT) {
    printf("Case #%d: ", T);
    T++;
    int N, K;
    scanf("%d%d", &N, &K);
    for (int i = 0; i < N; i++) scanf("%d%d", &(RH[i].first), &(RH[i].second));
    for (int i = 0; i < N; i++) RH[i].second = -2*RH[i].second;
    std::sort(RH, RH+N);
    double max_sum = 0;
    // 11 12 21 22
    for (int i = K-1; i < N; i++) { // [0,i) left
      double sum = 0;
      // we choose i as the bottom
      sum += 1.0*RH[i].first*RH[i].first - 1.0*RH[i].second * RH[i].first;
      for (int j = 0; j < i; j++) {
        X[j] = -1.0*RH[j].first * RH[j].second;
      }
      std::sort(X, X+i);
      for (int k = i-K+1; k < i; k++) { // (i-K,i) -> K-1 elements
        sum += X[k];
      }
      if (max_sum < sum) max_sum = sum;
    }
    max_sum *= 3.141592654;

    printf("%f\n", max_sum);
  }
}
