/**
 * Problem: test.cpp
 * Author: babhishek21
 * Lang: C++11
 */

#include <bits/stdc++.h> // using GCC/G++
// #include "custom/prettyprint.hpp" // G++11 only
using namespace std;

static const int MOD = 1000000007;
static const int INF = 0x3f3f3f3f;
static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
#define pb push_back
#define eb emplace_back
#define mp make_pair

#define debug(x) cerr << #x << " : " << x << endl;
#define whole(func, x, ...) ([&](decltype((x)) var) { return (func)(begin(var), end(var), ##__VA_ARGS__); })(x)

int t, n, k, i, cnt;
string str;

int flip() {
  int j = 0, err = -1;

  while(j < k && i+j < n) {
    str[i+j] = (str[i+j] == '+' ? '-' : '+');

    err = (str[i+j] == '+' && err < 0 ? i+j : err);

    j++;
  }

  return err;
}

void solve() {
  cin >> str;
  cin >> k;
  n = str.length();

  i = 0, cnt = 0;

  while(i < n) {
    if(str[i] == '+') {
      i++;
      continue;
    }

    cnt++;

    i = flip();

    // debug(str)

    if(i+k > n) {
      cout << "IMPOSSIBLE";
      return;
    }
  }

  cout << cnt;
}

int main() {
  // ios_base::sync_with_stdio(false); // for fast I/O

  cin >> t;

  for(int tc=0; tc<t; tc++) {
    cout << "Case #" << tc+1 << ": ";
    solve();
    cout << endl;

    debug(tc)
  }

  return 0;
}
