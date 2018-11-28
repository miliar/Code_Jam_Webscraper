#include <bits/stdc++.h>
using namespace std;
int t,tt;
long long n,m,x,y,z;
int main() {
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%lld%lld",&n,&m);
    map<long long, long long> all;
    all[-n]=1;
    while (!all.empty()) {
      auto it=all.begin();
      x=-it->first-1;
      z=it->second;
      all.erase(it);
      y=x/2;
      x-=y;
      m-=z;
      if (m<=0) {
        printf("Case #%d: %lld %lld\n",t,x,y);
        break;
      }
      if (x>0) all[-x]+=z;
      if (y>0) all[-y]+=z;
    }
  }
  return 0;
}

