#include <bits/stdc++.h>
using namespace std;

template <typename S, typename F>
void dfs_visit (int cur, vector<vector<int>> const& buren, S start, F finish,
	vector<bool> &mark) {
	if (mark[cur]) { return; }
	mark[cur] = true;

	start (cur);
	for (auto nb : buren[cur]) {
		dfs_visit (nb, buren, start, finish, mark);
	}
	finish (cur);
}
vector<int> finish_sort(vector<vector<int>> const& buren) {
	vector<int> finished; vector<bool> mark(buren.size());
	int n = buren.size();
	for (int i = 0; i < n; i++) { 
		dfs_visit (i, buren, [](int){},
			[&](int cur){finished.push_back(cur);}, mark);
	}
	return finished;
}
pair<int, vector<int>> 
 scc_and_top_sort(vector<vector<int>> const& heen, vector<vector<int>> const& terug) {
	vector<int> comp(heen.size());
	vector<bool> mark(heen.size(),false); int comp_n = 0;
	
	auto finished = finish_sort(heen);
	for (auto it = finished.rbegin(); it != finished.rend(); it++) {
		if (mark[*it]) { continue; }
		dfs_visit(*it, terug, [&](int cur){comp[cur] = comp_n;}, [](int){}, mark);
		comp_n++;
	}
	return make_pair(comp_n, comp);
}
// 2sat gives output for both nodes of a variable
vector<bool> two_sat(vector<vector<int>> const& heen, vector<vector<int>> const& terug) {
	int n = heen.size();
	vector<bool> val;
	int comp_n; vector<int> comp;
	vector<int> opp(n);
	
	tie(comp_n, comp) = scc_and_top_sort(heen, terug);
	for (int i=0; i<n; i++) { opp[comp[i]] = comp[i^1]; }
	for (int i=0; i<comp_n; i++) { if (opp[i] == i) { return val; } }
	vector<bool> cval(comp_n, false);
	for (int i=0; i<comp_n; i++) { if (!cval[i]) { cval[opp[i]] = true; } }
	for (int i=0; i<n; i++) { val.push_back(cval[comp[i]]); }
	return val;
}

void doCase(int t) {
	int R, C;
	cin >> R >> C;
	vector<vector<char>> grid(R, vector<char>(C));
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			cin >> grid[i][j];
		}
	}
	vector<vector<vector<int>>> lasers(R, vector<vector<int>>(C));
	vector<vector<int>> heen, terug;
	int curIdx = 0;
	
	// First iteration, find lasers
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			if (grid[i][j] != '|' && grid[i][j] != '-')
				continue;
			
			heen.push_back(vector<int>());
			heen.push_back(vector<int>());
			terug.push_back(vector<int>());
			terug.push_back(vector<int>());
			
			bool udAcceptable = true;
			int curX = i-1, curY = j;
			int dirX = -1, dirY = 0;
			while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
				if (grid[curX][curY] == '#')
					break;
				if (grid[curX][curY] == '|' || grid[curX][curY] == '-') {
					udAcceptable = false;
					break;
				}
				if (grid[curX][curY] == '/') {
					int t = dirX;
					dirX = -dirY;
					dirY = -t;
				}
				if (grid[curX][curY] == '\\') {
					swap(dirX, dirY);
				}
				curX += dirX;
				curY += dirY;
			}
			curX = i+1; curY = j;
			dirX = +1; dirY = 0;
			while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
				if (grid[curX][curY] == '#')
					break;
				if (grid[curX][curY] == '|' || grid[curX][curY] == '-') {
					udAcceptable = false;
					break;
				}
				if (grid[curX][curY] == '/') {
					int t = dirX;
					dirX = -dirY;
					dirY = -t;
				}
				if (grid[curX][curY] == '\\') {
					swap(dirX, dirY);
				}
				curX += dirX;
				curY += dirY;
			}
			bool lrAcceptable = true;
			curX = i; curY = j-1;
			dirX = 0; dirY = -1;
			while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
				if (grid[curX][curY] == '#')
					break;
				if (grid[curX][curY] == '|' || grid[curX][curY] == '-') {
					lrAcceptable = false;
					break;
				}
				if (grid[curX][curY] == '/') {
					int t = dirX;
					dirX = -dirY;
					dirY = -t;
				}
				if (grid[curX][curY] == '\\') {
					swap(dirX, dirY);
				}
				curX += dirX;
				curY += dirY;
			}
			curX = i; curY = j+1;
			dirX = 0; dirY = 1;
			while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
				if (grid[curX][curY] == '#')
					break;
				if (grid[curX][curY] == '|' || grid[curX][curY] == '-') {
					lrAcceptable = false;
					break;
				}
				if (grid[curX][curY] == '/') {
					int t = dirX;
					dirX = -dirY;
					dirY = -t;
				}
				if (grid[curX][curY] == '\\') {
					swap(dirX, dirY);
				}
				curX += dirX;
				curY += dirY;
			}
			
			if (udAcceptable) {
				curX = i-1; curY = j;
				dirX = -1; dirY = 0;
				while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
					if (grid[curX][curY] == '#')
						break;
					if (grid[curX][curY] == '.') {
						lasers[curX][curY].push_back(2*curIdx);
					}
					if (grid[curX][curY] == '/') {
						int t = dirX;
						dirX = -dirY;
						dirY = -t;
					}
					if (grid[curX][curY] == '\\') {
						swap(dirX, dirY);
					}
					curX += dirX;
					curY += dirY;
				}
				curX = i+1; curY = j;
				dirX = 1; dirY = 0;
				while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
					if (grid[curX][curY] == '#')
						break;
					if (grid[curX][curY] == '.') {
						lasers[curX][curY].push_back(2*curIdx);
					}
					if (grid[curX][curY] == '/') {
						int t = dirX;
						dirX = -dirY;
						dirY = -t;
					}
					if (grid[curX][curY] == '\\') {
						swap(dirX, dirY);
					}
					curX += dirX;
					curY += dirY;
				}
			} else {
				// add not curIdx to graph
				heen[2*curIdx].push_back(2*curIdx+1);
				terug[2*curIdx+1].push_back(2*curIdx);
			}
			if (lrAcceptable) {
				curX = i; curY = j-1;
				dirX = 0; dirY = -1;
				while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
					if (grid[curX][curY] == '#')
						break;
					if (grid[curX][curY] == '.') {
						lasers[curX][curY].push_back(2*curIdx+1);
					}
					if (grid[curX][curY] == '/') {
						int t = dirX;
						dirX = -dirY;
						dirY = -t;
					}
					if (grid[curX][curY] == '\\') {
						swap(dirX, dirY);
					}
					curX += dirX;
					curY += dirY;
				}
				curX = i; curY = j+1;
				dirX = 0; dirY = 1;
				while (curX >= 0 && curX < R && curY >= 0 && curY < C) {
					if (grid[curX][curY] == '#')
						break;
					if (grid[curX][curY] == '.') {
						lasers[curX][curY].push_back(2*curIdx+1);
					}
					if (grid[curX][curY] == '/') {
						int t = dirX;
						dirX = -dirY;
						dirY = -t;
					}
					if (grid[curX][curY] == '\\') {
						swap(dirX, dirY);
					}
					curX += dirX;
					curY += dirY;
				}
			} else {
				// add curIdx to graph
				heen[2*curIdx+1].push_back(2*curIdx);
				terug[2*curIdx].push_back(2*curIdx+1);
			}
			
			// another laser done
			curIdx++;
		}
	}
	
	// Second iteration, find empty cells
	bool isPossible = true;
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			if (grid[i][j] != '.')
				continue;
			
			if (lasers[i][j].size() == 0) {
				isPossible = false;
				break;
			}
			
			if (lasers[i][j].size() == 1) {
				heen[lasers[i][j][0] ^ 1].push_back(lasers[i][j][0]);
				terug[lasers[i][j][0]].push_back(lasers[i][j][0] ^ 1);
			} else {
				heen[lasers[i][j][0] ^ 1].push_back(lasers[i][j][1]);
				terug[lasers[i][j][1]].push_back(lasers[i][j][0]^1);
				heen[lasers[i][j][1] ^ 1].push_back(lasers[i][j][0]);
				terug[lasers[i][j][0]].push_back(lasers[i][j][1]^1);
			}
		}
	}
	
	cout << "Case #" << t << ": ";
	
	if (!isPossible) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	
	vector<bool> res = two_sat(heen, terug);
	if (res.size() != curIdx*2) {
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	cout << "POSSIBLE" << endl;
	
	// Third iteration, set laser directions
	curIdx = 0;
	for (int i=0; i<R; i++) {
		for (int j=0; j<C; j++) {
			if (grid[i][j] == '|' || grid[i][j] == '-') {
				if (res[2*curIdx])
					grid[i][j] = '|';
				else
					grid[i][j] = '-';
				curIdx++;
			}
			cout << grid[i][j];
		}
		cout << endl;
	}
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++)
		doCase(i+1);
	return 0;
}
