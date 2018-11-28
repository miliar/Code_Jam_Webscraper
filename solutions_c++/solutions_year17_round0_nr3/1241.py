#include<stdio.h>
#include<map>
using namespace std;

void solve(int t) {
  long long n,k;
  map< long long, long long > M;

  scanf("%lld %lld",&n,&k);
  M[ n ]++;
  while(1) {
    long long kk = (--M.end())->second;
    long long p = (--M.end())->first;
    if(kk < k) {
      k -= kk;
      M.erase( --M.end() );
      M[ p/2 ] += kk;
      M[(p-1)/2] += kk;
    } else {
      printf("Case #%d: %lld %lld\n",t,p/2,(p-1)/2);
      break;
    }
  }
}


int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}