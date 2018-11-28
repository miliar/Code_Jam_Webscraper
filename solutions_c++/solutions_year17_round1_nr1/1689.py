#include <iostream>
#include <utility>
#include <algorithm>
#include <cstdlib>
#include <map>
#define ii pair<int,int>
#define ll long long
using namespace std;





int R,C;
char M[25][25];


void showit()
{
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
			{cerr<<M[i][j];if(j==C-1)cerr<<'\n';
			}
	cerr<<"__________\n";
}

void dp(int j)
{
	int i=0;
	while(M[i][j]=='?')i++;
	if(i==R)
	{
		for(int k=0;k<R;k++)M[k][j]=M[k][j-1];
	}
	else
	{
		for(int k=0;k<i;k++)M[k][j]=M[i][j];
		int p=i+1;
		while(i<R && p<R)
		{
			if(M[p][j]=='?')M[p][j]=M[i][j];
			else i=p,p++;
		}
	}


	//showit();
}

void solve(int t)
{
	int x;
	bool flag=1;
	for(int j=0;j<C;j++)
	{
		for(int i=0;i<R;i++)
		{
			if(M[i][j]!='?'){x=j;flag=0;break;}
		}
		if(!flag)break;
	}
	for(int k=x;k<C;k++)dp(k);
		//showit();
	for(int j=0;j<=x-1;j++)
	{
		for(int i=0;i<R;i++)M[i][j]=M[i][x];
	}
//showit();
	
	cout<<"Case #"<<t<<":\n";
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
			{cout<<M[i][j];if(j==C-1)cout<<'\n';
			}

}

int main()
{
	freopen ("A-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int tc;string s;
	cin>>tc;for(int t=1;t<=tc;t++)
	{
		cin>>R>>C;
		for(int i=0;i<R;i++)
		{
			cin>>s;
			for(int j=0;j<C;j++)
				M[i][j]=s[j];
		}
		solve(t);
	}


}