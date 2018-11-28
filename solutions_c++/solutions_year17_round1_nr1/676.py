#include <bits/stdc++.h>

using namespace std;

void check(string s[], string ans[], int r, int c) {
  map<char, set<pair<int, int>>> mp;
  for (int i = 0; i < r; ++i) {
    assert(ans[i].length() == c);
  }
  for (int i = 0; i < r; ++i) {
    for (int j = 0; j < c; ++j) {
      mp[ans[i][j]].insert(make_pair(i, j));
    }
  }
  assert(mp.find('?') == mp.end());
  for (auto &x: mp) {
    assert('A' <= x.first && x.first <= 'Z');
    int x1 = x.second.begin()->first, x2 = x.second.rbegin()->first, y1 = x.second.begin()->second, y2 = x.second.rbegin()->second;
    assert(x.second.size() == (x2 - x1 + 1) * (y2 - y1 + 1));
    for (int i = x1; i <= x2; ++i) {
      for (int j = y1; j <= y2; ++j) {
        assert(ans[i][j] == x.first && (s[i][j] == '?' || s[i][j] == x.first));
      }
    }
  }
}

void solve(string s[], int r, int c) {
  vector<int> ret;
  string ans[30];
  for (int i = 0; i < r; ++i) {
    vector<int> vec;
    for (int j = 0; j < c; ++j) {
      if (s[i][j] != '?') {
        vec.push_back(j);
      }
    }
    ans[i] = "";
    if (vec.empty()) {
      continue;
    }
    for (int j = 0, sz = vec.size(), k = 0; j < c;) {
      if (j <= vec[k] || k == sz - 1) {
        ans[i].push_back(s[i][vec[k]]);
        ++j;
      } else {
        ++k;
      }
    }
    ret.push_back(i);
  }
  for (int i = 0, sz = ret.size(), j = 0; i < r;) {
    if (i <= ret[j] || j == sz - 1) {
      ans[i] = ans[ret[j]];
      ++i;
    } else {
      ++j;
    }
  }
  check(s, ans, r, c);
  for (int i = 0; i < r; ++i) {
    cout << ans[i] << endl;
  }
}

int main() {
  int test, r, c;
  string s[30];
  cin >> test;
  for (int ca = 1; ca <= test; ++ca) {
    cin >> r >> c;
    for (int i = 0; i < r; ++i) {
      cin >> s[i];
    }
    cout << "Case #" << ca << ": " << endl;
    solve(s, r, c);
  }
  return 0;
}
