#include<stdio.h>
#include<string.h>
#include<assert.h>
#include<algorithm>
using namespace std;
const long long int inf = 1000000000000000LL;
int n;
long long int d[111][111];
int maxdis[111],speed[111];

double dis[111];
bool used[111];
double dij(int x,int y){
	for(int i=1; i<=n; i++)
		dis[i] = -1;
	dis[x]=0;
	memset(used,0,sizeof(used));
	for(int run = 1; run <= n; run++){
		int p = -1;
		for(int i=1; i<=n; i++)
			if(!used[i] && dis[i] > -0.5 && (p==-1 || dis[i] < dis[p])){
				p=i;
			}
		if(p==-1)break;
		if(p == y)break;
		used[p] = true;
		for(int i=1; i<=n; i++)
			if(!used[i] && d[p][i] <= maxdis[p]){
				double tmp = dis[p] + d[p][i] / (double)speed[p];
				if(dis[i] < 0 || dis[i] > tmp)
					dis[i] = tmp;
			}
	}
	assert(dis[y] > 0);
	return dis[y];
}
int main(){
	int _,t;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		int nq;
		scanf("%d%d",&n,&nq);
		for(int i=1; i<=n; i++)
			scanf("%d%d",&maxdis[i],&speed[i]);
		for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++){
			int x;
			scanf("%d",&x);
			if(i == j)d[i][j] = 0;else
			if(x == -1)d[i][j] = inf;else
				d[i][j] = x;
		}
		for(int k=1; k<=n; k++)
		for(int i=1; i<=n; i++)
		for(int j=1; j<=n; j++)
			d[i][j] = min(d[i][j],d[i][k] + d[k][j]);

		printf("Case #%d:",t);
		for(; nq--;){
			int x,y;
			scanf("%d%d",&x,&y);
			printf(" %.12lf",dij(x,y));
		}
		puts("");
	}
	return 0;
}
