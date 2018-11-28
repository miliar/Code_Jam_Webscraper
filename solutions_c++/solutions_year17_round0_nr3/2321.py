#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;
pair<long long, long long> solve(long long n, long long k){
  int ln = 0;
  while( k > 1ll<<ln ){
    k -= 1ll<<ln;
    n -= 1ll<<ln;
    ln++;
  }
  long long m = n/(1ll<<ln);
  if ( k <= n - m*(1ll<<ln) )
    return make_pair((m+1)/2, m/2);
  return make_pair(m/2,(m-1)/2);
}
int main(){
  int T;
  long long n, k;
  scanf("%d",&T);
  for(int i = 0; i < T; ++i){
    scanf("%lld%lld", &n, &k);
    pair<long long,long long> rc = solve(n, k);
    printf("Case #%d: %lld %lld\n", i+1, rc.first, rc.second);
  }
}
