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

int Solve() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    long long n;
    cin >> n;
    string str = to_string(n);
    bool f = 1;
    while (f) {
      f = 0;
      for (int i = 1; i < (int)str.size(); ++i) {
        if (str[i] < str[i - 1]) {
          for (int j = i; j < (int) str.size(); ++j) {
            str[j] = '0';
          }
          f = 1;
          break;
        }
      }
      n = stoll(str);
      if (f) {
        --n;
      }
      str = to_string(n);
    }
    for (int i = (int) str.size() - 2; i >= 0; --i) {
      if (str[i] > str[i + 1]) {
        str[i] = str[i + 1];
      }
    }
    std::cout << "Case #" << t << ": "
              << str << "\n";
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
