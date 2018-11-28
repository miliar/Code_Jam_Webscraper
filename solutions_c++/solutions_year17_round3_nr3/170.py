//gcj problems are extremely easy
#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
const int mx=55;
double p[mx];
int main(){
  freopen("cs.in","r",stdin);
  freopen("cs.out","w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    int n,k;
    double u;
    scanf("%d %d %lf",&n,&k,&u);
    for(int i=0;i<n;i++)scanf("%lf",p+i);
    double li=0.0,ls=1.0;
    double ans=0.0;
    for(int it=0;it<60;it++){
      double at=(li+ls)*0.5;
      double bet=1.0;
      double rem=u;
      bool can=true;
      for(int i=0;i<n;i++){
        if(p[i]<at){
          if(at-p[i]<=rem){
            rem-=(at-p[i]);
            bet*=at;
          }
          else{
            can=false;
            break;
          }
        }
        else bet*=p[i];
      }
      if(can)ans=max(ans,bet),li=at;
      else ls=at;
    }
    printf("Case #%d: %lf\n",tt,ans);
  }
  return 0;
}
