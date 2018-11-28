#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
int nx,ny;
char ind[31][31];
#define isc(c) (((c)>='A'&&(c)<='Z')||((c)>='a'&&(c)<='z'))
void task()
{
	scanf("%d%d",&nx,&ny);
	rep(i,nx)
	{
		scanf("%s",&ind[i][1]);
		//rep(j,ny)
		//{
			//if(ind[i][j]!='?')
			//	unfull[i]=true;
		//}
	}
	rep(i,nx)
	{
		rep(j,ny)
		{
			if(isc(ind[i][j-1])&&ind[i][j]=='?')
				ind[i][j]=ind[i][j-1];
		}
		for(int j=ny;j;--j)
		{
			if(isc(ind[i][j+1])&&ind[i][j]=='?')
				ind[i][j]=ind[i][j+1];
		}
	}
	rep(i,nx)
	{
		if(isc(ind[i-1][1])&&ind[i][1]=='?')
		{
			rep(j,ny)
				ind[i][j]=ind[i-1][j];
		}
	}
	for(int i=nx;i;--i)
	{
		if(isc(ind[i+1][1])&&ind[i][1]=='?')
		{
			rep(j,ny)
				ind[i][j]=ind[i+1][j];
		}
	}
	rep(i,nx)
	{
		rep(j,ny)
		{
			putchar(ind[i][j]);
		}
		putchar('\n');
	}
}
int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt){printf("Case #%d:\n",i);task();}
}
