#include <bits/stdc++.h>
using namespace std;

#define pb push_back
typedef pair<int, int> pii;

int yy[]={-1, 0, 1, 0}, xx[]={0, 1, 0, -1};
int T, N, M, B;
char A[51][52];
int bnum[51][51];
bool valid[51][51][2];
int poss[51][51][2];

int vis[2501];
vector <int> con[5001];
inline int num(int n){ return n < 0 ? B - n : n; }

vector <int> history;
bool dfs(int state){
	int n = abs(state);
	if (vis[n]) return vis[n] == state;
	history.pb(n); vis[n] = state;
	for (int t: con[num(state)]){
		if (!dfs(t)) return 0;
	}
	return 1;
}

int main()
{
	for (scanf("%d", &T);T--;){
		static int ts = 0;
		printf("Case #%d: ", ++ts);

		memset(bnum, 0, sizeof(bnum));
		memset(valid, 0, sizeof(valid));
		memset(poss, 0, sizeof(poss));
		scanf("%d%d", &N, &M); B = 0;
		for (int i=1;i<=N;i++) scanf("%s", A[i]+1);
		for (int i=1;i<=N;i++) for (int j=1;j<=M;j++)
			if (strchr("-|", A[i][j])) bnum[i][j] = ++B;

		bool impossible = 0;
		for (int i=1;i<=N;i++) for (int j=1;j<=M;j++) if (strchr("-|", A[i][j])){
			for (int d=0;d<2;d++){
				bool invalid = 0;
				for (int dir=d;dir<4;dir+=2){
					int y = i, x = j, nd = dir;
					for (;;){
						y += yy[dir]; x += xx[dir];
						if (A[y][x] == '#' || y < 1 || y > N || x < 1 || x > M) break;
						if (bnum[y][x]){ invalid = 1; break; }
						if (A[y][x] == '/') nd = 3-nd;
						else if (A[y][x] == '\\') nd = nd^1;
						else poss[y][x][nd&1] = d ? -bnum[i][j] : bnum[i][j];
					}
				}
				valid[i][j][d] = !invalid;
			}
			if (!valid[i][j][0] && !valid[i][j][1]) impossible = 1;
		}
		for (int i=1;i<=N;i++) for (int j=1;j<=M;j++) if (A[i][j] == '.'){
			if (!poss[i][j][0] && !poss[i][j][1]) impossible = 1;
		}

		if (impossible){ puts("IMPOSSIBLE"); continue; }

		// Make relation
		for (int i=1;i<=B;i++) vis[i] = 0;
		for (int i=1;i<=B+B;i++) con[i].clear();
		for (int i=1;i<=N;i++) for (int j=1;j<=M;j++) if (A[i][j] == '.'){
			if (poss[i][j][0] && poss[i][j][1]){
				con[num(-poss[i][j][0])].pb(poss[i][j][1]);
				con[num(-poss[i][j][1])].pb(poss[i][j][0]);
			}
		}

		// Now 2-SAT
		for (int i=1;i<=N;i++) for (int j=1;j<=M;j++) if (bnum[i][j]){
			if (!valid[i][j][1]){
				if (!dfs(bnum[i][j])){ impossible = 1; break; }
			}else if (!valid[i][j][0]){
				if (!dfs(-bnum[i][j])){ impossible = 1; break; }
			}
		}
		for (int i=1;i<=N;i++) for (int j=1;j<=M;j++) if (A[i][j] == '.'){
			if (!poss[i][j][1] && !dfs(poss[i][j][0])){ impossible = 1; break; }
			if (!poss[i][j][0] && !dfs(poss[i][j][1])){ impossible = 1; break; }
		}
		if (impossible){ puts("IMPOSSIBLE"); continue; }

		for (int i=1;i<=B;i++) if (!vis[i]){
			history.clear();
			if (dfs(i)) continue;
			for (int t: history) vis[t] = 0;
			if (!dfs(-i)){ impossible = 1; break; }
		}
		if (impossible){ puts("IMPOSSIBLE"); continue; }
		puts("POSSIBLE");
		for (int i=1;i<=N;i++,puts("")) for (int j=1;j<=M;j++){
			if (bnum[i][j]) putchar(vis[bnum[i][j]] > 0 ? '|' : '-');
			else putchar(A[i][j]);
		}
	}
}