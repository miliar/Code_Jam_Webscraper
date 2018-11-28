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
int ning,npack;
int require[51];
int ipack[51][51];
int pointer[51];
void task()
{
	scanf("%d%d",&ning,&npack);
	rep(i,ning)
	{
		scanf("%d",&require[i]);
	}
	#define getlower(pack,require) (((pack)*10-1)/((require)*11)+1)
	#define getupper(pack,require) (((pack)*10)/((require)*9))
	rep(i,ning)
	{
		rep(j,npack)
		{
			scanf("%d",&ipack[i][j]);
		}
		sort(ipack[i]+1,ipack[i]+npack+1);
		pointer[i]=1;
		while(pointer[i]<=npack&&getupper(ipack[i][pointer[i]],require[i])==0)
			++pointer[i];
	}
	
	int tot=0;
	while(true)
	{
		int tl=0,tu=1999999999;
		rep(i,ning)
		{
			if(pointer[i]>npack)
			{
				printf("%d\n",tot);
				return;
			}
			tl=max(tl,getlower(ipack[i][pointer[i]],require[i]));
			tu=min(tu,getupper(ipack[i][pointer[i]],require[i]));
		}
		if(tu>=tl)
		{
			++tot;
			rep(i,ning)
				++pointer[i];
		}
		else
		{
			rep(i,ning)
			{
				if(getupper(ipack[i][pointer[i]],require[i])<tl)
				{
					++pointer[i];
					break;
				}
			}
		}
	}
		
}
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int nt;scanf("%d",&nt);
	rep(i,nt){printf("Case #%d: ",i);task();}
}
