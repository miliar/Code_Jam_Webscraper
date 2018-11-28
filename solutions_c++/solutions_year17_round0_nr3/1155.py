#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pii pair<int,int>
#define pll pair<ll,ll>
#define PB push_back
#define MP make_pair

void AddToMap(map< ll,ll >& m, ll n, ll x){
  if(n > 0)
    m[n] += x;
}

pll Solve(){
  ll n, k, x;
  map< ll, ll > m;
  pll ans;

  cin >> n >> k;
  x = 1;
  m.insert(MP(n, x));

  while(k){
    n = m.rbegin()->first;
    x = m.rbegin()->second;
    m.erase(n);

    ll mid = (n + 1) / 2;

    AddToMap(m, mid - 1, x);
    AddToMap(m, n - mid, x);

    k -= min(x, k);

    if(k == 0)
      ans = MP(n - mid, mid - 1);
  }

  return ans;
}

int main(){
  int t;
  cin >> t;
  for(int k = 1; k <= t; k++){
    pll ans = Solve();
    printf("Case #%d: %lld %lld\n", k, ans.first, ans.second);
  }
  return 0;
}
