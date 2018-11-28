#include <stdio.h>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  freopen("A-large.in","r",stdin);
  freopen("A-large.out","w",stdout);
  int test,cas(1);
  scanf("%d",&test);
  while(test--){
    int n;
    double D;
    scanf("%lf%d",&D,&n);
    vector<pair<double,double> > p;
    for(int i = 0; i < n; ++i){
      double a,b;
      scanf("%lf%lf",&a,&b);
      p.push_back(make_pair(a,b)); 
    }
    p.push_back(make_pair(D,10000.0));
    sort(p.begin(),p.end());
    double speed(p[0].second),last_p(p[0].first);
    double t(0.0);
    for(int i = 0; i < p.size();++i){
      double tmp=(D-p[i].first)/p[i].second;
      t=max(tmp,t);
    }
    printf("Case #%d: %.6lf\n",cas++,D/t);
  }


  return 0;
}
/* sw=2;ts=2;sts=2;expandtab */
