#include <iostream>
#include <string>
#include <vector>
#include <set>

using namespace std;

const double pi = 3.14159265358979323846264;

int main()
{
  cout.precision(20);

  uint nCase;
  cin >> nCase;
  for (auto iCase = 1; iCase <= nCase; ++iCase) {

    uint n, k;
    cin >> n >> k;
    vector<pair<double, double>> cakes;
    for (auto i = 0; i < n; ++i) {
      double r, h;
      cin >> r >> h;
      cakes.push_back(make_pair(r, h));
    }

    sort(cakes.begin(), cakes.end());

    multiset<double> s;
    for (auto i = 0; i < k-1; ++i) {
      s.insert(2 * pi * cakes[i].first * cakes[i].second);
    }

    double m = 0.0;
    for (auto i = k-1; i < n; ++i) {

      double t = 0.0;
      auto j = 0;
      for (auto it = s.rbegin(); j < k - 1; ++j, ++it) {
        t += *it;
      }

      m = max(m, t + 2 * pi * cakes[i].first * cakes[i].second + pi * cakes[i].first * cakes[i].first);

      s.insert(2 * pi * cakes[i].first * cakes[i].second);
    }

    cout << "Case #" << iCase << ": " << m << endl;
  }

  return 0;
}
