#include <stdio.h> 
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

int N, M, k;
int R,C;

int min(int a, int b)
{
	if (a > b)return b;
	return a;
}
int max(int a, int b)
{
	if (a > b)return a;
	return b;
}
int abs(int a)
{
	if(a>0)return a;
	return -a;
}

const int MAXN = 30;
char A[MAXN][MAXN];
char ans[MAXN][MAXN];
int r[MAXN],c[MAXN];
int dont[MAXN][MAXN];

char findCol(int y, int x)
{
	for(int yy=y;yy>=0;yy--)
	{
		if(r[yy]==0)
			continue;
		for(int xx=x;xx>=0;xx--)
		{
			if(dont[yy][xx]==1)
				return A[yy][xx];
		}
		for(int xx=x+1;xx<C;xx++)
		{
			if(dont[yy][xx]==1)
				return A[yy][xx];
		}
	}
	for(int yy=y+1;yy<R;yy++)
	{
		if(r[yy]==0)
			continue;
		for(int xx=x;xx>=0;xx--)
		{
			if(dont[yy][xx]==1)
				return A[yy][xx];
		}
		for(int xx=x+1;xx<C;xx++)
		{
			if(dont[yy][xx]==1)
				return A[yy][xx];
		}
	}
	return 0;
}
int main()
{ 
	int tc, i;
	freopen("alarge.txt","r",stdin);
	freopen("alargeoutput.txt","w",stdout);

	scanf("%d",&tc);

	for(int t=1;t<=tc;t++)
	{
		
		memset(A,0,sizeof(A));
		memset(ans,0,sizeof(ans));
		memset(dont,0,sizeof(dont));
		memset(r,0,sizeof(r));
		memset(c,0,sizeof(c));

		scanf("%d%d",&R,&C);
		for(int i=0;i<R;i++)
		{
			scanf("%s",A[i]);
			for(int x=0;x<C;x++)
			{
				if(A[i][x]!=63)
				{
					ans[i][x]=A[i][x];
					r[i]=1,c[x]=1;
					dont[i][x]=1;
				}
			}
		}

		for(int y=0;y<R;y++)
		{
			if(r[y]==1)
			{
				for(int x=C-2;x>=0;x--)
				{
					if(dont[y][x])
						continue;
					ans[y][x] = ans[y][x+1];
				}
				for(int x=1;x<C;x++)
				{
					if(dont[y][x])
						continue;
					ans[y][x] = ans[y][x-1];
				}
			}
		}
		if(t==94)
		{
			int ccccccc=1;
		}
		for(int x=0;x<C;x++)
		{
			for(int y=0;y<R;y++)
			{
				if(r[y]==1)
					continue;

				
				char cc = findCol(y,x);
				for(int xx=x;xx>=0;xx--)
				{
					if(ans[y][xx]!=0)
						break;
					ans[y][xx] = cc;
				}
			}
		}
		

		printf("Case #%d:\n", t);
		for(int y=0;y<R;y++)
		{
			for(int x=0;x<C;x++)
			{
				printf("%c",ans[y][x]);
			}
			printf("\n");
		}
	}

	return 0;
}


