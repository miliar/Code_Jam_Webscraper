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
  int k;
  string s;
  cin >> s >> k;
  int n = s.size();
  int ans = 0;
  for (int i = 0; i < n; ++i) {
    if (s[i] == '-' && i + k <= n) {
      for (int j = i; j < i + k; ++j) {
        s[j] = (s[j] == '-' ? '+' : '-');
      }
      ++ans;
    }
  }
  for (int i = 0; i < n; ++i) {
    if (s[i] == '-') {
      cout << "Case #" << T << ": IMPOSSIBLE\n";
      return;
    }
  }
  cout << "Case #" << T << ": " << ans << '\n';
}

int main() {
  freopen("A-large.in", "r", stdin);
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