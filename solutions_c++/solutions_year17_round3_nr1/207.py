#include <algorithm>
#include <cstdio>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

constexpr double const kPI = 3.14159265358979323846;

int main() {
  int cases;
  cin >> cases;
  for (int ca = 1; ca <= cases; ++ca) {
    int n;
    int k;
    cin >> n >> k;
    vector<pair<int, long long int>> cakes;
    vector<long long int> sides;
    for (int i = 0;i <n; ++i) {
      long long int r;
      long long int h;
      cin >> r >> h;
      cakes.push_back(make_pair(r, r * h));
      sides.push_back(r * h);
    }
    sort(cakes.rbegin(), cakes.rend());
    sort(sides.rbegin(), sides.rend());
    double max_area = -1;
    for (int i = 0; i <= n-k; ++i) {
      auto&& c = cakes[i];
      sides.erase(find(sides.begin(), sides.end(), c.second));
      long long int hh = c.second;
      for (int j = 0;j<k-1;++j) {
        hh += sides[j];
      }
      double area = kPI * c.first * c.first + 2 * kPI * hh;
      max_area = max(area, max_area);
    }
    printf("Case #%d: %f\n", ca, max_area);
  }
  return 0;
}
