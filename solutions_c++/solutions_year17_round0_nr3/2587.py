#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> P;
const ll mod = 1e9+7;

P calc(ll n,ll k){
  if(n == 1)
    return P(0,0);
  if(n == 2){
    if(k == 1)
      return P(1,0);
    else
      return P(0,0);
  }
  if(k == 1)
    return P(n/2,(n-1)/2);
  if((k-1)%2 == 1)
    return calc(n/2,k/2);
  return calc((n-1)/2,(k-1)/2);  
}

void solve(int case_num){
  printf("Case #%d: ",case_num);
  ll n,k;
  cin >> n >> k;
  P res = calc(n,k);
  cout << res.first << " " << res.second << endl;
}


int main(void){
  int n;
  cin >> n;
  for(int i = 0;i < n;++i){
    solve(i+1);
  }
  return 0;
}
