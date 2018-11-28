#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int tests; cin >> tests;
  for(int test = 0; test<tests; ++test) {
    int ac, aj; cin >> ac >> aj;
    vector<pair<pair<int, int>, bool > > times;
    int tc = 0, tj = 0;
    for(int i = 0; i<ac; ++i) {
      int ci,di;
      cin >> ci >> di;
      times.push_back(make_pair(make_pair(ci, di), false));
      tc += di - ci;
    }
    for(int i = 0; i<aj; ++i) {
      int ci,di;
      cin >> ci >> di;
      times.push_back(make_pair(make_pair(ci, di), true));
      tj += di - ci;
    }
    tc = 720 - tc;
    tj = 720 - tj;
    sort(times.begin(), times.end());

    int total = 0;
    for(int i = 0; i<(int)times.size()-1; ++i) {
      if(times[i].second != times[i+1].second) {
        total++;
      }
    }
    if(times[0].second != times[times.size()-1].second) {total++;}

    vector<int> gapsc;
    for(int i = 0; i<(int)times.size()-1; ++i) {
      if(times[i].second == times[i+1].second && times[i].second == false) {
        gapsc.push_back(times[i+1].first.first - times[i].first.second);
      }
    }
    if(times[0].second == times[times.size()-1].second && times[0].second == false) {
      gapsc.push_back(times[0].first.first - times[times.size()-1].first.second + 1440);
    }
    sort(gapsc.begin(), gapsc.end());
    for(int i = 0; i<(int)gapsc.size(); ++i) {
      tc -= gapsc[i];
      if(gapsc[i] != 0 && tc < 0) {total += 2;}
    }

    vector<int> gapsj;
    for(int i = 0; i<(int)times.size()-1; ++i) {
      if(times[i].second == times[i+1].second && times[i].second == true) {
        gapsj.push_back(times[i+1].first.first - times[i].first.second);
      }
    }
    if(times[0].second == times[times.size()-1].second && times[0].second == true) {
      gapsj.push_back(times[0].first.first - times[times.size()-1].first.second + 1440);
    }
    sort(gapsj.begin(), gapsj.end());
    for(int i = 0; i<(int)gapsj.size(); ++i) {
      tj -= gapsj[i];
      if(gapsj[i] != 0 && tj < 0) {total += 2;}
    }

    cout << fixed << "Case #" << test+1 << ": " << total << endl;
  }
}
