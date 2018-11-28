#include <bits/stdc++.h>

using namespace std;

const int maxn = 2004 * 5;

int n,m,c,cnt=1,S,T,nodeCnt = 1,ans;
int a[maxn],q[maxn],last[maxn],dis[maxn],p[maxn],b[maxn];
bool inq[maxn],mark[maxn];
struct edge
{
	int to,next,v,c;
}e[maxn * 5];
void insert(int u,int v,int w,int c)
{
	e[++cnt].to=v;e[cnt].next=last[u];last[u]=cnt;e[cnt].v=w;e[cnt].c=c;
	e[++cnt].to=u;e[cnt].next=last[v];last[v]=cnt;e[cnt].v=0;e[cnt].c=-c;
}
bool spfa()
{
	int head=0,tail=1;
	for (int i = S; i <= T; ++i)
		dis[i] = INT_MAX;
	q[0] = T; dis[T] = 0;
	while(head!=tail)
	{
		int now=q[head];head++;inq[now]=0;
		if(head==maxn)
			head=0;
		for(int i=last[now];i;i=e[i].next)
			if(dis[now]+e[i^1].c<dis[e[i].to]&&e[i^1].v)
			{
				dis[e[i].to]=dis[now]+e[i^1].c;
				if(!inq[e[i].to])
				{
					inq[e[i].to]=1;
					q[tail++]=e[i].to;
					if(tail==maxn)
						tail=0;
				}
			}
	}
	return dis[S]!=INT_MAX;
}
int dfs(int x,int f)
{
	mark[x]=1;
	if(x==T)
		return f;
	int w,used=0;
	for(int i=last[x];i;i=e[i].next)
		if(!mark[e[i].to]&&e[i].v&&dis[x]-e[i].c==dis[e[i].to])
		{
			w=dfs(e[i].to,min(e[i].v,f-used));
			e[i].v-=w;e[i^1].v+=w;
			ans+=w*e[i].c;
			used+=w;
			if(used==f)
				return f;
		}
	return used;
}
int zkw()
{
	int flow=0;
	while(spfa())
	{
		memset(mark,0,sizeof(mark));
		mark[T]=1;
		while(mark[T])
		{
			mark[T]=0;
			flow+=dfs(S,INT_MAX);
		}
	}
	return flow;
}
int build(int guess)
{
	ans = 0;
	cnt = 1;
	S = 0;T = 2 * n + m + 1;
	for (int i = S; i <= T; ++i)
		last[i] = 0;
	for (int i = 1; i <= n; ++i)
	{
		insert(i, T, guess, 0);
		insert(n + i, i, maxn, 0);
		if (i > 1)
			insert(n + i, n + i - 1, maxn, 0);
	}
	for (int i = 1; i <= m; ++i)
	{
		insert(S, 2 * n + i, 1, 0);
		insert(2 * n + i, n + p[i], 1, 1);
		insert(2 * n + i, p[i], 1, 0);
	}
}
bool check(int guess)
{
	build(guess);
	return zkw() == m;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		cin >> n >> c >> m;
		int num[maxn];
		memset(num, 0, sizeof(num));
		for (int i = 1; i <= m; ++i)
		{
			cin >> p[i] >> b[i];
			++num[b[i]];
		}
		int L = 0, R = m, MID;
		for (int i = 1; i <= c; ++i)
			L = max(L, num[i]);
		while (L < R)
		{
			MID = (L + R) / 2;
			if (check(MID))
				R = MID;
			else
				L = MID + 1;
		}
		check(L);
		printf("%d %d\n", L, ans);
	}
	return 0;
}
 
