//g++ -std=c++11 -g -O2 -o ./a ./A.cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define ff first
#define ss second
#define nl '\n'
//////////////////////////////////////////////////////////////////////

//C,J 0/1
const int N = 210;
int ac,aj,n;

int at[2000];
int dp[2000][2000][2];
const int INF = 1e9;

bool st;
int f(int t,int del,bool w){
  //cerr<<t<<','<<del<<endl;

  if(t==1440){
    if(del==0){
      return dp[t][del+750][w]=(w==st?0:1);
    }
    return dp[t][del+750][w]=INF;
  }
  if(dp[t][del+750][w] != -1)return dp[t][del+750][w];

  int ret = INF;

  if(at[t] == 1){
    if(w){
      ret = f(t+1,del+1,1);
    }else{
      ret = f(t+1,del+1,1)+1;
    }
  }else if(at[t] == 2){
    if(w){
      ret = f(t+1,del-1,0)+1;
    }else{
      ret = f(t+1,del-1,0);
    }
  }else{
    if(w){
      ret = min( f(t+1,del+1,1) , f(t+1,del-1,0)+1 );
    }else{
      ret = min( f(t+1,del-1,0) , f(t+1,del+1,1)+1 );
    }
  }

  return dp[t][del+750][w] = ret;
}

int main(){
  ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);  
  int tc;cin>>tc;
  for(int tt=1;tt<=tc;tt++){
    cout<<"Case #"<<tt<<": ";
    
    cin>>ac>>aj;
    n = ac + aj;
    int u,v;
    

    memset(at,0,sizeof at);
    for(int i=1;i<=ac;i++){
      cin>>u>>v;
      for(int j=u;j<v;j++)at[j] = 1;
    }    
    for(int i=ac+1;i<=ac+aj;i++){
      cin>>u>>v;
      for(int j=u;j<v;j++)at[j] = 2;
    }
    memset(dp,-1,sizeof dp);
    st = 0;int ans = f(0,0,st);
    memset(dp,-1,sizeof dp);
    st = 1;ans = min(ans,f(0,0,st));

    cout<<ans<<endl;
    cerr<<ans<<endl;
  }
  return 0;
}
