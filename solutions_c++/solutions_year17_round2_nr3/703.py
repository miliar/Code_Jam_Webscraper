#include <cstdio>
#include <queue>
#include <cstring>
#define LL long long
using namespace std;

const int Maxn=100;

int n,Q;

LL abi[Maxn+5],spe[Maxn+5];
LL dis[Maxn+5][Maxn+5];

double dist[Maxn+5];
bool vis[Maxn+5];
bool inQue[Maxn+5];
queue<int> que;

double ans[Maxn+5];

void spfa(int src){
	while(!que.empty()) que.pop();
	memset(inQue,false,sizeof(inQue));
	memset(vis,false,sizeof(vis));

	vis[src]=true;
	dist[src]=0;
	inQue[src]=true;
	que.push(src);

	while(!que.empty()){
		int now=que.front();que.pop();
		inQue[now]=false;

		for (int x=1;x<=n;x++){
			if (now==x) continue;
			if (dis[now][x]==-1 || dis[now][x]>abi[now]) continue;
			
			double cst=(double)dis[now][x]/(double)spe[now];
			if (!vis[x] || dist[x]>dist[now]+cst){
				vis[x]=true;
				dist[x]=dist[now]+cst;
				if (!inQue[x]){
					que.push(x);
					inQue[x]=true;
				}
			}
		}
	}
}

inline void solve(int T){

	//Input
	scanf("%d%d",&n,&Q);
	for (int i=1;i<=n;i++) scanf("%lld%lld",&abi[i],&spe[i]);
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			scanf("%lld",&dis[i][j]);

	//Floyd
	for (int k=1;k<=n;k++)
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++){
				if (i==j) continue;
				if (dis[i][k]==-1 || dis[k][j]==-1) continue;
				if (dis[i][j]==-1 || dis[i][j]>dis[i][k]+dis[k][j]) dis[i][j]=dis[i][k]+dis[k][j];
			}

	/*for (int i=1;i<=n;i++){
		for (int j=1;j<=n;j++) printf("%d ",dis[i][j]);
		printf("\n");
	}*/

	//Solve
	for (int i=1;i<=Q;i++){
		int u,v;scanf("%d%d",&u,&v);
		spfa(u);
		ans[i]=dist[v];
	}

	//Print
	printf("Case #%d: ",T);
	for (int i=1;i<Q;i++) printf("%.8f ",ans[i]);
	printf("%.8f\n",ans[Q]); 
}

int main(){
	freopen("C-large.in.txt","r",stdin);
	freopen("C.out","w",stdout);
	int T=0;scanf("%d",&T);
	for (int i=1;i<=T;i++) solve(i);
	return 0;
}