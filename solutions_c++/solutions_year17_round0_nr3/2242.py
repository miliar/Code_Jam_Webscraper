#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")

#include <iostream>
#include <string>
#include <cassert>
#include <vector>
#include <set>
#include <map>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

void solve() {
	ll n, k;
	cin >> n >> k;

  map<ll, ll> segments;
  segments[n] = 1;

  while (k > 0) {
    assert(!segments.empty());
    auto it = --segments.end();
    ll len = it->first;
    ll cnt = it->second;

    segments.erase(it);
    
    k -= cnt;
    if (k <= 0) {
      cout << (len / 2) << " " << (len - 1) / 2;
    }

    if (len > 2) {
      segments[(len - 1) / 2] += cnt;
    }
    if (len > 1) {
      segments[len / 2] += cnt;
    }
  }
  
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
