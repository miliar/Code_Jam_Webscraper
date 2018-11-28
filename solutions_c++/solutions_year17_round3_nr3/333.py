#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <iomanip>

using namespace std;

double eps = 1e-10;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int N, K;
    double U;
    cin >> N >> K >> U;

    vector<double> ps;
    for (int i = 0; i < N; i++) {
      double p;
      cin >> p;
      ps.push_back(p);
    }

    sort(ps.begin(), ps.end());

    while (U > eps) {
      int a;
      double d;
      for (a = 1; a < ps.size(); a++) {
        d = ps[a] - ps[a - 1];
        if (d > eps) {
          break;
        }
      }
      double e;
      if (d <= eps) {
        e = U;
      } else {
        e = min(U, a * d);
      }
      U -= e;
      //cout << "add " << e / a << " each to first " << a << endl;
      for (int i = 0; i < a; i++) {
        ps[i] += e / a;
      }
    }

    double prod = 1.0;
    for (auto p : ps) {
      prod *= p;
    }

    cout << setprecision(11);
    cout << "Case #" << (t + 1) << ": " << prod << endl;
  }

  return 0;
}
