#include <bits/stdc++.h>

using namespace std;

float P[1001];

int main() {
  int TTT;
  scanf("%d", &TTT);
  for (int TT = 1; TT <= TTT; TT++) {
    printf("Case #%d: ", TT);
    // only works for N=K
    int N, K;
    float U;
    scanf("%d%d%f", &N, &K, &U);
    for (int i = 0; i < N; i++) scanf("%f", P+i);
    sort(P, P+N);
    P[N] = 1;
    for (int i = 0; i < N; i++) {
      int num = i+1;
      float u = min(U/num, P[i+1]-P[i]);
      if (u < 0) break;
      U -= num*u;
      for (int j = 0; j <= i; j++) P[j] += u;
    }
    float chance = 1;
    for (int i = 0; i < N; i++) if (P[i] <= 1.0) chance *= P[i];
    printf("%f\n", chance);
  }
}
