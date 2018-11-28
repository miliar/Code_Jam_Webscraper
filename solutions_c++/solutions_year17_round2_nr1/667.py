#include <bits/stdc++.h>
using namespace std;

int main()
{
  int T;
  scanf("%d",&T);
  for(int cs=1;cs<=T;cs++){
    long long D;
    int n;
    scanf("%lld%d",&D,&n);
    double M=0.;
    for(int i=0;i<n;i++){
      long long d,s;
      scanf("%lld%lld",&d,&s);
      M=max(M,(double)(D-d)/s);
    }
    printf("Case #%d: %.6lf\n",cs,(double)D/M);
  }
  return 0;
}
