#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define mp make_pair
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define pb push_back
#define ii pair<int,int>
#define INF 100000000000000.0
#define M 1000000007ll
#define EPS 1e-11
#define INFLL 1000000000000000010ll
#define UQ(x) (x).resize(distance((x).begin(),unique(all((x)))))
#define mid(x,y) (((x)+(y))>>1)
int tc;
int n,q;
ll e[105];
double s[105];
ll d[105][105];
double t[105][105];
#define pdi pair<double,int>
priority_queue<pdi,vector<pdi>,greater<pdi> > pq;
void dijkstra(int sc) {
	for (int i=0;i<n;i++) {
		t[sc][i]=INF;
	}
	t[sc][sc]=0;
	while(!pq.empty()) pq.pop();
	pq.push(mp(0.0,sc));
	while(!pq.empty()) {
		pdi x=pq.top();
		pq.pop();
		int v=x.second;
		if (x.first>t[sc][v]+EPS) continue;
		for (int i=0;i<n;i++) {
			if (i==v) continue;
			if (d[v][i]==-1ll) continue;
			if (e[v]>=d[v][i]) {
				double tt=(double)d[v][i]/s[v];
				if (t[sc][v]+tt<t[sc][i]) {
					t[sc][i]=t[sc][v]+tt;
					pq.push(mp(t[sc][i],i));
				}
			}
		}
	}
}

int main() {
	scanf("%d",&tc);
	for (int kk=1;kk<=tc;kk++) {
		scanf("%d%d",&n,&q);
		for (int i=0;i<n;i++) {
			scanf("%lld%lf",&e[i],&s[i]);
		}
		for (int i=0;i<n;i++) {
			for (int j=0;j<n;j++) {
				scanf("%lld",&d[i][j]);
			}
		}
		for (int k=0;k<n;k++) {
			for (int i=0;i<n;i++) {
				for (int j=0;j<n;j++) {
					if (d[i][k]==-1ll || d[k][j]==-1ll) continue;
					if (d[i][j]==-1ll) d[i][j]=d[i][k]+d[k][j];
					else d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
				}
			}
		}
		for (int i=0;i<n;i++) dijkstra(i);
		int u,v;
		printf("Case #%d:", kk);
		while(q--) {
			scanf("%d%d",&u,&v);
			--u,--v;
			assert(d[u][v]>0);
			assert(t[u][v]<INF-EPS);
			printf(" %.8lf",t[u][v]);
		}
		printf("\n");
	}
}