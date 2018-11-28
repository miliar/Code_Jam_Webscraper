#include <iostream>
#include <sstream>
#include <algorithm>
#include <bitset>
#include <complex>
#include <exception>
#include <initializer_list>
#include <locale>
#include <tuple>
#include <typeinfo>
#include <type_traits>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <limits>
#include <iomanip>

using namespace std;

void output(int t, vector<string> res) {
  cout << "Case #" << t + 1<< ": " << endl;
  for (int i=0; i < res.size(); i++) {
    cout << res[i] << endl;
  }
}

void output(int t, double res) {
  cout << "Case #" << t + 1<< ": " << setprecision(19) << res << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int t;
  cin >> t;
  for (int tt = 0; tt < t; tt++) {
    int d, n;
    cin >> d >> n;
    vector<pair<int, int> > a;
    for (int i=0, k, s; i<n; i++) {
      cin >>  k >> s;
      a.push_back(make_pair(k, s));
    }
    sort(a.begin(), a.end());
    double t = (double)(d - a[0].first) / (double) a[0].second;
    int v = a[0].second;
    double d0 = d;
    for (int i=1; i < a.size(); i++) {
      if (a[0].second <= a[i].second) continue;
      double tmp = (double)(a[i].first - a[0].first) / (double)(a[0].second - a[i].second);
      if (a[0].first + a[0].second * tmp <= d && tmp < t){
        t = tmp;
        v = a[i].second;
        d0 = a[0].first + a[0].second * tmp;
      }
    }
    //cout << t << " "<< v << " " << d0 << endl;
    t += (d - d0)/v;
    //cout << t << endl;
    double res = d/t;
    output(tt, res);
  }
  return 0;
}
