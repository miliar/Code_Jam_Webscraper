#include <bits/stdc++.h>
using namespace std;

const int MAXN=55;

struct interval
{
	int l,r;
}lim[MAXN][MAXN];

int r[MAXN],q[MAXN][MAXN],lim_min[MAXN][MAXN],lim_max[MAXN][MAXN],head[MAXN];

bool cmp(const interval &a,const interval &b)
{
	return a.l<b.l;
}

void solve()
{
	int n,p;
	scanf("%d%d",&n,&p);
	for (int i=0;i<n;i++)
		scanf("%d",&r[i]);
	for (int i=0;i<n;i++)
		for (int j=0;j<p;j++)
			scanf("%d",&q[i][j]);
	for (int i=0;i<n;i++)
		for (int j=0;j<p;j++)
		{
			lim[i][j].l=(q[i][j]*10-1)/(11*r[i])+1;
			lim[i][j].r=q[i][j]*10/(9*r[i]);
			//printf("%d %d\n",lim[i][j].l,lim[i][j].r);
		}
	for (int i=0;i<n;i++)
		head[i]=0;
	for (int i=0;i<n;i++)
		sort(lim[i],lim[i]+p,cmp);
	int ans=0;
	priority_queue <int,vector<int>,greater<int> > pq[MAXN];
	for (int k=1;k<=1000000;k++)
	{
		for (int i=0;i<n;i++)
			while (!pq[i].empty()&&pq[i].top()<k)
				pq[i].pop();
		for (int i=0;i<n;i++)
			while (head[i]<p&&lim[i][head[i]].l==k)
			{
				if (lim[i][head[i]].l<=lim[i][head[i]].r) pq[i].push(lim[i][head[i]].r);
				head[i]++;
			}
		for (bool flag=true;flag;)
		{
			for (int j=0;j<n;j++)
				if (pq[j].empty())
				{
					flag=false;
					break;
				}
			if (flag)
			{
				ans++;
				for (int j=0;j<n;j++)
					pq[j].pop();
			}
		}
	}
	printf("%d\n",ans);
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
