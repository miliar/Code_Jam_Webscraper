#include <bits/stdc++.h>
using namespace std;

int D, N;
int K[1234], S[1234];

bool f(double speed) { 
  double time_needed = D/speed;
  for (int i = 0; i < N; i++) {
    double pos = K[i] + S[i]*time_needed;
    if (pos < D) return false;
  }
  return true;
}

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;
  int case_num = 0;
  while (T--) {
    case_num++;
    cin >> D >> N;
    for (int i = 0; i < N; i++) cin >> K[i] >> S[i];

    double low_speed = 0;
    double high_speed = 1e15;
    int counter = 0;
    while (fabs(high_speed - low_speed) > 1e-8) {
      counter++;
      if (counter > 10000) break;
      double mid_speed = (low_speed + high_speed)*0.5;
      if (f(mid_speed)) low_speed = mid_speed;
      else high_speed = mid_speed;
    }

    double ans = (low_speed + high_speed)*0.5;
    printf("Case #%d: %0.6lf\n", ans, case_num);
  }
}
