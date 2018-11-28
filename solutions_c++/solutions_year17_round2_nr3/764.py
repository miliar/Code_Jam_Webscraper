#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#include <bitset>
#include <string>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define ls id<<1,l,mid
#define rs id<<1|1,mid+1,r
#define OFF(x) memset(x,-1,sizeof x)
#define CLR(x) memset(x,0,sizeof x)
#define MEM(x) memset(x,0x3f,sizeof x)
typedef long long ll ;
typedef pair<ll,ll> pii ;
const int maxn = 150 ;
const int maxm = 1e6 + 50;
const double eps = 1e-10;
const int max_Index = 62;
const int inf = 0x3f3f3f3f ;
const int MOD = 1e9+7 ;

ll speed[maxn];
ll totaldist[maxn], dist[maxn][maxn];
ll dis[maxn];
int head[maxn], cnt = 0;
int nxt[maxm], pnt[maxm];
double cost[maxm], Dis[maxn];
bool inq[maxn];
int n, q; 

void add_edge(int u, int v, double c) {
	pnt[cnt] = v;
	nxt[cnt] = head[u];
	cost[cnt] = c;
	head[u] = cnt++;
}

void spfa(int st) {
	memset(dis, 0x3f, sizeof dis);
	memset(inq, 0x00, sizeof inq);
	dis[st] = 0;
	queue<int> q;
	q.push(st);
	while (q.size()) {
		int u = q.front(); q.pop();
		inq[u] = 0;
		for (int i = 1; i <= n; i++) {
			if (dist[u][i] == -1) continue;
			if (dis[u] + dist[u][i] >= dis[i]) continue;
			dis[i] = dis[u] + dist[u][i];
			if (dis[i] > totaldist[st]) continue;
			if (!inq[i]) q.push(i);
			inq[i] = 1;
		}
	}
	for (int i = 1; i <= n; i++)
		if (dis[i] <= totaldist[st]) add_edge(st, i, dis[i] * 1.0 / speed[st]);
}

void spfa1(int st) {
	double *dis = Dis;
	for (int i = 1; i <= n; i++) dis[i] = 1e18;
	memset(inq, 0, sizeof inq);
	dis[st] = 0;
	queue<int> q;
	q.push(st);
	while (q.size()) {
		int u = q.front(); q.pop();
		inq[u] = 0;
		for (int i = head[u]; ~i; i = nxt[i]) {
			int v = pnt[i];
			if (dis[u] + cost[i] >= dis[v]) continue;
			dis[v] = dis[u] + cost[i];
			if (!inq[v]) q.push(v);
			inq[v] = 1;
		}
	}
}

int main() {
#ifdef zzblack
	freopen("C:\\Users\\zzblack\\Desktop\\case.in","r",stdin);
    freopen("C:\\Users\\zzblack\\Desktop\\case.out","w",stdout);
#endif
    int T, cas = 1; cin >> T;
    while (T--) {
    	printf("Case #%d:", cas++);
    	cin >> n >> q; 
    	for (int i = 1; i <= n; i++) cin >> totaldist[i] >> speed[i];
    	for (int i = 1; i <= n; i++)
    		for (int j = 1; j <= n; j++)
    			cin >> dist[i][j];
    	memset(head, 0xff, sizeof head); cnt = 0;
    	for (int i = 1; i <= n; i++) {
    		spfa(i);
    	}
    	while (q--) {
    		int u, v; cin >> u >> v;
    		spfa1(u);
    		printf(" %.7f", Dis[v]);
    	}
    	puts("");
    }

    return 0;
}

    
