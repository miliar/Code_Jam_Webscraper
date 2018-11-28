//gcj problems are very easy
#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
struct ival{
  int l,r;
  bool operator <(ival x)const{
    return r<x.l;
  }
};
const int oo=1e9;
vector<ival>alice,bob;
const int mx=1500;
int last;
int f[mx][2][mx];
bool inside(int t,vector<ival>&d){
  ival tt={t,t};
  int at=lower_bound(d.begin(),d.end(),tt)-d.begin();
  if(at<(int)d.size() && d[at].l<=t && t<=d[at].r)return true;
  return false;
}
int solve(int i,int bef,int ta){
  if(f[i][bef][ta]!=-1)return f[i][bef][ta];
  int tb=i-ta;
  if(i==1439){
    if(last==0 && inside(i,alice))return oo;
    if(last==1 && inside(i,bob))return oo;
    if(last==0 && ta+1!=720)return oo;
    if(last==1 && tb+1!=720)return oo;
    return last!=bef; 
  }
  f[i][bef][ta]=oo;
  bool ina=inside(i,alice);
  bool inb=inside(i,bob);
  if(!ina && ta<720)f[i][bef][ta]=min(f[i][bef][ta],solve(i+1,0,ta+1)+(bef!=0));
  if(!inb && tb<720)f[i][bef][ta]=min(f[i][bef][ta],solve(i+1,1,ta)+(bef!=1));
  return f[i][bef][ta];
}
int main(){
  freopen("bl.in","r",stdin);
  freopen("bl.out","w",stdout);
  int t;
  scanf("%d",&t);
  for(int tt=1;tt<=t;tt++){
    int n,m;
    scanf("%d %d",&n,&m);
    alice.resize(n);
    bob.resize(m);
    for(int i=0;i<n;i++){
      scanf("%d %d",&alice[i].l,&alice[i].r);
      alice[i].r--;
    }
    for(int i=0;i<m;i++){
      scanf("%d %d",&bob[i].l,&bob[i].r);
      bob[i].r--;
    }
    sort(alice.begin(),alice.end());
    sort(bob.begin(),bob.end());
    int ans=oo;
    for(last=0;last<2;last++){
      memset(f,-1,sizeof f);
      int bet=solve(0,last,0);
      ans=min(ans,bet);
    }
    printf("Case #%d: %d\n",tt,ans);
  }
  return 0;
}
