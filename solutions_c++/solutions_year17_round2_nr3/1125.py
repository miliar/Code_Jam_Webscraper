#include <stdio.h>
#include <algorithm>
#include <vector>
#include <map>
#define MAX_N 105
#define F_INF 1e20
using namespace std;
typedef pair<int, int> Edge;
typedef long long ll;
vector< vector< Edge > > graph;
int E[MAX_N], S[MAX_N];
map< ll, double > dp;

inline ll mHash(int s, int e, int hs, int he){
	ll res = 0;
	res |= ((ll) s) << 49;
	res |= ((ll) e) << 42;
	res |= ((ll) hs) << 32;
	res |= ((ll) he);
	return res;
}

double minTime(int s, int e, int hs, int he){
	//printf("%d %d %d %d\n", s, e, hs, he);
	if(he < 0) return F_INF;
	if(s == e) return 0.;
	ll hres = mHash(s, e, hs, he);
	if(dp.find(hres) != dp.end()) return dp[hres];
	double ans = F_INF;
	for(int i = 0; i < graph[s].size(); i++){
		int v = graph[s][i].first;
		int d = graph[s][i].second;
		if(hs >= S[s] && he >= E[s]){
			ans = min(ans, minTime(v, e, hs, he - d) + (double)d/hs);
 		}else if(S[s] >= hs && E[s] >= he){
			ans = min(ans, minTime(v, e, S[s], E[s] - d) + (double)d/S[s]);
		}else{
			ans = min(ans, minTime(v, e, S[s], E[s] - d) + (double)d/S[s]);
			ans = min(ans, minTime(v, e, hs, he - d) + (double)d/hs);
		}
	}
	dp[hres] = ans;
	//printf("%d %d %d %d %f\n", s, e, hs, he, ans);
	return ans;
}


int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T; scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		int N, Q; scanf("%d %d", &N, &Q);
		for(int i = 1; i <= N; i++){
			scanf("%d %d", &E[i], &S[i]);
		}
		graph.clear();
		graph.resize(N + 1);
		for(int i = 1; i <= N; i++){
			for(int j = 1; j <= N; j++){
				int D; scanf("%d", &D);
				if(D != -1){
					graph[i].push_back(make_pair(j, D));
				}
			}
		}
		printf("Case #%d: ", t);
		for(int q = 0; q < Q; q++){
			dp.clear();
			int s, e; scanf("%d %d", &s, &e);
			printf("%.9f ", minTime(s, e, 1, 0));
		}
		printf("\n");
	}
	return 0;
}