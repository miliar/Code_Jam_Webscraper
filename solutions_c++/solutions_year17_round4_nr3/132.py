#include <bits/stdc++.h>

#define debug(x) cout << #x << " = " << x << endl
#define fori(i, ini, lim) for(int i = int(ini); i < int(lim); i++)
#define ford(i, ini, lim) for(int i = int(ini); i >= int(lim); i--)

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef tuple<int, int, int> state;

enum {LEFT, RIGHT, UP, DOWN};
const int MAX = 1e2 + 5;
const vector<ii> dir {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
int n, m;
char grid[MAX][MAX];
vector<ii> beams;
bool may[MAX][2], visited[MAX][MAX][4], is_beam[MAX][MAX];
bitset<55 * 55> p[MAX][2];

inline bool inside(int x, int y) {
	return x >= 1 && x <= n && y >= 1 && y <= m;
}

int get_dir(char c, int d) {
	if(c == '/') {
		if(d == UP) {
			return RIGHT;
		}
		else if(d == LEFT) {
			return DOWN;
		}
		else if(d == RIGHT) {
			return UP;
		}
		else if(d == DOWN) {
			return LEFT;
		}
	}
	else { //  
		if(d == UP) {
			return LEFT;
		}
		else if(d == RIGHT) {
			return DOWN;
		}
		else if(d == LEFT) {
			return UP;
		}
		else if(d == DOWN) {
			return RIGHT;
		}
	}
	return -1;
}

inline int mask(int x, int y) {
	x--, y--;
	return (x * m + y);
}

// type 0 -> -
// type 1 -> |
bool bfs(ii source, int type, bitset<55 * 55> &points) {
	queue<state> q;
	memset(visited, false, sizeof visited);
	if(type == 0) {
		q.emplace(source.first, source.second, LEFT);
		q.emplace(source.first, source.second, RIGHT);
		visited[source.first][source.second][LEFT] = true;
		visited[source.first][source.second][RIGHT] = true;
	}
	else {
		q.emplace(source.first, source.second, UP);
		q.emplace(source.first, source.second, DOWN);
		visited[source.first][source.second][UP] = true;
		visited[source.first][source.second][DOWN] = true;
	}
	while(!q.empty()) {
		auto cur = q.front(); q.pop();
		int x, y, d;
		tie(x, y, d) = cur;
		if(grid[x][y] == '.') {
			points.set(mask(x, y));
		}
		int nx = x + dir[d].first, ny = y + dir[d].second;
		if(!inside(nx, ny) || grid[nx][ny] == '#') {
			continue;
		}
		if(grid[nx][ny] == '|' || grid[nx][ny] == '-') {
			return false;
		}
		else if(grid[nx][ny] == '.' && !visited[nx][ny][d]) {
			visited[nx][ny][d] = true;
			q.emplace(nx, ny, d);
		}
		else {
			int nd = get_dir(grid[nx][ny], d);
			if(!visited[nx][ny][nd]) {
				visited[nx][ny][d] = true;
				q.emplace(nx, ny, nd);
			}
		}
	}

	return true;
}

int main() {
	int t;
	scanf("%d%*c", &t);
	int kase = 1;
	while(t--) {
		memset(may, false, sizeof may);
		beams.clear();
		bitset<55 * 55> points;
		scanf("%d %d%*c", &n, &m);
		fori(i, 1, n + 1) {
			fori(j, 1, m + 1) {
				scanf("%c", &grid[i][j]);
				if(grid[i][j] == '-' || grid[i][j] == '|') {
					beams.emplace_back(i, j);
				}
				else if(grid[i][j] == '.') {
					points.set(mask(i, j));
				}
			}
			scanf("%*c");
		}
		// type 0 -> -
		// type 1 -> |
		bitset<55 * 55> has;
		bool bad = false;
		vector<int> guys;
		fori(i, 0, beams.size()) {
			int can = 0;
			int last = -1;
			fori(j, 0, 2) {
				p[i][j].reset();
				//cout << "beam (" << beams[i].first << ", " << beams[i].second << ") type " << j << " -> ";
				if(bfs(beams[i], j, p[i][j])) {
					may[i][j] = true;
					can++;
					last = j;
				}
				//cout << may[i][j] << endl;
			}
			if(can == 0) {
				bad = true;
				break;
			}
			else if(can == 1) {
				grid[beams[i].first][beams[i].second] = (last == 0) ? '-' : '|';
				has |= p[i][last];		
			}
			else if(can == 2) {
				if(!p[i][0].any() && !p[i][1].any()) {

				}
				else if(!p[i][0].any()) {
					grid[beams[i].first][beams[i].second] = '|';
					has |= p[i][1];
				}
				else if(!p[i][1].any()) {
					grid[beams[i].first][beams[i].second] = '-';
					has |= p[i][0];
				}
				else {
					guys.push_back(i);
				}
			}
		}
		printf("Case #%d: ", kase++);
		if(bad) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		bad = true;
		int sz = guys.size();
		fori(i, 0, 1 << sz) {
			bitset<55 * 55> cur;
			fori(j, 0, sz) {
				if(i & (1 << j)) {
					cur |= p[guys[j]][1];
				}
				else {
					cur |= p[guys[j]][0];
				}
			}
			if((has | cur) == points) {
				bad = false;
				fori(j, 0, sz) {
					if(i & (1 << j)) {
						grid[beams[guys[j]].first][beams[guys[j]].second] = '|';
					}
					else {
						grid[beams[guys[j]].first][beams[guys[j]].second] = '-';
					}
				}
				break;
			}
		}
		if(!bad) {
			printf("POSSIBLE\n");
			fori(i, 1, n + 1) {
				fori(j, 1, m + 1) {
					printf("%c", grid[i][j]);
				}
				puts("");
			}
		}
		else {
			printf("IMPOSSIBLE\n");
		}
	}

	return 0;
}

