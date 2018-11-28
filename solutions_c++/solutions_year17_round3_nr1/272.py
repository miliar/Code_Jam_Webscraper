#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
  int tests; cin >> tests;
  for(int test = 0; test<tests; ++test) {

    long long n, k; cin >> n >> k;
    double total = 0;
    vector<pair<double,  double> > sides;
    for(int i = 0; i<n; ++i) {
      double r, h; cin >> r >> h;
      sides.push_back(make_pair(2*r*h, r*r));
    }
    sort(sides.rbegin(), sides.rend());

    k--;
    double maxr2 = 0;
    while(k--) {
      total += sides[0].first;
      maxr2 = max(maxr2, sides[0].second);
      sides.erase(sides.begin());
    }
    double mx = 0;
    for(int i = 0;i<(int)sides.size(); ++i) {
      if(sides[i].second > maxr2) {
        mx = max(mx, sides[i].first + sides[i].second);
      }
      else {
        mx = max(mx, maxr2 + sides[i].first);
      }
    }
    total += mx;

    cout << fixed << setprecision(24) << "Case #" << test+1 << ": " << 3.141592653589793238462643383279502884L * total << endl;
  }
}
