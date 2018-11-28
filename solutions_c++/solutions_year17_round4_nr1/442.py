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

int64_t n, p;
map<pair<vector<int64_t>, int64_t>, int64_t> result;
int64_t getResult(vector<int64_t> rem, int64_t left) {
  int64_t ans = 0;
  if (rem == vector<int64_t>{0, 0, 0, 0}) return 0;
  if (result.count({rem, left})) {
      return result[{rem, left}];
  }

  for (int64_t i = 0; i < rem.size(); ++i) {
    if (rem[i] > 0) {
      rem[i] -= 1;
      ans = max(ans, getResult(rem, (left + i) % p));
      rem[i] += 1;
    }
  }
  result[{rem, left}] = ans + (left == 0);
  return ans + (left == 0);
}

int64_t Solve() {
  int64_t tt;
  cin >> tt;
  for (int64_t t = 1; t <= tt; ++t) {
    result.clear();
    cin >> n >> p;
    cout << "Case #" << t << ": ";
    vector<int64_t> rem = {0, 0, 0, 0};
    for (int64_t i = 0; i < n; ++i) {
      int64_t cur = 0;
      cin >> cur;
      ++rem[cur % p];
    }
    cout << getResult(rem, 0) << '\n';

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
