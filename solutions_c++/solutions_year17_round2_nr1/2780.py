#include<iostream>
#include<iomanip>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int d;
    cin >> d;
    int n;
    cin >> n;
    double max = 0;
    for (int i = 0; i < n; i++) {
      int k;
      cin >> k;
      int s;
      cin >> s;
      int nd = d - k;
      double maxs = nd / (double)s;
      if (max < maxs) {
        max = maxs;
      }
    }
    double r = d / max;
    cout << "Case #" << t << ": " << fixed << setprecision(6) << r << endl;
  }
}
