#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

const int last = 60*24;

void update(multimap<int, tuple<int,int>> &m, int type, vector<pair<int, int>>& ranges) {
  int count = ranges.size();
  for (int i = 0; i < count - 1; ++i) {
    m.emplace(ranges[i + 1].first - ranges[i].second, make_tuple(type, i));
  }
  if (count >= 1)
    m.emplace(last - ranges.back().second + ranges.front().first, make_tuple(type, count - 1));
}

int main() {
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int count1, count2;
    cin >> count1 >> count2;

    int used[2] = {0, 0};

    vector<pair<int, int>> ranges[2];
    ranges[0].resize(count1);
    ranges[1].resize(count2);
    for (int i = 0; i < count1; ++i) {
      cin >> ranges[0][i].first >> ranges[0][i].second;
      used[0] += ranges[0][i].second - ranges[0][i].first;
    }
    for (int i = 0; i < count2; ++i) {
      cin >> ranges[1][i].first >> ranges[1][i].second;
      used[1] += ranges[1][i].second - ranges[1][i].first;
    }

    sort(ranges[0].begin(), ranges[0].end());
    sort(ranges[1].begin(), ranges[1].end());

    multimap<int, tuple<int,int>> m;

    update(m, 0, ranges[0]);
    update(m, 1, ranges[1]);

    vector<int> merges[2];

    for (auto& e: m) {
      int dist = e.first;
      int type = get<0>(e.second);
      int id = get<1>(e.second);

      int other_type = (type + 1) % 2;

      if (used[type] + dist <= 720) {
        bool can_merge = true;

        int start = ranges[type][id].second;
        int end = ranges[type][(id + 1) % ranges[type].size()].first;

        for (int i = 0; i < ranges[other_type].size(); ++i) {
          int s = ranges[other_type][i].first;
          int e = ranges[other_type][i].second;

          if (start <= end && ((start <= s && s <= end) || (start <= e && e <= end))) {
            can_merge = false;
            break;
          }

          if (start > end && (start <= s || start <= e || s <= end || e << end)) {
            can_merge = false;
            break;
          }
        }
        if (can_merge) {
          used[type] += dist;
          merges[type].push_back(id);
        }
      }
    }

    for (int k = 0; k < 2; ++k)
      for (int i = 0; i < merges[k].size(); ++i) {
        int id = merges[k][i];

        for (int j = i + 1; j < merges[k].size(); ++j) {
          if (merges[k][i] > id)
            merges[k][i]--;
        }

        if (id == ranges[k].size() - 1) {
          ranges[k].back().second = last;
          ranges[k].front().first = 0;
        } else {
          ranges[k][id].second = ranges[k][id+1].second;
          ranges[k].erase(ranges[k].begin() + id + 1);
        }
      }

    map<pair<int,int> ,int> t;

    for (int k = 0; k < 2; ++k)
      for (int i = 0; i < ranges[k].size(); ++i) {
        t[ranges[k][i]] = k;
      }

    int count = 0;

    auto i = t.begin();
    auto n = i;
    ++n;
    while (n != t.end()) {
      if (i->second != n->second) {
        count++;
      } else {
        count += 2;
      }
      i = n;
      ++n;
    }

    i = t.begin();
    n = t.end();
    --n;

    if (i->second != n->second) {
      count++;
    } else if (!(i->first.first == 0 && n->first.second == last)) {
      count += 2;
    }

    cout << "Case #" << test << ": " << count<< endl;
  }
}
