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
int n,p;
int arr[111];
int cnt[5];

int dp[103][103][103][103][5];

int solve(int c1,int c2,int c3,int c4,int rem){
  if(c1+c2+c3+c4==0)return 0;
  int &ret=dp[c1][c2][c3][c4][rem];
  if(~ret)return ret;
  ret=0;
  if(c1)ret=max(ret,solve(c1-1,c2,c3,c4,(rem+0)%p));
  if(c2)ret=max(ret,solve(c1,c2-1,c3,c4,(rem+1)%p));
  if(c3)ret=max(ret,solve(c1,c2,c3-1,c4,(rem+2)%p));
  if(c4)ret=max(ret,solve(c1,c2,c3,c4-1,(rem+3)%p));
  ret+=(rem==0);
  return ret;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("A-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  sc(T);
  for(int C=1;C<=T;++C){
    sc(n),sc(p);
    memset(cnt,0,sizeof cnt);
    for(int i=0;i<n;++i){
      sc(arr[i]);
      cnt[arr[i]%p]++;
    }
    memset(dp,-1,sizeof dp);
    printf("Case #%d: %d\n",C,solve(cnt[0],cnt[1],cnt[2],cnt[3],0));
  }
}




