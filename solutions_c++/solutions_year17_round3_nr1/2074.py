#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <numeric>
#include <iomanip>
#include <map>

using namespace std;
typedef unsigned long long ull;

const double PI = 3.1415926535897;
void problem() {
  double n, k;
  cin >> n >> k;

  //map<double , vector<double , double >> m;
  vector<pair<double, double>> vv;
  for (int i = 0; i < n; ++i) {
    double r, h;
    cin >> r >> h;
//    m[r + h].emplace_back(r, h);
    vv.emplace_back(r, h);
  }
  sort(vv.begin(), vv.end(), [](const pair<double, double>& a, const pair<double, double>& b){
      return a.first < b.first;
  });
//  double prev = 0;
//  double res = 0;
//  for (auto it = m.rbegin(); it != m.rend(); ++it) {
//    if (k == 0) {
//      break;
//    }
//    res += it->second * 2 * it->first * PI;
//    if (prev != 0) {
//      res += PI * (prev * prev - it->first * it->first );
//    }
//    prev = it->first;
//  }
//
//  vector<double> dp(k +1);
//
  vector<bool> v(n);
  double  res = 0;

  fill(v.end() - k, v.end(), true);
  do {
    double pp = 0;
    int i = 0;
    double prev = 0;
    for (; i < n; ++i) {
      if (v[i]) {
        pp += vv[i].second * 2 * PI * vv[i].first;
        pp += PI * (vv[i].first * vv[i].first - prev*prev);
        prev = vv[i].first;
      }
    }
    if (pp > res)
      res = pp;


  } while (next_permutation(v.begin(), v.end()));

  cout << fixed << setprecision(9) << res << endl;
}

int main() {
  ifstream in("../../in");
  cin.rdbuf(in.rdbuf());

  int n;
  cin >> n;
  for (int i = 0; i < n; ++i) {
    cout << "Case #" << (i + 1) << ": ";
    problem();
  }

  return 0;
}