#include <algorithm>
#include <bitset>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <iostream>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <memory>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

const int N = (int)1e6 + 1;
const int K = 105;
const int M = 301;
const int inf = (int)1e9 + 7;

void solve(int T) {
  string s;
  cin >> s;
  int n = s.size();
  int x = -1;
  for (int i = 1; i < n; ++i) {
    if (s[i] < s[i - 1]) {
      x = i - 1;
      break;
    }
  }
  if (x == -1) {
    cout << "Case #" << T << ": " << s << '\n';
    return;
  }
  int k = -1;
  for (int i = x; i >= 1; --i) {
    if (s[i - 1] != s[i]) {
      k = i;
    }
  }
  if (k != -1) {
    --s[k];
    for (int i = k + 1; i < n; ++i) {
      s[i] = '9';
    }
  } else {
    --s[0];
    if (s[0] == '0') {
      s = "";
      for (int i = 0; i < n - 1; ++i) {
        s += '9';
      }
    } else {
      for (int i = 1; i < n; ++i) {
        s[i] = '9';
      }
    }
  }
  cout << "Case #" << T << ": " << s << '\n';
}

int main() {
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    solve(t);
  }
  return 0; 
}