#include<bits/stdc++.h>
#define mod 1000000007
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

using namespace std;
int r,c;
char cake[30][30];

bool rempty(int a)
{
	if(a<0||a>=r)
		return false;
	for(int i=0;i<c;i++)
		if(cake[r][i]!='?')
			return false;
	return true;
}

int main()
{
	int t,cs=0;
	scanf("%d",&t);
	while(t--)
	{	
		cs++;
		scanf("%d %d",&r,&c);
		for(int i=0;i<r;i++)
		{
			scanf("%s",cake[i]);
		}
		for(int i=0;i<r;i++)
		{
			for(int j=0;j<c;j++)
			{
				if(cake[i][j]!='?')
				{
					int b = j+1;
					while(b<c&&cake[i][b]=='?')
						cake[i][b] = cake[i][b-1],b++;
					b = j-1;
					while(b>=0&&cake[i][b]=='?')
						cake[i][b] = cake[i][b+1],b--;
				}
			}
		}
		for(int i=1;i<r;i++)
		{
			int re = 1;
			for(int j=0;j<c;j++)
			{
				if(cake[i][j]!='?')
					re=0;
			}
			if(re)
			{
				//cerr<<"copying "<<i-1<<" to "<<i<<endl;
				for(int j=0;j<c;j++)
				{
					cake[i][j] = cake[i-1][j];
				}
			}
		}
		for(int i=r-2;i>=0;i--)
		{
			int re = 1;
			for(int j=0;j<c;j++)
			{
				if(cake[i][j]!='?')
					re=0;
			}
			if(re)
			{
				//cerr<<"copying "<<i+1<<" to "<<i<<endl;
				for(int j=0;j<c;j++)
				{
					cake[i][j] = cake[i+1][j];
				}
			}
		}
		printf("Case #%d: \n",cs);
		for(int i=0;i<r;i++)
			printf("%s\n",cake[i]);
		
	}

	return 0;
}