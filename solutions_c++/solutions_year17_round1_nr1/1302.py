#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define ll long long
#define INF 1e18
#define pb push_back
#define f first
#define s second
char a[30][30];
int main()
{
	ll t;
	cin>>t;
	ll z=0;
	while(t--)
	{
		z++;
		cout<<"Case #"<<z<<":"<<endl;
		ll c,r;
		cin>>r>>c;
		for(int i=0;i<r;i++)
		{
			cin>>a[i];
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(a[i][j]=='?')
				{
					if(j-1>=0 && a[i][j-1]!='?')
					{
						a[i][j]=a[i][j-1];
					}
					else if(j+1<c && a[i][j+1]!='?')
					{
						a[i][j]=a[i][j+1];
					}
				}
			}
			for(int j=c-1;j>=0;j--)
			{
				if(a[i][j]=='?')
				{
					if(j-1>=0 && a[i][j-1]!='?')
					{
						a[i][j]=a[i][j-1];
					}
					else if(j+1<c && a[i][j+1]!='?')
					{
						a[i][j]=a[i][j+1];
					}	
				}
			}
		}
		for(int j=0;j<c;j++)
		{
			for(int i=0;i<r;i++)
			{
				if(a[i][j]=='?')
				{
					if(i-1>=0 && a[i-1][j]!='?')
					{
						a[i][j]=a[i-1][j];
					}
					else if(i+1<r && a[i+1][j]!='?')
					{
						a[i][j]=a[i+1][j];
					}
				}
			}
			for(int i=r-1;i>=0;i--)
			{
				if(a[i][j]=='?')
				{
					if(i-1>=0 && a[i-1][j]!='?')
					{
						a[i][j]=a[i-1][j];
					}
					else if(i+1<r && a[i+1][j]!='?')
					{
						a[i][j]=a[i+1][j];
					}
				}
			}
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				cout<<a[i][j];	
			}
			cout<<endl;
			
		}
	}
}