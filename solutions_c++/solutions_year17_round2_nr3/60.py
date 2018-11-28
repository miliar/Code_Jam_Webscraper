#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define M 1000000007
#define all(a) a.begin(), a.end()

int n, q;
int e[110], s[110];
ll d[110][110];
double dis[110];
bool vis[110];

int main(){
	freopen("C-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	int T, ca = 0;
	scanf("%d", &T);
	while(T--){
		printf("Case #%d: ", ++ca);
		scanf("%d%d", &n, &q);
		for(int i = 1; i <= n; ++i) scanf("%d%d", e + i, s + i);
		for(int i = 1; i <= n; ++i)
			for(int j = 1; j <= n; ++j)
				scanf("%lld", d[i] + j);
		for(int k = 1; k <= n; ++k)
			for(int i = 1; i <= n; ++i)
				for(int j = 1; j <= n; ++j)
					if(d[i][k] != -1 && d[k][j] != -1)
						if(d[i][j] == -1 || d[i][k] + d[k][j] < d[i][j])
							d[i][j] = d[i][k] + d[k][j];
		
		while(q--){
			int u, v;
			scanf("%d%d", &u, &v);
			for(int i = 1; i <= n; ++i) dis[i] = 1e18;
			memset(vis, 0, sizeof(vis));
			dis[u] = 0;
			vis[u] = 1;
			queue<int> q;
			q.push(u);
			while(!q.empty()){
				int t = q.front(); q.pop();
				for(int i = 1; i <= n; ++i)
					if(d[t][i] != -1 && d[t][i] <= e[t]){
						if(dis[t] + 1. * d[t][i] / s[t] < dis[i]){
							dis[i] = dis[t] + 1. * d[t][i] / s[t];
							if(!vis[i]) q.push(i), vis[i] = 1;
						}
					}
				vis[t] = 0;
			}
			printf("%.10f ", dis[v]);
		}
		puts("");
	}
	
	return 0;
}
