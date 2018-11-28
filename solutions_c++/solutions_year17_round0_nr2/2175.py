#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")

#include <iostream>
#include <string>
#include <cassert>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

void solve() {
	ll n;
	cin >> n;
  //n = (rand() % 10000) + 1;
	
	auto s = to_string(n);
  auto sr = s;
  reverse(all(sr));

	ll result = 1;

  for (int l = 1; l <= s.size(); l++) {
    if (l < s.size()) {
      ll candidate = 0;
      for (int i = 0; i < l; i++)
        candidate = 10 * candidate + 9;
      result = max(result, candidate);
    } else {
      {
        ll candidate = 0;
        int digit = 9;
        ll pw = 1;
        for (int i = 0; i < l; i++) {
          digit = min(digit, sr[i] - '0');
          candidate += pw * digit;
          pw *= 10;
        }
        result = max(result, candidate);
      }
      for (int p = 0; p < l; p++) {
        if (sr[p] == '0')
          continue;
        ll candidate = 0;
        ll pw = 1;
        for (int i = 0; i < p; i++) {
          candidate += pw * 9;
          pw *= 10;
        }
        int digit = sr[p] - '0' - 1;
        candidate += digit * pw;
        pw *= 10;
        for (int i = p + 1; i < l; i++) {
          digit = min(digit, sr[i] - '0');
          candidate += pw * digit;
          pw *= 10;
        }
        result = max(result, candidate);
        //cout << "C: " << candidate << endl;
      }
    }
  }

  assert(result <= n);

  /*ll dumb = 0;
  for (ll i = 1; i <= n; i++) {
    string c = to_string(i);
    bool ok = true;
    for (int j = 1; j < c.size(); j++) {
      ok &= c[j - 1] <= c[j];
    }
    if (ok)
      dumb = i;
  }

  assert(result == dumb);*/


	cout << result;
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
