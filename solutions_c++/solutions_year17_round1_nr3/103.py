#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

const int inf=10000000;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		int hd,ad,hk,ak,b,d;
		scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
		int ans=inf;
		for (int i=0;i<=100;i++)
		{
			int x1=hd,x2=ak,cnt=0;
			for (int j=1;j<=i;j++)
			{
				if (x1-(x2-d)>0)
				{
					x2=max(x2-d,0);
					x1-=x2;
				}
				else
				{
					cnt++;x1=hd-x2;
					if (x1-max(x2-d,0)<=0) {cnt=inf;break;}
					x2=max(x2-d,0);x1-=x2;
				}
				cnt++;
			}
			if (cnt==inf) continue;
			for (int j=0;j<=100;j++)
			{
				int t1=x1,t2=x2,t3=ad,cnt2=cnt;
				for (int k=0;k<j;k++)
				{
					if (t1-t2>0)
					{
						t1-=t2;t3+=b;
					}
					else
					{
						cnt2++;t1=hd-t2;
						if (t1-t2<=0) {cnt2=inf;break;}
						t1-=t2;t3+=b;
					}
					cnt2++;
				}
				if (cnt2==inf) continue;
				int t4=hk;
				
				while (1)
				{
					if (t4-t3<=0) {cnt2++;break;}
					if (t1-t2>0)
					{
						t4-=t3;t1-=t2;
					}
					else
					{
						cnt2++;t1=hd-t2;
						if (t1-t2<=0) {cnt2=inf;break;}
						t1-=t2;t4-=t3;
					}
					cnt2++;
				}
				ans=min(ans,cnt2);
			}
		}
		if (ans<inf) printf("Case #%d: %d\n",T,ans); else printf("Case #%d: IMPOSSIBLE\n",T);
	}
	return 0;
}

