#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iostream>

using namespace std;

int main(){
  int T;
  int N,K;
  long long R[1000],H[1000];
  long long prod[1000];

  scanf("%d",&T);

  for(int tc = 1;tc <= T;++tc){
    scanf("%d %d",&N,&K);

    for(int i = 0;i < N;++i)
      scanf("%lld %lld", &R[i], &H[i]);

    for(int i = 0;i < N;++i)
      for(int j = i + 1;j < N;++j)
        if(R[i] > R[j]){
          swap(R[i], R[j]);
          swap(H[i], H[j]);
        }

    double best = 0;

    for(int j = K - 1;j < N;++j){
      double ans = M_PI * R[j] * R[j] + 2 * M_PI * R[j] * H[j];

      for(int i = 0;i < j;++i){
        prod[i] = R[i] * H[i];
      }

      sort(prod, prod + j);

      for(int i = j - 1;i >= j - (K - 1);--i){
        ans += 2 * M_PI * prod[i];
      }
      if(ans >= best) best = ans;
    }

    printf("Case #%d: %.8f\n", tc, best);
  }

  return 0;
}
