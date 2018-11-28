#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define F first
#define S second

const int MAXN = 50 + 3;

int n, m;
string s[MAXN];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
int vis[MAXN][MAXN][4], g;
bool fail;
vector<pii> vec[MAXN][MAXN][2];
vector<pair<pii, int>> par[MAXN][MAXN];
int cnt[MAXN][MAXN];
bool mark[MAXN][MAXN];

bool fit(int x, int y){return 0 <= x && x < n && 0 <= y && y < m && s[x][y] != '#';}

void go(int x, int y, int dir, int xx, int yy, int tt){
	if (!fit(x, y)) return;
	
	if (s[x][y] == '/'){
		if (dir == 0) dir = 3;
		else if (dir == 3) dir = 0;
		else if (dir == 1) dir = 2;
		else dir = 1;
	}
	else if (s[x][y] == '\\')
		dir ^= 1;

	if (vis[x][y][dir] == g || s[x][y] == '|' || s[x][y] == '-'){
		fail = 1;
		return;
	}
	vis[x][y][dir] = g;

	go(x+dx[dir], y+dy[dir], dir, xx, yy, tt);
	mark[x][y] = 1;
}

bool done[MAXN][MAXN], fx[MAXN][MAXN], ok[MAXN][MAXN][2];
int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	int te;	cin >> te;
	for (int w = 1; w <= te; w++){
		cin >> n >> m;
		for (int i = 0; i < n; i++) cin >> s[i];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++){
				for (int w = 0; w < 2; w++)
					vec[i][j][w].clear();
				par[i][j].clear();
			}

		memset(vis, 0, sizeof(vis));
		memset(ok, 0, sizeof(ok));
		memset(cnt, 0, sizeof(cnt));
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (s[i][j] == '|' || s[i][j] == '-'){
					g++;
					fail = 0;
					memset(mark, 0, sizeof(mark));
					go(i+dx[0], j+dy[0], 0, i, j, 0);
					g++;
					go(i+dx[2], j+dy[2], 2, i, j, 0);
					if (!fail){
						ok[i][j][0] = 1;
						for (int ii = 0; ii < n; ii++)
							for (int jj = 0; jj < m; jj++)
								if (mark[ii][jj]){
									cnt[ii][jj]++;
									par[ii][jj].push_back({{i, j}, 0});
									vec[i][j][0].push_back({ii, jj});
								}
					}

					fail = 0;
					g++;
					memset(mark, 0, sizeof(mark));
					go(i+dx[1], j+dy[1], 1, i, j, 1);
					g++;
					go(i+dx[3], j+dy[3], 3, i, j, 1);
					if (!fail){
						ok[i][j][1] = 1;
						for (int ii = 0; ii < n; ii++)
							for (int jj = 0; jj < m; jj++)
								if (mark[ii][jj]){
									cnt[ii][jj]++;
									par[ii][jj].push_back({{i, j}, 1});
									vec[i][j][1].push_back({ii, jj});
								}
					}
				}

		fail = 0;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				if (s[i][j] == '|' || s[i][j] == '-'){
					if (!ok[i][j][0] && !ok[i][j][1])
						fail = 1;
					if (ok[i][j][0])
						s[i][j] = '-';
					else
						s[i][j] = '|';
				}

		if (fail){
			cout << "Case #" << w << ": " << "IMPOSSIBLE\n";
			continue;
		}

		memset(done, 0, sizeof(done));
		memset(fx, 0, sizeof(fx));
		bool changed = 1;
		while (changed){
			changed = 0;
			for (int i = 0; i < n; i++)
				for (int j = 0; j < m; j++)
					if (s[i][j] == '.' && cnt[i][j] == 0 && !done[i][j]){
						fail = 1;
						goto there;
					}
			
			for (int i = 0; !changed && i < n; i++)
				for (int j = 0; !changed && j < m; j++)
					if (s[i][j] == '.' && cnt[i][j] == 1 && !done[i][j]){
						changed = 1;
						pair<pii, int> v;
						for (auto x:par[i][j])
							if (!fx[x.F.F][x.F.S]){
								v = x;
								break;
							}

						if (v.S == 0)
							s[v.F.F][v.F.S] = '-';
						else
							s[v.F.F][v.F.S] = '|';
						fx[v.F.F][v.F.S] = 1;

						for (auto x:vec[v.F.F][v.F.S][v.S])
							done[x.F][x.S] = 1;
						for (auto x:vec[v.F.F][v.F.S][!v.S])
							cnt[x.F][x.S]--;
					}
		}
there:
		if (fail){
			cout << "Case #" << w << ": " << "IMPOSSIBLE\n";
			continue;
		}

		cout << "Case #" << w << ": " << "POSSIBLE\n";
		for (int i = 0; i < n; i++)
			cout << s[i] << "\n";
	}
	return 0;
}
