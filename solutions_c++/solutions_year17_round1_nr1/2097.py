#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

const int maxn=40;

char G[maxn][maxn];

void fun()
{
	int R,C;
	scanf("%d %d",&R,&C);
	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
            cin>>G[i][j];

	for(int i=0;i<R;i++)
		for(int j=0;j<C;j++)
		{
			if(G[i][j]=='?' && i>0)
				G[i][j]=G[i-1][j];
		}


    for(int i=R-1;i>=0;i--)
		for(int j=0;j<C;j++)
		{
			if(G[i][j]=='?' && i<R-1)
				G[i][j]=G[i+1][j];
		}

	for(int j=0;j<C;j++)
		for(int i=0;i<R;i++)
		{
			if(G[i][j]=='?' && j>0)
				G[i][j]=G[i][j-1];
		}

    for(int j=C-1;j>=0;j--)
		for(int i=0;i<R;i++)
		{
			if(G[i][j]=='?' && j<C-1)
				G[i][j]=G[i][j+1];
		}
	for(int i=0;i<R;i++)
	{
		for(int j=0;j<C;j++)
			printf("%c",G[i][j]);
		printf("\n");
	}

}

void solve()
{
	int t;
	scanf("%d",&t);
	for(int id=1;id<=t;id++)
    {
        printf("Case #%d:\n",id);
        fun();
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    solve();
    return 0;
}
