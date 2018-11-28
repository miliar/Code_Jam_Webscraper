#include <bits/stdc++.h>
using namespace std;

int main() {
  cout.precision(10);
  int t, n;
  double d, k, s, temp, ans;
  bool done;
  vector<pair<double, double>> horses;
  pair<double, double> horse;
  vector<double> times;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    times.clear();
    horses.clear();
    cin >> d >> n;
    done = false;
    for(int j = 0; j < n; j++) {
      cin >> k >> s;
      horse.first = k;
      horse.second = s;
      //temp = (d-k)/s;
      horses.push_back(horse);
    }
    sort(horses.begin(),horses.end());
    for(int j = 0; j < n; j++) {
      k = horses[j].first;
      s = horses[j].second;
      temp = (d-k)/s;
      times.push_back(temp);
    }
    ans = d/times[0];
    for(int j = 0; j < times.size()-1; j++) {
      if(times[j] < times[j+1] && !done) {
        ans = d/times[j+1];
        done = true;
      }
    }
    cout << "Case #" << i << ": " << fixed << ans << endl;
  }

  return 0;
}