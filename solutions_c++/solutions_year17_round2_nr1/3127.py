#include <iostream>
#include <iomanip>
using namespace std;
int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  int t;
  cin >> t;
  cout << fixed;
  cout << setprecision(7);
  for (int ti = 0; ti < t; ++ti) {
    cout << "Case #" << ti+1 << ": ";
    double d;
    int n;
    cin >> d >> n;
    double result = 1e50;
    for (int i = 0; i < n; ++i) {
      double k, s;
      cin >> k >> s;
      result = min(result, d*s/(d-k));
    }
    cout << result <<endl;
  }
}
