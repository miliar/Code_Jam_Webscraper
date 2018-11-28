#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
typedef long double ld;
int main(){
  freopen("al.in","r",stdin);
  freopen("al.out","w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    printf("Case #%d: ",tt);
    int d,n;
    scanf("%d %d",&d,&n);
    vector<int>x(n);
    vector<int>s(n);
    ld ls=-1;
    for(int i=0;i<n;i++){
      scanf("%d %d",&x[i],&s[i]);
      ld bet=(ld(d)*ld(s[i]))/(ld(d)-ld(x[i]));
      if(i==0 || bet<ls)ls=bet;
    }
    cout<<setprecision(9)<<fixed<<ls<<endl;
    continue;
/*
    ld li=*min_element(s.begin(),s.end());
    ld ls=*max_element(s.begin(),s.end());
    cout<<"li="<<li<<" ls="<<ls<<endl;
    double ans;
    for(int it=0;it<60;it++){
      ld v=(li+ls)*0.5;
      bool ok=true;
      for(int i=0;i<n;i++)if(s[i]<v){
        ld lft=ld(x[i])*v;
        ld rht=ld(d)*(v-ld(s[i]));
        if(lft<rht){
          ok=false;
          break;
        }
      }
      cout<<"v="<<v<<" ok="<<ok<<endl;
      if(ok)ans=v,li=v;
      else ls=v;
    }
    printf("%.9lf\n",ans);
    */
  }
  return 0;
}
