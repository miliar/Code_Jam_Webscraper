#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")

#include <iostream>
#include <string>
#include <cassert>
#include <map>
#include <queue>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

void solve() {
	string s;
  cin >> s;
  int k;
  cin >> k;
  int n = s.size();

  int res = 0;
  bool fail = false;

  {
    auto revert = [](char c) {
      return (c == '+' ? '-' : '+');
    };
    auto sr = s;
    for (int i = 0; i <= n - k; i++) {
      if (sr[i] == '-') {
        ++res;
        for (int j = 0; j < k; j++) {
          sr[i + j] = revert(sr[i + j]);
        }
      }
    }


    for (char c : sr)
      if (c == '-')
        fail = true;
  }

  if (!fail)
    cout << res;
  else
    cout << "IMPOSSIBLE";
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; test++) {
  	cout << "Case #" << test << ": ";
  	solve();
  	cout << endl;
  }

  return 0;
}
