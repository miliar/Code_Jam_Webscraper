#include <bits/stdc++.h>
using namespace std;

int main() {
  int T;
  cin >> T;
  cout << setprecision(10);
  for(int t = 0; t < T; t++) {
    double D;
    int N;
    cin >> D >> N;
    double all_arrive = 0.0;

    for(int i = 0; i < N; i++) {
      double K, S;
      cin >> K >> S;
      all_arrive = max(all_arrive, (D - K) / S);
    }
    double ans = D / all_arrive;
    cout << "Case #" << t + 1 << ": " << ans <<  endl;
  }
}
