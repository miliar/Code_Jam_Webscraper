#include <iostream>
#include <cmath>
#include <set>
using namespace std;

// (a + x) * (b + x) * (c + x)

int main() {
  int T, N, K;
  double U, sum, average, answer;
  scanf("%d", &T);
  for (int i = 0; i < T; i++) {
    scanf("%d%d", &N, &K);
    scanf("%lf", &U);
    double *P = new double[N];
    for (int j = 0; j < N; j++) {
      scanf("%lf", &P[j]);
      sum += P[j];
    }
    sort(P, P + N);
    int k = 0;
    double maxP, requiredP;
    do {
      requiredP = 0.0;
      k++;
      maxP = P[N - k];
      for (int j = 0; j < (N - k); j++) {
        requiredP += maxP - P[j];
      }
    } while (requiredP > U);
    
    for (int j = 0; j < (N - k); j++) {
      U -= P[N - k] - P[j];
      P[j] = P[N - k];
    }
    for (int j = 0; j < (N - k + 1); j++) {
      P[j] += U / (N - k + 1);
    }
    answer = 1.0;
    for (int j = 0; j < N; j++) answer *= P[j];
    printf("Case #%d: %lf\n", i + 1, answer);
  }
}