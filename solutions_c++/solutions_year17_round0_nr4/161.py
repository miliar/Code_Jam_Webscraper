#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()

int T, N, M, D, V;
bool row[101], col[101], d1[201], d2[201];
char A[101][101], B[101][101];
bool w[601][601];

int nd1(int r, int c){ return r+c-1; }
int nd2(int r, int c){ return r-c+N; }

bool bfs()
{
	vector <int> vis(V+1, 0), from(V+1, 0);
	queue <int> que;
	que.push(0); vis[0] = 1;
	while (!que.empty()){
		int q = que.front(); que.pop();
		for (int i=0;i<=V;i++) if (w[q][i] && !vis[i]){
			vis[i] = 1; que.push(i); from[i] = q;
		}
	}
	if (!vis[V]) return 0;
	vector <int> path;
	for (int i=V;i;i=from[i]) path.pb(i);
	path.pb(0);
	reverse(all(path));
	for (int i=1;i<sz(path);i++)
		w[path[i-1]][path[i]] = 0, w[path[i]][path[i-1]] = 1;
	return 1;
}

int main()
{
	for (scanf("%d", &T);T--;){
		static int ts = 0;
		printf("Case #%d: ", ++ts);

		scanf("%d%d", &N, &M); D = N+N-1; V = N+N+D+D+1;
		for (int i=1;i<=N;i++) row[i] = col[i] = 1;
		for (int i=1;i<=D;i++) d1[i] = d2[i] = 1;
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++) A[i][j] = '.';
		for (int i=0;i<=V;i++) for (int j=0;j<=V;j++) w[i][j] = 0;

		int ans = 0;
		for (int i=1;i<=M;i++){
			char c; int y, x;
			scanf(" %c%d%d", &c, &y, &x); A[y][x] = c;
			if (c != '+') row[y] = col[x] = 0, ans++;
			if (c != 'x') d1[nd1(y, x)] = d2[nd2(y, x)] = 0, ans++;
		}
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++) B[i][j] = A[i][j];

		for (int i=1;i<=N;i++) w[0][i] = row[i], w[N+i][V] = col[i];
		for (int i=1;i<=D;i++) w[0][N+N+i] = d1[i], w[N+N+D+i][V] = d2[i];
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++)
			w[i][N+j] = w[N+N+nd1(i, j)][N+N+D+nd2(i, j)] = 1;

		while (bfs()) ans++;
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++){
			if (w[N+j][i]) B[i][j] = B[i][j] == '+' ? 'o' : 'x';
			if (w[N+N+D+nd2(i, j)][N+N+nd1(i, j)]) B[i][j] = B[i][j] == 'x' ? 'o' : '+';
		}

		struct Z{
			char c; int y, x;
		};
		vector <Z> changed;
		for (int i=1;i<=N;i++) for (int j=1;j<=N;j++) if (A[i][j] != B[i][j]){
			changed.pb({B[i][j], i, j});
		}

		printf("%d %d\n", ans, sz(changed));
		for (Z &z: changed) printf("%c %d %d\n", z.c, z.y, z.x);
	}
}