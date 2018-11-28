#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <numeric>
#include <functional>
using namespace std;

typedef unsigned long long int llui;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;
typedef pair<string, string> pss;

const int sz = 1e5;

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int Ac, Aj;
    cin >> Ac >> Aj;
    vector<pii> Acc(Ac);
    vector<pii> Ajc(Aj);
    vector<piii> all;

    for (int i = 0; i < Ac; ++i) {
      piii a;
      cin >> a.first.first >> a.first.second;
      a.second = 0;
      all.push_back(a);
    }
    for (int i = 0; i < Aj; ++i) {
      piii a;
      cin >> a.first.first >> a.first.second;
      a.second = 1;
      all.push_back(a);
    }

    if (all.size() == 0) {
      cout << 2 << endl;
      continue;
    }

    sort(all.begin(), all.end());

    vector<int> buffer[2];
    int worktime[2] = {0, 0};

    int ch = 0;
    int acc = all[0].first.second;
    int cur_start = all[0].first.first;
    for (int i = 1; i < all.size(); ++i) {
      if (all[i].second != all[i - 1].second) {
        ++ch;
        worktime[all[i - 1].second] += all[i - 1].first.second - cur_start;
        cur_start = all[i].first.first;
      } else {
        int diff = all[i].first.first - all[i - 1].first.second;
        buffer[all[i].second].push_back(diff);
      }
    }

    if (all.back().second != all[0].second) {
      worktime[all.back().second] += all.back().first.second - cur_start;
      ++ch;
    } else {
      int diff = (1440 - all.back().first.second + all[0].first.first);
      buffer[all[0].second].push_back(diff);
      worktime[all[0].second] += (1440 - cur_start) + all[0].first.first;
    }

    sort(buffer[0].begin(), buffer[0].end());
    sort(buffer[1].begin(), buffer[1].end());

    for (int i = 0; i < 2; ++i) {
      int j = buffer[i].size() - 1;
      while (worktime[i] > 720) {
        ch += 2;
        worktime[i] -= buffer[i][j];
        --j;
        if (j < 0 && worktime[i] > 720) {
          cout << "SHIT" << endl;
          break;
        }
      }
    }

    cout << ch << endl;
  }
}

