#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
typedef long long int ll;
#define MAXN 2000

void solve()
{
  ll N,K;
  scanf("%lld %lld",&N,&K);
  std::map<ll,ll,std::greater<ll> > intervalli;//largezza,freq
  intervalli[N]=1;
  K--;
  while(K>=intervalli.begin()->second)
  {
    K-=intervalli.begin()->second;
    ll l=intervalli.begin()->first;l--;
    intervalli[l/2]+=intervalli.begin()->second;
    intervalli[(l+1)/2]+=intervalli.begin()->second;
    intervalli.erase(intervalli.begin());
  }
  ll l=intervalli.begin()->first;l--;
  printf("%lld %lld\n",(l+1)/2,l/2);
}

int main()
{
  int T;
  scanf("%d\n",&T);
  for(int i=1;i<=T;i++){printf("Case #%d: ",i);solve();}
}
