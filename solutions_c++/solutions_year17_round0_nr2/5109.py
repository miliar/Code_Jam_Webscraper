#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <cassert>
using namespace std;
#define rep(i,n) for(int i=1;i<=(n);++i)
#define rep2(i,a,b) for(int i=(a);i<=(b);++i)
char ns[101];
long long tdp[20][10][2];
void task()
{
	ns[0]=0;
	scanf("%s",ns+1);
	int n=strlen(ns+1);
	memset(tdp,-1,sizeof tdp);
	tdp[0][0][1]=0;
	rep2(i,0,n-1)
	{
		rep2(id,0,9)
		{
			rep2(ib,0,1)
			{
				if(tdp[i][id][ib]==-1)continue;
				bool tb=false;
				rep2(td,0,9)
				{
					if(ib&&td>ns[i+1]-'0')continue;
					if(td<id)continue;
					if(ib&&td==ns[i+1]-'0')tb=true;
					tdp[i+1][td][tb]=max(tdp[i+1][td][tb],tdp[i][id][ib]*10+td);
				}
			}
		}
	}
	long long tmax=-1;
	rep2(id,0,9)
	{
		rep2(ib,0,1)
		{
			tmax=max(tmax,tdp[n][id][ib]);
		}
	}
	cout<<tmax<<endl;
					
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt){printf("Case #%d: ",i);task();}
}
