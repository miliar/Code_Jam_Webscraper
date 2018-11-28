//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define me dp[i][j][k]

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

int dp[101][101][101];

int A[5];

void reset()
{
  A[0]=A[1]=A[2]=A[3]=0;
}

int main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      reset();

      int n,p;
      cin>>n>>p;
      for(int g,i=0;i<n;i++)
	{
	  cin>>g;
	  A[g%p]++;
	}
      memset(dp,0,sizeof dp);
      for(int i=0;i<=100;i++)
	for(int j=0;j<=100;j++)
	  for(int k=0;k<=100;k++)
	    {
	      if(i)
		me=max(dp[i-1][j][k]+(((i-1)*1+(j)*2+(k)*3)%p==0),me);
	      if(j)
		me=max(dp[i][j-1][k]+(((i)*1+(j-1)*2+(k)*3)%p==0),me);
	      if(k)
		me=max(dp[i][j][k-1]+(((i)*1+(j)*2+(k-1)*3)%p==0),me);
	    }
      cout<<"Case #"<<t<<": "<<dp[A[1]][A[2]][A[3]]+A[0]<<endl;
    }
  
  return 0;
}
