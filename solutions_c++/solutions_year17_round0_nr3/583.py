#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

typedef pair<ll, ll> pll;

int main() {
  ios :: sync_with_stdio(0);


  int t; cin >> t;
  for(int cn=1; cn<=t; cn++) {

    ll n,k;

    cin >> n >> k;

    map<ll, ll> m;

    m[n] = 1;

    ll ansmn;
    ll ansmx;
    while (k > 0) {
      ll val, qtd;

      tie(val, qtd) = *m.rbegin();
      m.erase(val);

      ll take = min(qtd, k);

      ll ls = (val-1)/2;
      ll rs = (val-1+1)/2;

      ansmn = min(ls, rs);
      ansmx = max(ls, rs);

      m[ls] += take;
      m[rs] += take;

      k -= take;
    }



    printf("Case #%d: %lld %lld\n", cn, ansmx, ansmn);
  }
  return 0;
}
