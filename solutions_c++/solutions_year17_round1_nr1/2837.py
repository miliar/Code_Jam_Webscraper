#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
#define pb push_back
int main()
{
	int t;
	cin>>t;
	for(int case1=1;case1<=t;case1++)
	{
		int r,c;
		cin>>r>>c;
		char s[r][c+2];
		for(int i=0;i<r;i++)
			scanf("%s",s[i]);
		vector<int> v[r];
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(s[i][j]!='?')
				{
					v[i].pb(j);
				}
			}
		}
		for(int i=0;i<r;i++)
		{
			int pos,flag=0;
			for(vector<int>::iterator it=v[i].begin();it!=v[i].end();it++)
			{
				flag=1;
			    pos=*it;
				for(int j=pos-1;j>=0;j--)
				{
					if(s[i][j]!='?')break;
					s[i][j]=s[i][pos];
				}
			}
			if(flag==1)
			{
				for(int j=pos+1;j<c;j++)s[i][j]=s[i][pos];
			}
	}
		vector<int>par;
		for(int i=0;i<r;i++)
		{
			if(s[i][0]!='?')par.pb(i);
		}
		for(vector<int>::iterator it=par.begin();it!=par.end();it++)
		{
			int pos=*it;
			for(int k=pos+1;k<r;k++)
			
			{
				if(s[k][0]=='?')
				{
					for(int j=0;j<c;j++)
						s[k][j]=s[pos][j];
				}
				else break;
			}
		}
	
		if(s[0][0]=='?')
		{
			int pos=par[0];
			for(int i=0;i<r;i++)
			{
				if(s[i][0]=='?')
				{
					for(int j=0;j<c;j++)
						s[i][j]=s[pos][j];
				}
				else break;
			}
		}
		printf("Case #%d:\n",case1);
		for(int i=0;i<r;i++)
			printf("%s\n",s[i]);
	}

	return 0;
}
