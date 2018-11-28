#include <stdio.h>
#include <cstring>
#include <map>

#define ll long long

ll n,k;

void run(int iter){
  scanf("%lld%lld\n", &n, &k);
  std::map<ll, ll> m;

  m.insert({n, 1});

  while(true){
    auto res = m.end();
    res--;
    ll l1 = (res->first-1)/2;
    ll l2 = (res->first-1)/2 + (res->first+1)%2;
    if (res->second<k) {
      k -= res->second;
      m[l1] += res->second;
      m[l2] += res->second;
      m.erase(res);
    }
    else{printf("Case #%d: %lld %lld\n", iter, l2, l1);return;}
  }
}

int main(){
  int t;
  scanf("%d", &t);
  for(int i=0;i<t;i++){
    run(i+1);
  }
}
