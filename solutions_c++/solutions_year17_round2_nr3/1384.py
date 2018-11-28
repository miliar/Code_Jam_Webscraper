#include <bits/stdc++.h>

using namespace std;

void solve() {
  int n; int q;
  cin >> n >> q;
  double city_horse[101][101];
  vector<double> e(n+1);
  vector<double> s(n+1);
  for(int i = 1; i <= n; i++) {
    cin >> e[i] >> s[i];
  }
  double city_map[101][101];
  for(int i = 1; i <= n; i++) {
    for(int j = 1; j <= n; j++) {
      cin >> city_map[i][j];
    }
  }
  int a; int b;
  for(int i = 1; i <= q; i++) {
    cin >> a >> b;
    vector<double> hours(n+1);
    vector<double> dis_covered(n+1);
    double min_hours;
    double hours_cov = 0;
    for(int j = a+1; j <= b; j++) {
      min_hours = (double)1e18;
      for(int k = 1; k < j; k++) {
        if(e[k]>=dis_covered[k]+city_map[j-1][j]) {
          hours[k] += (city_map[j-1][j] / s[k]);
          min_hours = min(min_hours, hours[k]);
        }
        dis_covered[k] += city_map[j-1][j];
      }
      hours_cov = min_hours;
      hours[j] = hours_cov;
    }
    cout << fixed << setprecision(9) << hours_cov;
    if(i!=q) cout << " ";
  }
}

int main() {
  int t; cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
