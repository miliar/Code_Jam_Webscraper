#include<bits/stdc++.h>
using namespace std;

const int maxn=720;
int n[2],sum0,sum1,a[2][2000],dp[2000][2000][2][2],ans;

int main()
{
  int qw;
  cin>>qw;
  for(int q=1;q<=qw;q++)
    {
      cin>>n[0]>>n[1];
      memset(a,0,sizeof a);
      memset(dp,63,sizeof dp);
      for(int j=0;j<2;j++)
	for(int i=0;i<n[j];i++)
	  {
	    int tmp1,tmp2;
	    cin>>tmp1>>tmp2;
	    a[j][tmp1]++;
	    a[j][tmp2]--;
	  }
      sum0=a[0][0],sum1=a[1][0];
      if(!sum0) dp[0][1][0][0]=0;
      if(!sum1) dp[0][0][1][1]=0;
      for(int i=1;i<2*maxn;i++)
	{
	  sum0+=a[0][i],sum1+=a[1][i];
	  for(int j=0;j<=min(maxn,i+1);j++)
	    {
	      if(!sum0 && j>0){
		dp[i][j][0][0]=min(dp[i-1][j-1][0][0],dp[i-1][j-1][0][1]+1);
		dp[i][j][1][0]=min(dp[i-1][j-1][1][0],dp[i-1][j-1][1][1]+1);
	      }
	      if(!sum1)
		{
		  dp[i][j][0][1]=min(dp[i-1][j][0][0]+1,dp[i-1][j][0][1]);
		  dp[i][j][1][1]=min(dp[i-1][j][1][0]+1,dp[i-1][j][1][1]);
		}
	    }
	}
      ans=min(min(dp[2*maxn-1][maxn][0][0],dp[2*maxn-1][maxn][1][1]),min(dp[2*maxn-1][maxn][1][0]+1,dp[2*maxn-1][maxn][0][1]+1));
      cout<<"Case #"<<q<<": "<<ans<<endl;
    }
}
	    
