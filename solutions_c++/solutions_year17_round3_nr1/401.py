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

const double pii=pi;

int T;
int n,k;
pair<int,int> arr[1010];
double dp[1010][1010];

double getSurA(int r,int h){
  return (2*pii*r*h);
}

double getFaA(int r){
  return (pii*r*r);
}

bool cmp(pair<int,int> a,pair<int,int> b){
  return a.F>b.F;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("A-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  sc(T);
  for(int C=1;C<=T;++C){
    scanf("%d%d",&n,&k);
    for(int i=0;i<n;++i)
      sc(arr[i].F),sc(arr[i].S);
    sort(arr,arr+n,cmp);
    double out=0;
    for(int i=0;i<n;++i)
      dp[1][i]=getSurA(arr[i].F,arr[i].S)+getFaA(arr[i].F),
      out=max(out,dp[1][i]);
    for(int w=2;w<=k;++w)
      for(int i=0;i<n;++i){
        dp[w][i]=0;
        for(int j=0;j<i;++j)
          dp[w][i]=max(dp[w][i],dp[w-1][j]+getSurA(arr[i].F,arr[i].S));
        out=max(out,dp[w][i]);
      }
    printf("Case #%d: %.9f\n",C,out);
    //cout<<fixed<<setprecision(9)<<out<<"\n";
  }
}
