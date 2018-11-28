#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<queue>
#define N 111
using namespace std;
double dis[N];
int test,vis[N],n,ques,map[N][N],S,T;
struct node
{
	int dis,speed;
}p[N];
void bfs(int S,int T)
{
	queue<int>q;
	for (int i=1;i<=n;i++)
	for (int j=1;j<=n;j++)
	dis[i]=1e15;
	dis[S]=0;
	memset(vis,0,sizeof(vis));
	vis[S]=1;
	q.push(S);
	while (!q.empty())
	{
		int temp=q.front();
		q.pop();
		for (int i=1;i<=n;i++)
		if (map[temp][i]!=0x3f3f3f3f&&map[temp][i]<=p[temp].dis&&dis[i]>dis[temp]+1.0*map[temp][i]/p[temp].speed)
		{	
			dis[i]=dis[temp]+1.0*map[temp][i]/p[temp].speed;
			if (!vis[i]) vis[i]=1,q.push(i);
		}
	}
	printf("%.8lf ",dis[T]);
}
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("3.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		printf("Case #%d: ",kk);
		cin>>n>>ques;
		for (int i=1;i<=n;i++)
		scanf("%d%d",&p[i].dis,&p[i].speed);
		for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
		{
			scanf("%d",&map[i][j]);
			if (map[i][j]==-1) map[i][j]=0x3f3f3f3f;
		}
		for (int k=1;k<=n;k++)
		for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
		if (map[i][j]>map[i][k]+map[k][j]) map[i][j]=map[i][k]+map[k][j];
	//	for (int i=1;i<=n;i++)
	//	for (int j=1;j<=n;j++)
	//	cout<<i<<' '<<j<<' '<<map[i][j]<<endl;
		while (ques--)
		{
			scanf("%d%d",&S,&T);
			bfs(S,T);
		}
		cout<<endl;
	}
	return 0;
}
