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
string s;
int dp[25][15][2];

int solve(int i,int lst,int op){
  if(i==sz(s))return 1;
  int &ret=dp[i][lst][op];
  if(~ret)return ret;
  ret=0;
  for(int j=(op?9:s[i]-'0');j>=lst;--j)
    ret|=solve(i+1,j,op||(j<s[i]-'0'));
  return ret;
}

void build(int i,int lst,int op){
  if(i==sz(s))return;
  for(int j=(op?9:s[i]-'0');j>=lst;--j)
    if(solve(i+1,j,op||(j<s[i]-'0'))){
      printf("%d",j);
      build(i+1,j,op||(j<s[i]-'0'));
      return;
    }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("B-large.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif
  sc(T);
  for(int C=1;C<=T;++C){
    cin>>s;
    memset(dp,-1,sizeof dp);
    printf("Case #%d: ",C);
    if(solve(0,1,0))build(0,1,0);
    else  for(int i=1;i<sz(s);++i)
            printf("9");
    printf("\n");
  }
}
