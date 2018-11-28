#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << #x << " = " << x << endl;


#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 10000

void solve(){
  ll n,k;
  map<ll,ll> mm;
  
  scanf("%lld%lld",&n,&k);

  priority_queue<pair<ll,pair<ll,ll> > > pq;

  mm[n] = 1;

  for(ll i=0;;){
    auto it = mm.end();
    it--;

    ll d = it->first;
    ll p = it->second;
    mm.erase(it);

    if(i >= k-p){
      printf("%lld %lld\n",d/2,d/2 - 1 + d%2);
      return;
    }
    
    i += p;
    
    if(d%2 == 0){
      mm[d/2-1] += p;
      mm[d/2] += p;
    }else{
      mm[d/2] += p*2;
    }
    
  }
  
}

int main(){
  int T;

  scanf("%d",&T);

  for(int i=1;i<=T;i++){

    printf("Case #%d: ",i);

    solve();
  }
  
  return 0;
}
