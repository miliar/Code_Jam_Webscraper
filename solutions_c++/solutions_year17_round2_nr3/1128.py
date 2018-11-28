#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define pb push_back
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x),ri(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)

typedef long long ll;
typedef vector<int> vi;

const int MAXN=110;
const double INF=1e15;

double dp[MAXN][MAXN];
pair<int,int> qs[MAXN];
int T,N,Q,dist[MAXN],speed[MAXN],D[MAXN][MAXN];

double solve(int c, int h, int left) {
	if(c == N-1) return 0;
	if(dp[c][h]!=-1) return dp[c][h];
	dp[c][h]=INF;
	if(dist[c] >= D[c][c+1])
		dp[c][h]=min(dp[c][h], solve(c+1,c,dist[c]-D[c][c+1]) + (double)D[c][c+1]/speed[c]);
	if(left >= D[c][c+1])
		dp[c][h]=min(dp[c][h], solve(c+1,h,left-D[c][c+1]) + (double)D[c][c+1]/speed[h]);
	return dp[c][h];
}

int main() {
	ri(T);
	FOR(t,1,T+1) {
		rii(N,Q);
		FOR(i,0,N) rii(dist[i],speed[i]);
		FOR(i,0,N) FOR(j,0,N) ri(D[i][j]);
		FOR(i,0,Q) rii(qs[i].first,qs[i].second);
		FOR(i,0,MAXN) FOR(j,0,MAXN) dp[i][j]=-1;
		printf("Case #%d: %.6lf\n",t,solve(0,0,dist[0]));
	}
}