#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
#define F first
#define S second
#define X real()
#define Y imag()

const ll INF=1e18;
ll dist[101][101];
ld tid[101][101];
ll e[101];
ld sp[101];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int tcs;
	cin>>tcs;
	cout<<setprecision(15);
	for (int tc=1;tc<=tcs;tc++) {
		int n,q;
		cin>>n>>q;
		for (int i=1;i<=n;i++) cin>>e[i]>>sp[i];
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				ll d;
				cin>>d;
				if (d==-1) dist[i][j]=INF;
				else dist[i][j]=d;
			}
		}
		for (int k=1;k<=n;k++) {
			for (int i=1;i<=n;i++) {
				for (int j=1;j<=n;j++) {
					dist[i][j]=
				min(dist[i][j],dist[i][k]+dist[k][j]);
				}
			}
		}
		for (int i=1;i<=n;i++) {
			for (int j=1;j<=n;j++) {
				if (dist[i][j]>e[i]) tid[i][j]=INF;
				else tid[i][j]=dist[i][j]/sp[i];
			}
		}
		for (int k=1;k<=n;k++) {
			for (int i=1;i<=n;i++) {
				for (int j=1;j<=n;j++) {
					tid[i][j]=
				min(tid[i][j],tid[i][k]+tid[k][j]);
				}
			}
		}
		cout<<"Case #" <<tc<<":";
		for (int i=0;i<q;i++) {
			int u,v;
			cin>>u>>v;
			cout<<" "<<tid[u][v];
		}
		cout<<"\n";
	}
}
