#include <bits/stdc++.h>
using namespace std;

#define PI 3.1415926535

int T;
int N;
int K;
double R[114514];
double H[114514];

int main() {
  scanf("%d", &T);
  for (int Case=1; Case<=T; Case++) {
    scanf("%d%d", &N, &K);
    for (int i=0; i<N; i++) {
      scanf("%lf%lf", &R[i], &H[i]);
    }

    double ans = 0;
    for (int i=0; i<N; i++) {
      vector<double> cand;

      for (int j=0; j<N; j++) {
        if (R[j] > R[i]) continue;
        if (i == j) continue;
        cand.emplace_back(2*PI*R[j]*H[j]);
      }

      if (cand.size() < K-1) continue;

      sort(cand.begin(), cand.end(), greater<double>());
      double t = PI * R[i] * R[i] + 2*PI*R[i]*H[i];
      for (int j=0; j<K-1; j++) {
        t += cand[j];
      }
      ans = max(ans, t);
    }

    printf("Case #%d: %.10f\n", Case, ans);
  }
}
