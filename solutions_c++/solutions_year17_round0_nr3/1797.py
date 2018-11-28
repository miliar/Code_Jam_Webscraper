#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<ll,ll> ii;

ll n,k;

int main(){
  ios::sync_with_stdio(false);
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    cin >> n >> k;
    ll k2 = 1;
    ii a(n,k2),b(n+1,0);
    while(2*k2-1 < k){
      if(a.first&1){
        ll aux = 2*a.second+b.second;
        ll aux2 = b.second;
        b = ii((a.first>>1)+1,aux2);
        a = ii((a.first>>1),aux);
      }
      else{
        ll aux = a.second;
        ll aux2 = a.second+2*b.second;
        a = ii((b.first>>1)-1,aux);
        b = ii((b.first>>1),aux2);
      }
      k2 <<= 1;
//       cerr << k2 << '\n';
//       cerr << a.first << ' ' << a.second << ' ' << b.first << ' ' << b.second << '\n';
    }
    ll x= k-(k2-1);
    if(x <= b.second) cout << "Case #" << cass << ": " << (b.first>>1) << ' ' << b.first-(b.first>>1)-1 << '\n';
    else cout << "Case #" << cass << ": " << (a.first>>1) << ' ' << a.first-(a.first>>1)-1 << '\n';
  }
}