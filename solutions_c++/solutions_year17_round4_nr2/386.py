#include <bits/stdc++.h>
using namespace std;

const int MAXN=1005;

struct ticket
{
	int p,b;
}a[MAXN];

int n,m,cnt[MAXN],cntp[MAXN],tcnt[MAXN];

int check(int x)
{
	memcpy(tcnt,cnt,sizeof(cnt));
	int ret=0;
	for (int i=1;i<=n;i++)
		while (tcnt[i]>x)
		{
			bool flag=false;
			for (int k=1;k<i;k++)
				if (tcnt[k]<x)
				{
					flag=true;
					tcnt[k]++;
					tcnt[i]--;
					ret++;
					break;
				}
			if (!flag) return -1;
		}
	return ret;
}

void solve()
{
	int c;
	scanf("%d%d%d",&n,&c,&m);
	memset(cnt,0,sizeof(cnt));
	memset(cntp,0,sizeof(cntp));
	for (int i=0;i<m;i++)
	{
		int b,p;
		scanf("%d%d",&p,&b);
		cnt[p]++;
		cntp[b]++;
	}
	int l=1,r=m;
	for (int i=1;i<=c;i++)
		l=max(l,cntp[i]);
	while (l<=r)
	{
		int mid=l+r>>1;
		if (check(mid)!=-1)
			r=mid-1;
		else
			l=mid+1;
	}
	printf("%d %d\n",l,check(l));
}

int main()
{
	freopen("read.txt","r",stdin);
	freopen("write.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;i++)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
