#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <string>

using namespace std;

# define pb push_back
# define mp make_pair

typedef long long ll;
typedef pair<int,int> PII;

const int maxn =  (100)+10;

int e[maxn],s[maxn],d[maxn][maxn],n;
double ans;

void dfs(int horse, int remain, int node, double t) {
	if(node == n) {
		ans = min(ans,t);
		return;
	}
	if(remain >= d[node][node+1]) {
		dfs(horse, remain - d[node][node+1], node+1, t + 1.0*d[node][node+1]/s[horse]);
	}
	if(e[node] >= d[node][node+1]) {
		dfs(node, e[node]-d[node][node+1], node+1, t + 1.0*d[node][node+1]/s[node]);
	}
}

int main()
{
	// freopen("input.txt","r",stdin);
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt","w", stdout);
	int ncase, T;
	int q,u,v;
	ncase = 0;
	cin >> T;
	while(T --) {
		ncase++;
		cin >> n >> q;
		for(int i = 1; i <= n; i++) {
			cin >> e[i] >> s[i];
		}
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= n; j++) {
				cin >> d[i][j];
			}
		}
		cin >> u >> v;
		ans = 1e20;
		dfs(1,e[1],1,0.0);
		printf("Case #%d: %.7lf\n",ncase,ans);
	}
	return 0;
}