//In the Name of God
//Ya Ali

#include<bits/stdc++.h>

#define int long long

#define ld long double

#define pb push_back

#define err(A) cout<<#A<<" = "<<(A)<<endl

using namespace std;

const int inf=1e17;

const int maxn=111;

int n;
int a[maxn],b[maxn];

int d[maxn][maxn];

ld c[maxn][maxn];

int32_t main()
{
  ios::sync_with_stdio(0);cin.tie(0);

  int T;
  cin>>T;
  for(int t=0;t<T;t++)
    {
      int n,q;
      cin>>n>>q;

      for(int i=0;i<n;i++)
	cin>>a[i]>>b[i];

      for(int i=0;i<n;i++)
	for(int j=0;j<n;j++)
	  {
	    cin>>d[i][j];
	    if(d[i][j]==-1)
	      d[i][j]=inf;
	    if(i==j)
	      d[i][j]=0;
	  }

      for(int k=0;k<n;k++)
	for(int i=0;i<n;i++)
	  for(int j=0;j<n;j++)
	    d[i][j]=min(d[i][j],d[i][k]+d[k][j]);

      for(int i=0;i<n;i++)
	for(int j=0;j<n;j++)
	  if(d[i][j]<=a[i])
	    {
	      c[i][j]=(ld)d[i][j]/b[i];
	    }
	  else
	    {
	      c[i][j]=inf;
	    }

      for(int k=0;k<n;k++)
	for(int i=0;i<n;i++)
	  for(int j=0;j<n;j++)
	    c[i][j]=min(c[i][j],c[i][k]+c[k][j]);

      cout<<setprecision(12)<<fixed;
      cout<<"Case #"<<t+1<<": ";
      for(int v,u;q--;)
	{
	  cin>>v>>u;
	  v--,u--;
	  cout<<c[v][u]<<" ";
	}
      cout<<endl;
    }  
  return 0;
}
