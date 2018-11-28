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

int main() {
  int cases;
  cin >> cases;
  for (int ca = 1; ca <= cases; ++ca) {
    int ac;
    int aj;
    cin >> ac >> aj;
    vector<pair<pair<int, int>, bool>> times;
    for (int i = 0; i < ac; ++i) {
      int c;
      int d;
      cin >> c >> d;
      times.push_back(make_pair(make_pair(c, d), true));
    }
    for (int i = 0; i < aj; ++i) {
      int c;
      int d;
      cin >> c >> d;
      times.push_back(make_pair(make_pair(c, d), false));
    }
    sort(times.begin(), times.end());
    int start_of = times[0].first.first;
    for (auto&& t : times) {
      t.first.first -= start_of;
      t.first.second -= start_of;
    }
    int break_cnt = ac;
    int already_off = 0;
    for (auto&& t : times) {
      if (t.second) {
        already_off += t.first.second - t.first.first;
      }
    }
    vector<int> merging;
    vector<int> filling;
    vector<int> nothing;
    for (int i = 0;i < ac + aj; ++i) {
      auto second = (i +1)%(ac+aj);
      auto k = times[second].first.first - times[i].first.second;
      if (k < 0) {
        k += 1440;
      }
      if (times[i].second == true && times[second].second == false) {
        filling.push_back(k);
      } else if (times[i].second == true && times[second].second == true) {
        merging.push_back(k);
      } else if (times[i].second == false && times[second].second == false) {
        nothing.push_back(k);
      } else {
        filling.push_back(k);
      }
    }
    // for (auto i : merging) {
    //   printf("m %d\n", i);
    // }
    // for (auto i : filling) {
    //   printf("f %d\n", i);
    // }
    // for (auto i : nothing) {
    //   printf(" n%d\n", i);
    // }
    sort(merging.rbegin(), merging.rend());
    while (already_off < 720 && 0 < merging.size()) {
      already_off += merging.back();
      merging.pop_back();
      --break_cnt;
      if (720 < already_off) {
        ++break_cnt;
      }
    }
    while (already_off < 720 && 0 < filling.size()) {
      already_off += filling.back();
      filling.pop_back();
    }
    sort(nothing.begin(), nothing.end());
    while (already_off < 720 && 0 < nothing.size()) {
      already_off += nothing.back();
      nothing.pop_back();
      ++break_cnt;
    }
    printf("Case #%d: %d\n", ca, 2 * break_cnt);
  }
  return 0;
}
