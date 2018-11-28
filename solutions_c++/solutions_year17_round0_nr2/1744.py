#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll p10[19];

ll sol(ll n,ll dig,ll last){
  if(dig == 0){
    if(last <= n) return n;
    else return -1;
  }
  ll x = (n/p10[dig])%10;
  for(ll y = x; y >= last; --y){
    ll z;
    if(y == x) z = sol(n%p10[dig],dig-1,y);
    else z = sol(p10[dig]-1,dig-1,y);
    if(z != -1) return z+p10[dig]*y;
  }
  return -1;
}

int main(){
  ios::sync_with_stdio(false);
  p10[0] = 1;
  for(int i = 1; i < 19; ++i) p10[i] = p10[i-1]*10ll;
  int t; cin >> t;
  for(int cass = 1; cass <= t; ++cass){
    ll n; cin >> n;
    ll dig = 0;
    while(p10[dig] < n) ++dig;
    if(p10[dig] == n) cout << "Case #" << cass << ": " << max(1ll,n-1) << '\n';
    else cout << "Case #" << cass << ": " << sol(n,dig,0) << '\n';
  }
}