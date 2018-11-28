//Author:- IITian_Sujal
//let's keep it simple and easy....
#include<bits/stdc++.h>
#define ll          long long int
#define mp          make_pair
#define pii         pair<int,int>
#define pb          push_back
#define vi          vector<int>
#define Max(a,b)    ((a)>(b)?(a):(b))
#define Min(a,b)    ((a)<(b)?(a):(b))
#define rep(i,a,b)  for (__typeof((b)) i=(a);i<(b);i+=1)
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define mod	        1000000007
#define endl        '\n'
using namespace std;

int main()
{
	freopen("1.txt","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin >>t;
	rep(u,1,t+1)
	{
		int  r,c;
		cin >>r>>c;
		char a[r][c];
		rep(i,0,r)
		{
			rep(j,0,c)
			{
				cin >>a[i][j];
			}
		}

		char last;
		rep(i,0,r)
		{
			last='?';
			rep(j,0,c)			
			{
				if(a[i][j]!='?')
				{
					last=a[i][j];
				}
				else
				{
					a[i][j]=last;
				}
			}
			for (int j = c-1; j>=0; j--)
			{
				if(a[i][j]!='?')
				{
					last=a[i][j];
				}
				else
				{
					a[i][j]=last;
				}
			}
		}
/*		rep(i,0,r)
		{
			rep(j,0,c)
			{
				cout<<a[i][j];
			}
			cout<<endl;
		}
		cout<<endl;*/
		rep(i,0,r)
		{
			int f=-1;
			rep(j,0,c)
			{
				if(a[i][j]=='?')
				{
					if(f==-1)
					{
						if(i+1<r&&a[i+1][j]!='?')
						{
							f=i+1;
						}
						if(i-1>=0&&a[i-1][j]!='?')
						{
							f=i-1;
						}						
					}
					if(f!=-1)
					a[i][j]=a[f][j];
				}
			}
		}
		
		for(int i=r-1;i>=0;i--)
		{
			int f=-1;
			rep(j,0,c)
			{
				if(a[i][j]=='?')
				{
					if(f==-1)
					{
						if(i+1<r&&a[i+1][j]!='?')
						{
							f=i+1;
						}
						if(i-1>=0&&a[i-1][j]!='?')
						{
							f=i-1;
						}						
					}
					if(f!=-1)
					a[i][j]=a[f][j];
				}
			}
		}
	cout<<"Case #"<<u<<":"<<endl;
	rep(i,0,r)
	{
		rep(j,0,c)
		{
			cout<<a[i][j];
		}
		cout<<endl;
	}
	}
}
