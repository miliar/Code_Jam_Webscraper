#include <cassert>
#include <iostream>
#include <map>
#include <utility>
using namespace std;

typedef long long ll;
typedef map<ll, ll> Map;

void get_last(Map& m, ll& k, ll& v) {
  Map::iterator it = m.end();
  --it;
  k = it->first;
  v = it->second;
  m.erase(it);
}

ll fun(ll n, ll k) {
  Map m;
  m[n] = 1;
  while (true) {
    ll s, a;
    get_last(m, s, a);
    if (k < a) {
      return s;
    }
    k -= a;
    ll h1 = (s - 1)/2;
    ll h2 = s - 1 - h1;
    m[h1] += a;
    m[h2] += a;
  }
}

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    ll n, k;
    cin >> n >> k;
    ll res = fun(n, k - 1);
    ll h1 = (res - 1)/2;
    ll h2 = res - 1 - h1;
    cout << "Case #" << cas << ": " << h2 << " " << h1 << endl;
  }
}
