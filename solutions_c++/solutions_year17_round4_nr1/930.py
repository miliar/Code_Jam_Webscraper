#include<bits/stdc++.h>
using namespace std;

int dp[101][101][101];
int N;
int P;
int G[100];
int A[4];

int solve(){
  int X=A[1];
  int Y=A[2];
  int Z=A[3];
  for(int i=0;i<=X;i++)
    for(int j=0;j<=Y;j++)
      for(int k=0;k<=Z;k++)
        dp[i][j][k]=-1e9;

  int res=0;
  dp[0][0][0]=0;
  for(int i=0;i<=X;i++){
    for(int j=0;j<=Y;j++){
      for(int k=0;k<=Z;k++){
        
        if(i<X||j<Y||k<Z)    res=max(res,dp[i][j][k]+1);
        else res=max(res,dp[i][j][k]);
        
        int c=dp[i][j][k];

        if(i+P<=X){
          dp[i+P][j][k]=max(dp[i+P][j][k],c+1);
        }
        
        if(j+P<=Y){
          dp[i][j+P][k]=max(dp[i][j+P][k],c+1);
        }
        
        if(P==3){
          if(i+1<=X&&j+1<=Y){
            dp[i+1][j+1][k]=max(dp[i+1][j+1][k],c+1);
          }
        }
        
        if(P==4){        
          if(j+2<=Y){
            dp[i][j+2][k]=max(dp[i][j+2][k],c+1);
          }
          if(i+2<=X&&j+1<=Y){
            dp[i+2][j+1][k]=max(dp[i+2][j+1][k],c+1);
          }
          if(k+2<=Z&&j+1<=Y){
            dp[i][j+1][k+2]=max(dp[i][j+1][k+2],c+1);
          }
          if(k+4<=Z){
            dp[i][j][k+4]=max(dp[i][j][k+4],c+1);
          }
          if(i+1<=X&&k+1<=Z){
            dp[i+1][j][k+1]=max(dp[i+1][j][k+1],c+1);
          }
        }

        
      }
    }
  }

  return res;
}

int main(){
  int Tc;
  cin>>Tc;
  for(int tc=1;tc<=Tc;tc++){

    cin>>N>>P;

    for(int i=0;i<4;i++)A[i]=0;
    
    for(int i=0;i<N;i++){
      cin>>G[i];
      G[i]%=P;
      A[G[i]]++;
    }
    cout<<"Case #"<<tc<<": ";
    cout<<A[0]+solve()<<endl;
  }
  return 0;
}
