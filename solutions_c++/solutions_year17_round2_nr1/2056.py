#include <bits/stdc++.h>

using namespace std;



int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.setf(ios::fixed, ios::floatfield);
  cout.precision(10);

  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int D, N;
    cin >> D >> N;
    double ans = 0;
    while (N--) {
      int K, S;
      cin >> K >> S;
      ans = max(ans, (D - K) / (S * 1.0));
    }
    cout << D / ans << '\n';
  }
}
