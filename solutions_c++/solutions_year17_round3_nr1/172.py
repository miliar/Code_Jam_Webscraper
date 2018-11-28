//gcj problems are easy
#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
typedef long double ld;
const int mx=1e3+10;
const ld pi=acos(-1);
pair<int,int>rh[mx];
struct cake{
  uli r,h;
  bool operator <(cake x)const{
    return r*h<x.r*x.h;
  }
};
int main(){
    freopen("al.in","r",stdin);
    freopen("al.out","w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    int n,k;
    scanf("%d %d",&n,&k);
    for(int i=0;i<n;i++){
      scanf("%d %d",&rh[i].first,&rh[i].second);
    }
    multiset<cake>s;
    sort(rh,rh+n,greater<pair<int,int> >());
    ld ans=0.0;
    for(int i=n-1;i>=0;i--){
      ld bet=ld(2)*ld(rh[i].first)*ld(rh[i].second)+ld(rh[i].first)*ld(rh[i].first);
      if((int)s.size()>=k-1){
        auto it=s.end();        
        for(int i=0;i<k-1;i++){
          it--;
          bet+=ld(2)*ld(it->r)*ld(it->h);
        }
        ans=max(ans,bet);
      }
      s.insert({rh[i].first,rh[i].second}); 
    }
    ans=ans*pi;
    cout<<fixed<<setprecision(9)<<"Case #"<<tt<<": "<<ans<<endl;
  }
  return 0;
}
