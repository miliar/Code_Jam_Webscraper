#include <bits/stdc++.h>
#define ll long long int
#define sc scanf
#define pf printf
using namespace std;

ll gcd(ll x,ll y){
  if(x%y==0)return y;
  else return gcd(y,x%y);
}


int main(){

    freopen("A-large.in","r",stdin);
    freopen("home\\mukter\\Desktop\\contest\\outputFileName2.txt","w",stdout);
    int t;
    sc("%d",&t);

    for(int i=1;i<=t;i++){
      ll n,d;
      double max_time=-1;

      sc("%lld %lld",&d,&n);
      for(int j=1;j<=n;j++){
        ll x,y;
        sc("%lld %lld",&x,&y);
        double off=double(d-x)/(y*1.0);
        if(off>max_time)max_time=off;
      }
      double puter=(d*1.0);
      puter/=max_time;

      pf("Case #%d: %.6lf\n",i,puter);

    }
    return 0;
}
