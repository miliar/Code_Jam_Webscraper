#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <deque>
using namespace std;
const int MAX_N = 30;
const int INF=1500000000;
char s[MAX_N][MAX_N];
int t[MAX_N];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Q,n,m;
	cin>>Q;
	for (int q1=1;q1<=Q;q1++)
	{
		cin>>n>>m;
		for (int i=0;i<MAX_N;i++)
			t[i]=0;
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
			{
				cin>>s[i][j];
				if (s[i][j]!='?')
					t[s[i][j]-'A']++;
			}
		}
		for(int k=0;k<MAX_N;k++)
		{
			if (t[k]>0)
			{
				int x1,x2,y1,y2;
				x1=x2=y1=y2=-1;
				for (int i=0;i<n;i++)
				{
					for (int j=0;j<m;j++)
					{
						if (s[i][j]==k+'A')
						{
							if (x1==-1)
							{
								x1=x2=i;
								y1=y2=j;
							}
							x1=min(x1,i);
							x2=max(x2,i);
							y1=min(y1,j);
							y2=max(y2,j);
						}
					}
				}
				for (int i=x1;i<=x2;i++)
				{
					for (int j=y1;j<=y2;j++)
					{
						s[i][j]=k+'A';
					}
				}
				int w=1;
				while (w==1)
				{
					w=0;
					int a=0;
					/*----------------------*/
					for (int j=y1;x1>0&&j<=y2;j++)
					{
						if (s[x1-1][j]=='?')
							a++;
					}
					if (a==y2-y1+1)
					{
						for (int j=y1;j<=y2;j++)
							s[x1-1][j]=k+'A';
						x1--;
						w=1;
					}
					/*----------------------*/
					a=0;
					for (int j=y1;x2+1<n&&j<=y2;j++)
					{
						if (s[x2+1][j]=='?')
							a++;
					}
					if (a==y2-y1+1)
					{
						for (int j=y1;j<=y2;j++)
							s[x2+1][j]=k+'A';
						x2++;
						w=1;
					}
					/*----------------------*/
					a=0;
					for (int i=x1;y1>0&&i<=x2;i++)
					{
						if (s[i][y1-1]=='?')
							a++;
					}
					if (a==x2-x1+1)
					{
						for (int i=x1;i<=x2;i++)
							s[i][y1-1]=k+'A';
						y1--;
						w=1;
					}
					/*----------------------*/
					a=0;
					for (int i=x1;y2+1<m&&i<=x2;i++)
					{
						if (s[i][y2+1]=='?')
							a++;
					}
					if (a==x2-x1+1)
					{
						for (int i=x1;i<=x2;i++)
							s[i][y2+1]=k+'A';
						y2++;
						w=1;
					}
				}
			}
		}
		cout<<"Case #"<<q1<<":\n";
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
			{
				if (s[i][j]=='?')
					return 0;
				cout<<s[i][j];
			}
			cout<<endl;
		}
	}
	return 0;
}