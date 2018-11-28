#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int main() {
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int d, n;
    cin >> d >> n;
    vector<pair<double, double>> h(n);

    for (int i = 0; i < n; ++i)
      cin >> h[i].first >> h[i].second;

    sort(h.begin(), h.end());

    for (int i = 0; i < n - 1; ++i) {
      if (h[i].second <= h[i + 1].second) {
        h.erase(h.begin() + i + 1);
        --n;
      }
    }

    vector<double> dist(n);

    dist.back() = d - h.back().first;

    for (int i = n - 2; i >= 0; --i) {
      dist[i] = h[i].second * (h[i+1].first - h[i].first) / (h[i].second - h[i+1].second);
      while (i + 1 < n && h[i].first + dist[i] > h[i+1].first + dist[i+1]) {
        h.erase(h.begin() + i + 1);
        dist.erase(dist.begin() + i + 1);
        --n;
        if (i + 1 < n) {
          dist[i] = h[i].second * (h[i+1].first - h[i].first) / (h[i].second - h[i+1].second);
        } else {
          dist[i] = d - h.back().first;
        }
      }

      if (i + 1 < n) {
        dist[i + 1] = dist[i + 1] - max(0., dist[i] + h[i].first - h[i+1].first);
      }
    }

    double t = 0.;

    for (int i = 0; i < n; ++i) {
      t += dist[i] / h[i].second;
    }

    cout.precision(10);
    cout << "Case #" << test << ": " << fixed << d / t << endl;
  }
}
