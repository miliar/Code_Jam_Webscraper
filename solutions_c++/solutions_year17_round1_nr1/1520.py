/******************************************
*    AUTHOR:         CHIRAG AGARWAL       *
*    INSTITUITION:   BITS PILANI, PILANI  *
******************************************/
#include <bits/stdc++.h>
using namespace std;
 
typedef long long LL; 
typedef long double LD;


string s[27];
int done[27][27];

int main() 
{
	int t;
	scanf("%d",&t);
	for(int tc=1;tc<=t;tc++)
	{
		int r,c;
		scanf("%d %d",&r,&c);
		for(int i=0;i<27;i++)
		{
			for(int j=0;j<27;j++)
			{
				done[i][j]=0;
			}
		}
		for(int i=0;i<r;i++)
		{
			cin>>s[i];
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(s[i][j]!='?')
				{
					done[i][j]=1;
					for(int k=i-1;k>=0;k--)
					{
						if(!done[k][j]&&s[k][j]=='?')
						{
							s[k][j]=s[i][j];
							done[k][j]=1;
						}
						else
						{
							break;
						}
					}
					for(int k=i+1;k<r;k++)
					{
						if(!done[k][j]&&s[k][j]=='?')
						{
							s[k][j]=s[i][j];
							done[k][j]=1;
						}
						else
						{
							break;
						}
					}
				}
			}
		}

		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(s[i][j]!='?')
				{
					done[i][j]=1;
					for(int k=j-1;k>=0;k--)
					{
						if(!done[i][k]&&s[i][k]=='?')
						{
							s[i][k]=s[i][j];
							done[i][k]=1;
						}
						else
						{
							break;
						}
					}
					for(int k=j+1;k<c;k++)
					{
						if(!done[i][k]&&s[i][k]=='?')
						{
							s[i][k]=s[i][j];
							done[i][k]=1;
						}
						else
						{
							break;
						}
					}

				}
			}
		}
		printf("Case #%d:\n",tc);
		for(int i=0;i<r;i++)
		{
			cout<<s[i]<<"\n";
		}
	}

	return 0;
}