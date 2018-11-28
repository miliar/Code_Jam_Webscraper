#include <bits/stdc++.h>
using namespace std;

#define MAXN 1004
#define MAXV 4003
#define MAXE 7007
#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()

int T, N, C, M;
struct Z{
	int p, b;
} A[MAXN];

int V, E;
int to[MAXE*2], flow[MAXE*2], cost[MAXE*2];
vector <int> cone[MAXV];

void add_edge(int a, int b, int f, int c)
{
	to[E] = b; flow[E] = f; cost[E] = c; cone[a].pb(E++);
	to[E] = a; flow[E] = 0; cost[E] = -c; cone[b].pb(E++);
}

int D[MAXV], frome[MAXV];
bool in_que[MAXV];

bool spfa()
{
	for (int i=1;i<=V;i++) D[i] = 1e9;
	queue <int> que; que.push(0); in_que[0] = 1;
	while (!que.empty()){
		int q = que.front(); que.pop();
		in_que[q] = 0;
		for (int e: cone[q]) if (flow[e]){
			int t = to[e], v = D[q] + cost[e];
			if (D[t] > v){
				D[t] = v; frome[t] = e;
				if (!in_que[t]) in_que[t] = 1, que.push(t);
			}
		}
	}
	return D[V] < 1e9;
}

int solve(int round)
{
	V = C + M + N + N + 1; E = 0;
	for (int i=0;i<=V;i++) cone[i].clear();
	for (int i=1;i<=C;i++) add_edge(0, i, round, 0);
	for (int i=1;i<=M;i++){
		add_edge(A[i].b, C+i, 1, 0);
		if (A[i].p > 1) add_edge(C+i, C+M+A[i].p-1, 1, 1);
		add_edge(C+i, C+M+N+A[i].p, 1, 0);
	}
	for (int i=1;i<=N;i++){
		if (i > 1) add_edge(C+M+i, C+M+i-1, 1e9, 0);
		add_edge(C+M+i, C+M+N+i, 1e9, 0);
		add_edge(C+M+N+i, V, round, 0);
	}
	int ret = 0, total = 0;
	while (spfa()){
		vector <int> pathe;
		for (int i=V;i;i=to[frome[i]^1]) pathe.pb(frome[i]);
		reverse(all(pathe));
		int f = 1e9;
		for (int e: pathe) f = min(f, flow[e]);
		total += f;
		for (int e: pathe) flow[e] -= f, flow[e^1] += f, ret += cost[e]*f;
	}
	if (total == M) return ret;
	return -1;
}

int main()
{
	for (scanf("%d", &T);T--;){
		scanf("%d%d%d", &N, &C, &M);
		for (int i=1;i<=M;i++) scanf("%d%d", &A[i].p, &A[i].b);

		int s = 1, e = M, ans, ans2;
		while (s <= e){
			int m = s+e >> 1;
			int v = solve(m);
			if (v >= 0) e = m-1, ans = m, ans2 = v;
			else s = m+1;
		}

		static int ts = 0;
		printf("Case #%d: %d %d\n", ++ts, ans, ans2);
	}
}