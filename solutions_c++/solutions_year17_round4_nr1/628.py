#include<bits/stdc++.h>
using namespace std;
#define int long long
int dp[111][111][111];
int x[4];
int dfs(int a,int b,int c){
  if(a>x[1]||b>x[2]||c>x[3]) return -1;
  if(~dp[a][b][c]) return dp[a][b][c];
  int res=0;
  for(int i=0;i<=4;i++){
    for(int j=0;j<=4;j++){
      for(int k=0;k<=4;k++){
	if(i+j+k==0) continue;
	if((i*1+j*2+k*3)%4) continue; 
	res=max(res,dfs(a+i,b+j,c+k)+1);
      }
    }
  }
  if((a<x[1]||b<x[2]||c<x[3])) res=max(res,1LL);
  return dp[a][b][c]=res;
}
signed main(){
  int T;
  cin>>T;
  for(int t=1;t<=T;t++){
    int n,p;
    cin>>n>>p;
    int g[n];
    for(int i=0;i<n;i++) cin>>g[i];
    memset(x,0,sizeof(x));
    for(int i=0;i<n;i++) x[g[i]%p]++;
    cout<<"Case #"<<t<<": ";
    int ans=x[0];
    if(p==2){
      ans+=(x[1]+1)/2;
    }
    if(p==3){
      int k=min(x[1],x[2]);
      ans+=k;
      ans+=(x[1]-k+2)/3;
      ans+=(x[2]-k+2)/3;
    }
    if(p==4){
      memset(dp,-1,sizeof(dp));
      ans+=dfs(0,0,0);
    }
    cout<<ans<<endl;
  }
  return 0;
}
