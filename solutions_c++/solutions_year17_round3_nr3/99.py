#include <bits/stdc++.h>
using namespace std;

#define PI 3.1415926535

int T;
int N;
int K;
double U;
double P[114514];

int main() {
  scanf("%d", &T);
  for (int Case=1; Case<=T; Case++) {
    scanf("%d%d", &N, &K);
    scanf("%lf", &U);

    map<double, int> ps;
    for (int i=0; i<N; i++) {
      scanf("%lf", &P[i]);
    }
    sort(P, P+N);

    P[N] = 1;
    for (int i=0; i<N; i++) {
      if (U < (P[i+1]-P[i])*(i+1)) {
        for (int j=0; j<=i; j++) {
          P[j] = P[i]+U/(i+1);
        }
        break;
      }
     
      U -= (P[i+1]-P[i])*(i+1);
      for (int j=0; j<=i; j++) {
        P[j] = P[i+1];
      }
    }

    double ans = 1.0;
    for (int i=0; i<N; i++) ans *= P[i];

    printf("Case #%d: %.10f\n", Case, ans);
  }
}
