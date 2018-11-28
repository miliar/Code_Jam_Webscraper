#include <cstdio>

int D, N;

void p() {
  scanf("%d%d", &D, &N);
  float t_max = 0;
  for (int i = 0; i < N; i++) {
    int k, s;
    scanf("%d%d", &k, &s);
    float t = (float)(D-k)/s; // s/v -> min
    if (t > t_max) t_max = t; // ->min
  }
  printf("%f\n", D/t_max); // -> max
}

int main() {
  int T;
  scanf("%d", &T);
  for (int i = 1; i <= T; i++) {
    printf("CASE #%d: ", i);
    p();
  }
}
