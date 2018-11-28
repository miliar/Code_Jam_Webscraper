#include <stdio.h>
#include <cstring>
#include <string>
#include <algorithm>

using namespace std;
const int N=51;
double p[N];
double solve(int n, int k, double u)
{
  double l(0), r(1.0);
  int cnt=0;
  while(cnt++<500){
    double mid=(l+r)/2.0;
    double add(0.0);
    for(int i = 0; i < n; ++i){
      if(p[i]<mid){
        add += mid - p[i];
      }
    }
    if(add>u){
      r=mid;
    }else{
      l=mid;
    }
  }
  double res=1.0;
  for(int i = 0; i < n; ++i){
    if(p[i]<l) res *= l;
    else res *= p[i];
  }
  return res;
}

int main()
{
  freopen("C-small-1-attempt1.in","r",stdin);
  freopen("C-small-1-attempt1.out","w",stdout);
  int test,cas(1);
  scanf("%d",&test);
  while(test--){
    int n,k;
    double u;
    scanf("%d%d",&n,&k);
    scanf("%lf",&u);
    for(int i=0;i<n;++i) scanf("%lf",p+i);
    printf("Case #%d: %.6lf\n",cas++,solve(n,k,u));
  }

  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
