#include <bits/stdc++.h>
using namespace std;

pair<long long,long long> ans(long long n,long long k)
{
  pair<long long,long long> ret;
  if(k==1){
    ret=make_pair(n/2,(n-1)/2);
  }
  else if(k%2==0){
    ret=ans(n/2,k/2);
  }
  else{
    ret=ans((n-1)/2,(k-1)/2);
  }
  return ret;
}

int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    long long n,k;
    scanf("%lld%lld",&n,&k);
    pair<long long,long long> ret=ans(n,k);
    printf("Case #%d: %lld %lld\n",cs,ret.first,ret.second);
  }
  return 0;
}
