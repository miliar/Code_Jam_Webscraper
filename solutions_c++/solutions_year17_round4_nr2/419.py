#include<cstdio>
#include<cstring>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
const int N=11100;
int chan,n,c,m,a[N],num[N];
int check(int mid)
{
	int num=0;
	chan=0;
	fd(i,n,1)
	{
		int rem=mid,now=a[i];
		int tp=min(rem,now);
		rem-=tp;
		now-=tp;
		chan+=now;
		tp=min(num,rem);
		rem-=tp;
		num-=tp;
		num+=now;
	}
	return num==0;
}
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cs=0;
	while (T--)
	{
		scanf("%d%d%d",&n,&c,&m);
		memset(num,0,sizeof num);
		memset(a,0,sizeof a);
		int ans=0;
		fo(i,1,m)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			num[y]++;
			a[x]++;
		}
		int ans1;
		fo(i,1,c) ans=max(ans,num[i]);
		int l=ans,r=m;
		while (l<=r)
		{
			int mid=(l+r)>>1;
			if (check(mid)) ans=mid,ans1=chan,r=mid-1; else l=mid+1;
		}
		printf("Case #%d: %d %d\n",++cs,ans,ans1);
	}
}
