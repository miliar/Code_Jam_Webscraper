#include <iostream>
#include <string>
#include <queue>
#include <set>
#include <cassert>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int solve2(int n, int c, int t, const vector<vector<int>>& a) {
  // cerr << "solve n: " << n << " c: " << c << " t: " << t << endl;
  vector<set<int>> inside(t);
  vector<int> frees(t, 0);
  int s = 0;
  for (int i = 0; i < n; ++i) {
    vector<char> taken(t, false);

    for (auto x : a[i]) {
      int toplace = -1;
      for (int j = 0; j < t; ++j) {
        if (taken[j]) continue;
        if (inside[j].count(x) == 0) {
          if (toplace == -1 || frees[toplace] < frees[j]) {
            toplace = j;
          }
        }
      }
      if (toplace != -1) {
        assert(!taken[toplace]);
        assert(inside[toplace].count(x) == 0);
        taken[toplace] = true;
        inside[toplace].insert(x);
        continue;
      }

      for (int j = 0; j < t; ++j) {
        if (frees[j] == 0) continue;
        if (inside[j].count(x) == 0) {
          if (toplace == -1 || frees[toplace] < frees[j]) {
            toplace = j;
          }
        }
      }
      if (toplace != -1) {
        assert(taken[toplace]);
        assert(inside[toplace].count(x) == 0);
        assert(frees[toplace] > 0);
        frees[toplace]--;
        s++;
        inside[toplace].insert(x);
        continue;
      }

      return -1;
    }

    for (int j = 0; j < t; ++j) {
      if (!taken[j]) frees[j]++;
    }
  }
  return s;
}

int solve(int n, int c, int t, const vector<vector<int>>& a) {
  int ss = solve2(n,c,t,a);
  // cerr << "solve n: " << n << " c: " << c << " t: " << t << endl;
  vector<set<int>> inside(t);
  vector<int> frees(t, 0);
  int s = 0;
  for (int i = 0; i < n; ++i) {
    vector<char> taken(t, false);

    for (auto x : a[i]) {
      int toplace = -1;
      for (int j = 0; j < t; ++j) {
        if (taken[j]) continue;
        if (inside[j].count(x) == 0) {
          if (toplace == -1 || frees[toplace] > frees[j]) {
            toplace = j;
          }
        }
      }
      if (toplace != -1) {
        assert(!taken[toplace]);
        assert(inside[toplace].count(x) == 0);
        taken[toplace] = true;
        inside[toplace].insert(x);
        continue;
      }

      for (int j = 0; j < t; ++j) {
        if (frees[j] == 0) continue;
        if (inside[j].count(x) == 0) {
          if (toplace == -1 || frees[toplace] < frees[j]) {
            toplace = j;
          }
        }
      }
      if (toplace != -1) {
        assert(taken[toplace]);
        assert(inside[toplace].count(x) == 0);
        assert(frees[toplace] > 0);
        frees[toplace]--;
        s++;
        inside[toplace].insert(x);
        continue;
      }

      return ss;
    }

    for (int j = 0; j < t; ++j) {
      if (!taken[j]) frees[j]++;
    }
  }
  if (ss != -1) return min(s,ss);
}

int main() {
  int tc;
  cin >> tc;
  for (int t = 0; t < tc; ++t) {
    int n,c,m;
    cin >> n >> c >> m;
    vector<pair<int,int>> a(m);
    vector<vector<int>> need_pos(n);
    for (auto& x : a) {
      cin >> x.first >> x.second;
      x.first--;
      x.second--;
      need_pos[x.first].push_back(x.second);
    }
    for (auto & x : need_pos) {
      sort(x.begin(), x.end());
    }
    int l = 1;
    int r = 1001;
    while(l < r) {

    //for (int i = 1; i < 2000; ++i) {
       int mm = (l + r) /2;
 //     int mm = i;
      int s = solve(n,c,mm,need_pos);
      // cerr << "l: " << l << " r: " << r << " s: " << s << endl;
      if (s != -1) {
        r = mm;
//        break;
      } else {
        l = mm + 1;
      }
    }
    int s = solve(n,c,r,need_pos);

    cout << "Case #" << t + 1 << ": " << r << " " << s << endl;
  }
}
