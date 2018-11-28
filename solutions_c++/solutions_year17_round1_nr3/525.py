#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
const int inf=1000000;
int tim;
int hd,ad,hk,ak,B,D;
int work(int now,int ak)
{
	int tp=tim,re=0;
	fo(i,1,1000)
	{
		if (now>=ak || tp==1)
		{
			re++;
			tp--;
			if (tp==0) return re;
			now-=ak;
		} else now=hd-ak,re++;
	}
	return inf;
}
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	int s=0;
	while (T--)
	{
		scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&B,&D);
		tim=(hk-1)/ad+1;
		if ( B ) 
		{
			hk--;
			for(int i=ad+1;i<=hk+1;)
			{
				int j=hk<i?0:hk/(hk/i);
				int re=(i-ad-1)/B+1;
				re+=hk/i+1;
				tim=min(tim,re);
				i=max(j+1,i+1);
			}
		}
		hd--;
		printf("Case #%d: ",++s);
		if (tim==1)
		{
			printf("1\n");
			continue;
		}
		int ans=inf,now=hd;
		fo(i,0,1000)
		{
			ans=min(ans,work(now,ak)+i);
			if (now>=ak-D)
			{
				ak=ak-D;
				ak=max(ak,0);
				now-=ak;
			} else
			{
				now=hd-ak;
				if (now<0) break;
			}
		}
		if (ans>=inf) printf("IMPOSSIBLE\n"); else printf("%d\n",ans);
	}
}














