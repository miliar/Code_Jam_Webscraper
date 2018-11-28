#include <bits/stdc++.h>
#define NINF INT_MIN 
#define INF INT_MAX
#define ull unsigned long long
#define ld long double
#define ll long long
#define M 1000000009
#define REM 4
#define N 100005
#define pll pair<ll,ll>
#define pb(x) push_back(x)
#define mset(a) memset(a,0,sizeof(a))
#define sc(x)  scanf("%c",&x)
#define si(a)  scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define f(i,n) for(i=0;i<n;i++)
#define foi(i,j,k) for(i=j;i<k;i++)
#define mll map<ll,ll>
#define foe(i,j,k) for(i=j;i<=k;i++)
 
#define dbg(x) cout<<#x<<"="<<x<<endl;
using namespace std;

 char grid[26][26];

int main()
{
	int i,j,r,c,cs=1,t;
	cin>>t;
	char ch;
	while(t--)
	{
		cin>>r>>c;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				cin>>grid[i][j];				
			}
		}
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(grid[i][j]=='?')
				{
					if(j>0)
					{
						grid[i][j]=grid[i][j-1];
					}
				}
			}

			for(j=c-1;j>=0;j--)
			{
				if(grid[i][j]=='?')
				{
					if(j<c-1)
					{
						grid[i][j]=grid[i][j+1];
					}
				}
			}
		}


		for(j=0;j<c;j++)
		{
			for(i=0;i<r;i++)
			{
				if(grid[i][j]=='?')
				{
					if(i>0)
					{
						grid[i][j]=grid[i-1][j];
					}
				}
			}

			for(i=r-1;i>=0;i--)
			{
				if(grid[i][j]=='?')
				{
					if(i<r-1)
					{
						grid[i][j]=grid[i+1][j];
					}
				}
			}
		}
		cout<<"Case #"<<cs<<": \n";
		cs++;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
				cout<<grid[i][j];
			cout<<endl;
		}
	}
	return 0;
}