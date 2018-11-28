#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

double solve(int N, int , double U, double *P) {
  sort(P, P+N);
  P[N] = 1.0;
  double x = P[0];
  for (int i = 1; i <= N; i++) {
    double y;
    if ((P[i]-x)*i >= U) {
      y = U / i;
    } else {
      y = P[i]-x;
    }
    for (int j = 0; j < i; j++) {
      P[j] += y;
    }
    U -= y*i;
    x = P[i];
  }
  double ans = 1.0;
  for (int i = 0; i < N; i++) {
    ans *= P[i];
  }
  return ans;
}

int main()
{
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    int N, K;
    cin >> N >> K;
    double U;
    cin >> U;
    double P[60];
    for (int i = 0; i < N; i++) {
      cin >> P[i];
    }
    double ans = solve(N, K, U, P);
    printf("Case #%d: %.13f\n", i+1, ans);
  }
}
