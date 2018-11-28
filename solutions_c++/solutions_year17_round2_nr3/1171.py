#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
struct edge { int to; ld cost; };
typedef pair<ld, int> Pi;
int u, t=1;
int main(){
	for(cin>>u; t<=u; t++){
		int n, q, mx[101], speed[101], dis[101], i=1, j, tmp;
		ld tim[101];
		vector<edge> G[101];
		priority_queue<Pi, vector<Pi>, greater<Pi>> PQ;
		for(cin>>n>>q; i<=n; i++)
			cin>>mx[i]>>speed[i];
		for(i=1; i<=n; i++)
			for(j=1; j<=n; j++){
				cin>>tmp;
				if(j==i+1)
					dis[j]=tmp;
			}
		cin>>tmp>>tmp;
		for(i=2; i<=n; i++)	dis[i]=dis[i-1]+dis[i];
		for(i=1; i<=n; i++)
			for(j=i+1; j<=n&&(dis[j]-dis[i])<=mx[i]; j++)
				G[i].push_back({j, (ld)(dis[j]-dis[i])/speed[i]});
		fill(tim, tim+101, 1e13);
		tim[1]=0;
		PQ.push(Pi(0, 1));
		while(!PQ.empty()){
			int v=PQ.top().second;
			ld cost=PQ.top().first;
			PQ.pop();
			if(tim[v]<cost)	continue;
			for(auto e:G[v]){
				if(tim[e.to]>tim[v]+e.cost){
					tim[e.to]=tim[v]+e.cost;
					PQ.push(Pi(tim[e.to], e.to));
				}
			}
		}
		printf("Case #%d: %.6Lf\n", t, tim[n]);
	}
	return 0;
}
