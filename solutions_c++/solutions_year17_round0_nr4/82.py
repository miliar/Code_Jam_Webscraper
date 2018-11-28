#include <bits/stdc++.h>

using namespace std;

struct Diag {
	vector<int> edges;
	bool visited;
	int f;
	
	bool taken;
};

int n, m;
vector<Diag> graph;

int getDiag(int r, int c, bool d) {
	if(d) {
		r = n - r - 1;
	}

	int mmin = min(r, c);
	r -= mmin;
	c -= mmin;

	int ret = 0;
	if(d) {
		ret += n*2 - 1;
	}

	if(r == 0) {
		return c + ret;
	}
	else {
		return n + r - 1 + ret;
	}
}

pair<int, int> getPos(int u, int d) {
	for(int r = 0; r < n; r++) {
		for(int c = 0; c < n; c++) {
			if(getDiag(r, c, false) == u && getDiag(r, c, true) == d) {
				return make_pair(r, c);
			}
		}
	}
	return make_pair(-100, -100);
}

vector<bool> used;

bool augment(int d) {
	//cerr << d << endl;
	if(graph[d].visited || graph[d].taken || used[d]) {
		return false;
	}

	for(int i = 0; i < graph[d].edges.size(); i++) {
		int e = graph[d].edges[i];
		if(graph[e].taken || used[e]) continue;

		if(graph[e].visited) {
			int f = graph[e].f;
			used[d] = true;
			used[e] = true;
			//graph[d].taken = true;
			//graph[e].taken = true;

			graph[f].visited = false;
			if(augment(f)) {
				graph[f].visited = true;
				//graph[d].taken = false;
				//graph[e].taken = false;

				graph[d].visited = true;
				graph[e].visited = true;
				graph[d].f = e;
				graph[e].f = d;
				return true;
			}
			else {
				graph[f].visited = true;
				//graph[d].taken = false;
				//graph[e].taken = false;
			}
		}
		else {
			graph[d].visited = true;
			graph[e].visited = true;
			graph[d].f = e;
			graph[e].f = d;
			return true;
		}
	}

	return false;
}

void runTestCase(int t) {
	cin >> n >> m;

	vector<vector<int>> board(n, vector<int>(n, 0));
	graph = vector<Diag>(4*n-2);
	for(int i = 0; i < m; i++) {
		char model;
		int r, c;
		cin >> model >> r >> c;
		r--;
		c--;

		int type;
		if(model == '+') {
			type = 1;
		}
		else if(model == 'x') {
			type = 2;
		}
		else {
			type = 3;
		}

		board[r][c] = type;
	}

	for(int r = 0; r < n; r++) {
		for(int c = 0; c < n; c++) {
			int ud = getDiag(r, c, false);
			int dd = getDiag(r, c, true);
			graph[ud].edges.push_back(dd);
			graph[dd].edges.push_back(ud);

			if(board[r][c] == 1 || board[r][c] == 3) {
				graph[ud].taken = true;
				graph[dd].taken = true;
			}
		}
	}

	for(int i = 0; i < n*2 - 1; i++) {
		used = vector<bool>(graph.size(), false);
		//cerr << i << endl;
		augment(i);
	}

	vector<vector<int>> ans = board;

	for(int r = 0; r < n; r++) {
		for(int c = 0; c < n; c++) {
			bool good = true;
			for(int i = 0; i < n; i++) {
				if(ans[i][c] >= 2 || ans[r][i] >= 2) {
					good = false;
				}
			}
			if(good) {
				ans[r][c] += 2;
			}
		}
	}

	for(int i = 0; i < n*2 - 1; i++) {
		if(graph[i].visited) {
			auto pos = getPos(i, graph[i].f);
			ans[pos.first][pos.second] += 1;
		}
	}

	int score = 0;
	vector<string> diffs;
	for(int r = 0; r < n; r++) {
		for(int c = 0; c < n; c++) {
			//cout << ans[r][c] << " ";
			if(ans[r][c] == 1 || ans[r][c] == 2) {
				score++;
			}
			else if(ans[r][c] == 3) {
				score += 2;
			}

			if(ans[r][c] != board[r][c]) {
				stringstream ss;
				if(ans[r][c] == 1) {
					ss << "+";
				}
				else if(ans[r][c] == 2) {
					ss << "x";
				}
				else {
					ss << "o";
				}
				ss << " " << r+1 << " " << c+1;
				diffs.push_back(ss.str());
			}
		}
		//cout << endl;
	}
	
	cout << "Case #" << t << ": ";
	cout << score << " " << diffs.size() << endl;
	for(int i = 0; i < diffs.size(); i++) {
		cout << diffs[i] << endl;
	}
}

int main() {
	int t;
	cin >> t;

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}
	
	return 0;
}
