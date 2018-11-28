#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
using namespace std;
inline int max(int a, int b){
	return a > b ? a : b;
}
const int N = 4010;
const int inf = 100000000;
const int M = N * 100;
int n, m, c;
int S, T;
int P[N], B[N], tot[N];
	int pre[N];
	int start[N], Next[M], to[M], flow[M], cost[M];
	int cnt = 1;
	inline void connect(int x, int y, int f, int c){
		to[++cnt] = y; Next[cnt] = start[x]; start[x] = cnt;
		flow[cnt] = f; cost[cnt] = c;
	}

	inline void Add(int x, int y, int f, int c){
		connect(x, y, f, c);
		connect(y, x, 0, -c);
	}

pair<int,int> solve(int);
int Init(){
	scanf("%d%d%d", &n, &c, &m);
	S = 0; T = 1 + n * 2 + c;
	for (int i = 1;i <= c;i++){
		tot[i] = 0;
	}
	for (int i = 1;i <= m;i++){
		scanf("%d%d", P+i, B+i);
		tot[B[i]]++;
	}
}

void Work(){
	int l = 0, r = m;
	for (int i = 1;i <= n;i++){
		l = max(l, tot[i]);
	}
	pair<int,int> ans;
	while (l <= r){
		int mid = l + r >> 1;
		pair<int, int> ret = solve(mid);
		//fprintf(stderr, "solve(%d) = [%d,%d]\n", mid, ret.first, ret.second);
		if (ret.first == m){
			ans.first = mid;
			ans.second = ret.second;
			r = mid - 1;
		}else{
			l = mid + 1;
		}
	}
	printf("%d %d\n", ans.first, ans.second);
}

int suc(int &x){
	x = x % (N*2) + 1;
	return x;
}

int bfs(int s){
	pre[s] = 0;
	// 每个点只会进入两次队列(1 -> 0)
	static int q[N * 3], head, tail, u;
	static int in[N * 3], d[N * 3];
	for (int i = S; i <= T;i++){
		in[i] = 0;
		d[i] = 2;
	}
	head = 0, tail = 1;
	q[1] = s; in[s] = 1; d[s] = 0;
	while (head != tail){
		u = q[suc(head)];
		for (int p = start[u];p;p = Next[p]){
			if (flow[p] && d[to[p]] > d[u] + cost[p]){
				d[to[p]] = d[u] + cost[p];
				pre[to[p]] = p;
				if (!in[to[p]]){
					//fprintf(stderr, "bfs: (%d)%d - %d\n", u, to[p], d[to[p]]);
					q[suc(tail)] = to[p];
					in[to[p]] = 1;
				}
			}
		}
		in[u] = 0;
	}
	if (d[T] < 2) return 1;
	else return 0;
}

pair<int,int> solve(int val){
	for (int i = 1;i <= cnt;i++) Next[i] = 0;
	for (int i = S;i <= T;i++) start[i] = 0;
	cnt = 1;
	for (int i = 1;i <= c;i++){
		Add(S, i, tot[i], 0);
	}
	for (int i = 1;i <= n;i++){
		Add(c+i, c+n+i, inf, 1);
		Add(c+n+i, c+i, inf, 0);
	}
	for (int i = 2;i <= n;i++){
		Add(c+n+i, c+n+i-1, inf, 0);
	}
	for (int i = 1;i <= n;i++){
		Add(c+i, T, val, 0);
	}
	for (int i = 1;i <= m;i++){
		Add(B[i], c + P[i], 1, 0);
	}
	pair<int,int> ret = make_pair(0,0);
	int cur;
	while (cur = bfs(S)){
		//fprintf(stderr, "bfs() = [%d]\n", cur);
		ret.first += cur;
		for (int i = pre[T];i;i = pre[to[i^1]]){
			//fprintf(stderr, "pre[%d] = %d", to[i], i);
			flow[i] -= cur;
			flow[i^1] += cur;
			ret.second += cost[i];
		}
	}
	return ret;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output2.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int tt = 1; tt <= T;tt++){
		printf("Case #%d: ", tt);
		//fprintf(stderr, "Case #%d:\n", tt);
		Init();
		Work();
	}
}

