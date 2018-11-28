#include <iostream>
#include <fstream>

#include <stack>
#include <queue>
#include <deque>
#include <vector>

#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>

#include <cmath>

#include <cassert>

#include <algorithm>

using namespace std;

ifstream fin("///Users/Zetilov/Downloads/B-large.in-2.txt");
ofstream fout("output.txt");

void solve(long long cs)
{
  long long n, p;
  fin >> n >> p;
  vector<long long> r(n);
  for (auto& x : r) {
    fin >> x;
  }
  vector<vector<long long>> v(p, vector<long long>(n));
  for (long long i = 0; i < n; ++i) {
    for (long long j = 0; j < p; ++j) {
      fin >> v[j][i];
    }
  }
  long long ans = 0;
  vector<multiset<pair<long long, long long>>> s(n);
  for (long long j = 0; j < p; ++j) {
    const auto& z = v[j];
    for (long long i = 0; i < n; ++i) {
      long long x, y;
      long long L = -1, R = z[i] * 3 + 10, M;
      while (R - L > 1) {
        M = (L + R) / 2;
        if (M * r[i] * 11 >= z[i] * 10) {
          R = M;
        } else {
          L = M;
        }
      }
      x = R;
      L = -1; R = 3 * z[i] + 10;
      while (R - L > 1) {
        M = (L + R) / 2;
        if (M * r[i] * 9 > z[i] * 10) {
          R = M;
        } else {
          L = M;
        }
      }
      y = L;
      s[i].insert({y, x});
    }
  }
  long long mx = 1e6;
  for (long long i = 1; i <= mx; ++i) {
    vector<multiset<pair<long long, long long>>::iterator> del;
    for (const auto& z : s) {
      auto it = z.begin();
      for (; it != z.end(); ++it) {
        if (i <= it->first && i >= it->second) {
          break;
        }
      }
      if (it != z.end()) {
        del.push_back(it);
      }
    }
    if (del.size() == n) {
      ++ans;
      for (long long j = 0; j < n; ++j) {
        s[j].erase(del[j]);
      }
      --i;
    }
  }
  fout << ans;
}


int main()
{
  cin.tie(nullptr);
  ios_base::sync_with_stdio(false);

  cout.setf(ios_base::fixed);
  cout.precision(28);

  long long T;
  fin >> T;
  for (long long cs = 1; cs <= T; ++cs) {
    cout << cs << endl;

    fout << "Case #" << cs << ": ";
    solve(cs);
    fout << endl;
  }
  return 0;
}