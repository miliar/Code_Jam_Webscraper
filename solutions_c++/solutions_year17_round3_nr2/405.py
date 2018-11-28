#include <bits/stdc++.h>
using namespace std;

#define EPS      1e-9
#define F        first
#define S        second
#define pi       acos(-1)
#define ll       long long
#define inf      0x3f3f3f3f
#define sz(x)    (int)x.size()
#define sc(x)    scanf("%d",&x)
#define all(x)   x.begin(),x.end()
#define rall(x)  x.rbegin(),x.rend()

int T;
int n,m,l,r;
int arr[1500];
int dp[1500][800][4][4];

int solve(int i,int cnt,int lst,int f){
  if(i==1440)return (cnt==720?(lst!=f):5555);
  if(cnt>720)return 5555;
  int &ret=dp[i][cnt][lst][f];
  if(~ret)return ret;
  ret=5555;
  if((arr[i]&1)!=0)ret=min(ret,solve(i+1,cnt+1,1,(i==0?1:f))+((lst&1)==0));
  if((arr[i]&2)!=0)ret=min(ret,solve(i+1,cnt,2,(i==0?2:f))+((lst&2)==0));
  return ret;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  sc(T);
  for(int C=1;C<=T;++C){
    sc(n),sc(m);
    for(int i=0;i<1444;++i)arr[i]=3;
    for(int i=0;i<n;++i){
      sc(l),sc(r);
      for(int j=l;j<r;++j)
        arr[j]=1;
    }
    for(int i=0;i<m;++i){
      sc(l),sc(r);
      for(int j=l;j<r;++j)
        arr[j]=2;
    }
    memset(dp,-1,sizeof dp);
    printf("Case #%d: %d\n",C,solve(0,0,3,0));
  }
}
