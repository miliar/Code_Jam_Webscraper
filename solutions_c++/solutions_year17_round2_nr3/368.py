#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ld double
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define pii pair<int,int>
#define vll vector<ll >
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1)
#define all(a) (a).begin(), (a).end()
#define print(s) cerr<<#s<<" : ";for(auto i:(s))cerr<<i<<" ";cerr<<"\n";
#define sd(t) scanf("%d",&(t))
#define slld(t) scanf("%lld",&(t))
#define pd(t) printf("%d\n",(t))
#define endl "\n"
const int N = 105;
const ll inf = 1e18;
double dp[N][N][N], speed[N], dp2[N][N];
ll dist[N][N], d[N][N];
int e[N], s[N];
const ld INF = 1e18;
int main(){
	int t = 1, n, q;
	sd(t);
	for(int tt = 1; tt <= t; tt++){
		sd(n); sd(q);
		for(int i = 1; i <= n; i++){
			sd(e[i]), sd(s[i]);
			speed[i] = s[i];
		}
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= n; j++){
				slld(d[i][j]);
				if(d[i][j] == -1) d[i][j] = inf;
				dist[i][j] = d[i][j];
			}
			dist[i][i] = 0;
		}
		for(int k = 1; k <= n; k++){
			for(int i = 1; i <= n; i++){
				for(int j = 1; j <= n; j++)
					if(dist[i][j] > dist[i][k] + dist[k][j])
						dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
		cout <<"Case #" << tt << ": ";
		while(q--){
			int a, b;
			sd(a), sd(b);
			for(int i = 1; i <= n; i++){
				for(int j = 1; j <= n; j++){
					for(int k = 1; k <= n; k++)
						dp[i][j][k] = INF;
					dp2[i][j] = inf;	
				}
			}
			for(int i = 1; i <= n; i++){
				dp2[0][i] = inf;
				for(int j = 1; j <= n; j++) dp[0][i][j] = inf;
			}
			for(int i = 1; i <= n; i++) if(dist[a][i] <= e[a]){
				dp[0][a][i] = dist[a][i] / speed[a];
				dp2[0][i] = dp[0][a][i];
			}
			for(int i = 1; i <= n; i++){
				for(int j = 1; j <= n; j++){
					for(int k = 1; k <= n; k++){
						if(dist[k][j] <= e[k]) dp[i][k][j] = dp2[i - 1][k] + dist[k][j] / speed[k];
						dp2[i][j] = min(dp2[i][j], dp[i][k][j]);
					}
				}
			}
			double ans = inf;
			for(int i = 0; i <= n; i++) ans = min(ans, dp2[i][b]);
			printf("%.10lf ", ans);	
		}
		printf("\n");
	}
}