#include<bits/stdc++.h>
#define F first
#define S second
#define N 1005
using namespace std;
typedef pair<int,int> P;
long double dp[N][N];

int main(){
  
  int T;
  cin>>T;
  
  for(int t=1;t<=T;t++){
    
    int n,k;
    
    cin>>n>>k;

    P RH[N];
    
    for(int i=0;i<n;i++) cin>>RH[i].F>>RH[i].S;

    sort(RH,RH+n,greater<P>());
        
    memset(dp,0,sizeof(dp));

    for(int i=0;i<n;i++)dp[i][0]=M_PI*RH[i].F*RH[i].F;
    
    for(int i=0;i<n;i++){
      for(int j=0;j<n;j++){
	
	if(!dp[i][j])continue;
	
	dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+2.0*M_PI*RH[i].F*RH[i].S);
	if(j)dp[i+1][j]=max(dp[i+1][j],dp[i][j]);
	
      }
    }

    cout<<"Case #"<<t<<": ";
    printf("%.7Lf\n",dp[n][k]);
  }
  
  return 0;
}
