#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)

typedef long long ll;


ll solve(ll n,ll k){
  bool ng=(n%2==0),kg=(k%2==0);
  if(k==1){
    if(ng) return n-1;
    else return n-1;
  }
    
  if(!ng&&!kg) return solve((n-1)/2,(k-1)/2);
  else if(!ng&&kg) return solve((n-1)/2,(k-1)/2 + 1);
  else if(ng&&!kg){
    return solve(n/2-1,(k-1)/2);
  }
  else if(ng&&kg){
    if(k==2)  return solve(n/2, 1);
    else return solve(n/2,k/2);
  }
  return -10;
}

int main(){
  ll t;
  cin >> t;
  rep(i,t){
  ll n,k;
  cin >> n >> k;
  ll ans = solve(n,k);
  cout << "Case #" << i+1 << ": " << ((ans%2==0) ? ans/2 : ((ans/2)+1)) << " " << ans/2 << endl;
  }
  return 0;
}
