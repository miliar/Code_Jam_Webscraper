#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <string>
#include <utility>

using namespace std;
typedef long long ll;

ll INF = (ll)2e10;

template<typename T> T next() { T tmp; cin >> tmp; return tmp; }


ll fight(ll hd, ll h, ll ad, ll hk, ll ak) {
  ll steps = 0;
  if (hk <= ad) {
    return 1;
  }
  if (h <= ak) {
    h = hd - ak;
    steps++;
    if (h <= ak) {
      return INF;
    }
  }
  while (hk > 0) {
    hk -= ad;
    h -= ak;
    if (hk <= 0) {
      return steps + 1;
    }
    if (h <= 0) {
      return INF;
    }
    steps++;
    if (hk - ad > 0 && h <= ak) {
      h = hd - ak;
      steps++;
    }
  }
  return steps;
}

ll buff(ll hd, ll h, ll ad, ll hk, ll ak, ll b) {
  ll steps = 0;
  ll result = fight(hd, h, ad, hk, ak);
  if (b == 0) {
    return result;
  }
  if (h <= ak) {
    h = hd - ak;
    steps++;
    if (h <= ak) {
      return INF;
    }
  }
  
  while (ad <= hk) {
    ad += b;
    h -= ak;
    if (h <= 0) {
      return min(result, INF);
    }
    steps++;
    result = min(result, steps + fight(hd, h, ad, hk, ak));
    if (h <= ak) {
      h = hd - ak;
      steps++;
    }
  }
  result = min(result, steps + fight(hd, h, ad, hk, ak));
  return result;
}

ll debuff(ll hd, ll h, ll ad, ll hk, ll ak, ll b, ll d) {
  ll steps = 0;
  ll result = buff(hd, h, ad, hk, ak, b);
  if (d == 0) {
    return result;
  }
  while (ak > 0) {
    ak = max(ak - d, (ll)0);
    h -= ak;
    if (h <= 0) {
      return min(result, INF);
    }
    steps++;
    result = min(result, steps + buff(hd, h, ad, hk, ak, b));
    if (h <= ak - d) {
      h = hd - ak;
      steps++;
    }
  }
  result = min(result, steps + buff(hd, h, ad, hk, ak, b));
  return result;
}



void solve() {
 ll hd = next<ll>();
 ll ad = next<ll>();
 ll hk = next<ll>();
 ll ak = next<ll>();
 ll b = next<ll>();
 ll d = next<ll>();
 ll h = hd;

 ll result = debuff(hd, h, ad, hk, ak, b, d);
 if (result == INF) {
  cout << "IMPOSSIBLE" << endl;
  return;
 }
 cout << result << endl;
}

int main() {
  int n = next<int>();
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  } 
  return 0;
}
