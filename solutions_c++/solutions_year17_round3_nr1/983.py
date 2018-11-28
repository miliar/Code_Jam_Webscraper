#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>
#include <utility>

using namespace std;

int main() {
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int n, k;
    cin >> n >> k;

    vector<pair<double, double>> rh(n);

    for (int i = 0; i < n; ++i)
      cin >> rh[i].first >> rh[i].second;

    sort(rh.begin(), rh.end(), [](pair<double, double>& a, pair<double, double>& b) {
      return a.first > b.first;
    });

    vector<double> v(n);

    for (int i = 0; i < n; ++i) {
      double r = rh[i].first;
      double h = rh[i].second;
      v[i] = r*r + 2*r*h;
    }

    for (int i = 0; i < n; ++i) {
      if (n - i < k) {
        v[i] = -1;
        continue;
      }

      vector<double> ost(n - i - 1);
      for (int j = i + 1; j < n; ++j)
        ost[j - i - 1] = 2 * rh[j].first * rh[j].second;

      sort(ost.rbegin(), ost.rend());

      for (int j = 1; j < k; ++j)
        v[i] += ost[j-1];
    }

    double max = *max_element(v.begin(), v.end());

    cout << "Case #" << test << ": " << setprecision(15)<< max * M_PI<< endl;
  }
}
