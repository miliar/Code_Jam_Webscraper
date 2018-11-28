#include <iostream>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <vector>
using namespace std;
const double PI = 2*acos(0);
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int T;
  cin >> T;
  cout << fixed << setprecision(8);
  for (int Ti = 0; Ti < T; ++Ti) {
    cout << "Case #" << Ti+1 << ": ";
    int n, k;
    cin >> n >> k;
    int r[n], h[n];
    for (int i = 0; i < n; ++i) {
      cin >> r[i] >> h[i];
    }
    double result = 0;
    for (int i = 0; i < n; ++i) {
      double ov = PI*r[i]*r[i] + 2*r[i]*PI*h[i];
      vector<double> asd;
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        if (r[j] <= r[i]) asd.push_back(2*r[j]*PI*h[j]);
      }
      sort(asd.begin(), asd.end(), greater<double>());
      for (int j = 0; j+1 < k && j < asd.size(); ++j) {
        ov += asd[j];
      }
      if (ov > result) result = ov;
    }
    cout << result << '\n';
  }
}
