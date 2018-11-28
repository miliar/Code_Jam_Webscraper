#include <bits/stdc++.h>
using namespace std;
const int MAXN = 2005;
const char ch[] = {'\0', 'R', 'O', 'Y', 'G', 'B', 'V'};

int n, cnt[9], kase, g[9], nxt[MAXN], to[MAXN], edgeSize, cur; char ans[MAXN];

inline void addEdge(int u, int v){
	nxt[++ edgeSize] = g[u];
	to[g[u] = edgeSize] = v;
}
inline void addEdge(int u, int v, int w){
	while(w --) addEdge(u, v);
}
void Euler(int x){
	ans[cur --] = ch[x];
	if(!g[x]) return;
	int v = to[g[x]];
	g[x] = nxt[g[x]];
	Euler(v);
}
void solve(){
	int i, j; cur = n;
	printf("Case #%d: ", ++ kase);
	for(i = 0; i <= cnt[1] - cnt[4]; ++ i){
		memset(g, 0, sizeof(g));
		edgeSize = 0;
		addEdge(1, 4, cnt[4]);
		addEdge(4, 1, cnt[4]);
		addEdge(3, 1, i);
		addEdge(5, 1, cnt[1] - cnt[4] - i);
		addEdge(3, 6, cnt[6]);
		addEdge(6, 3, cnt[6]);
		if(i + cnt[6] > cnt[3]) continue;
		addEdge(3, 5, cnt[3] - cnt[6] - i);
		addEdge(5, 2, cnt[2]);
		addEdge(2, 5, cnt[2]);
		if(cnt[5] - cnt[2] - cnt[3] + cnt[6] + i < 0) continue;
		addEdge(1, 5, cnt[5] - cnt[2] - cnt[3] + cnt[6] + i);
		if(cnt[5] - cnt[2] - cnt[1] + i + cnt[4] < 0) continue;
		addEdge(5, 3, cnt[5] - cnt[2] - cnt[1] + i + cnt[4]);
		if(cnt[1] - cnt[4] - cnt[5] + cnt[2] + cnt[3] - cnt[6] - i < 0) continue;
		addEdge(1, 3, cnt[1] - cnt[4] - cnt[5] + cnt[2] + cnt[3] - cnt[6] - i);
		for(j = 1; !cnt[j]; ++ j) ;
		Euler(j);
		ans[n + 1] = 0;
		printf("%s\n", ans + 1);
		return;
	} printf("IMPOSSIBLE\n");
}
int main(){
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int i, testcase;
	scanf("%d", &testcase);
	while(testcase --){
		scanf("%d", &n);
		for(i = 1; i <= 6; ++ i)
			scanf("%d", &cnt[i]);
		solve();
	}
	return 0;
}
