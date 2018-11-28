#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main() {
  const double eps = 0.0000000001;
  int T;
  cin >> T;
  for(int t = 0; t < T; t++) {
    int N, K;
    cin >> N >> K;
    double U;
    cin >> U;
    vector<double> P(N);

    for(int i = 0; i < N; i++) {
      cin >> P[i];
    }

    sort(P.begin(), P.end());


    for(int i = 0; i < N - 1; i++) {
      // 0,,,iのindexのPを増加させる
      if( double(i + 1) * (P[i + 1] - P[i]) <= U ) {
        U -= double(i + 1) * (P[i + 1] - P[i]);
        for(int j = 0; j <= i; j++) {
          P[j] = P[i + 1];
        }

      }else {
        for(int j = 0; j <= i; j++) {
          P[j] += (U / double(i + 1));
        }
        U = 0.0;
        break;
      }
    }

    if(U > eps) {
      for(int i = 0; i < N; i++) {
        P[i] += U / double(N);
      }
    }

    double ans = 1;
    for(int i = 0; i < N; i++) {
      ans *= P[i];
    }

    cout << fixed;
    cout << setprecision(10);

    cout << "Case #" << t + 1 << ": " << ans << endl;


  }

}
