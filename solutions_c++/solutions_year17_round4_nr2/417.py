#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

template<class T>
ostream& operator<< (ostream& fout, const vector<T>& vec) {
  for (const auto& el : vec) {
    fout << el << ' ';
  }
  return fout;
}

template <class T>
istream& operator>> (istream& fin, vector<T>& vec) {
  for (size_t i = 0; i < vec.size(); ++i) {
    cin >> vec[i];
  }
  return fin;
}

int n, m, c;
bool check(vector<vector<int>> hist, int cap, int* res) {
  for (int j = 0; j < c; ++j) {
    int sum = 0;
    for (int i = 0; i < n; ++i) {
      sum += hist[j][i];
    }
    if (sum > cap) return 0;
  }

  int cal = 0;
  int left = 0;
  for (int i = n - 1; i >= 0; --i) {
    int sum = 0;
    for (int j = 0; j < c; ++j) {
      sum += hist[j][i];
    }

    if (sum > cap) {
      left += sum - cap;
      cal += sum - cap;
    } else {
      left -= min(left, cap - sum);
    }
  }
  if (res) *res = cal;
  return left == 0;
}

int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cin >> n >> c >> m;
    vector<vector<int>> hist(c, vector<int> (n)); 
    for (int i = 0; i < m; ++i) {
      int p, b;
      cin >> p >> b;
      --p; --b;
      ++hist[b][p];
    }
    int left = 0;
    int right = m;
    while (right != left) {
      int mid = left + (right - left) / 2;
      if (check(hist, mid, nullptr)) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
    int res = 0;
    check(hist, left, &res);
    cout << "Case #" << t << ": "
         << left << ' ' << res << "\n";
  }
  return 0;
}


int main() {
#ifndef LOCAL
  //freopen("input.txt", "rt", stdin);
  //freopen("output.txt", "wt", stdout);
#endif
#ifdef LOCAL
  //freopen("input.txt", "rt", stdin);
#endif

  ios_base::sync_with_stdio(0);
  cin.tie(0);
  Solve();
  return 0;
}
