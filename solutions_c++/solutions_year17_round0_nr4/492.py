#include <bits/stdc++.h>

using namespace std;

bool check(const vector<string> &G) {
	const int N = G.size();

	for (int r1 = 0; r1 < N; ++r1) {
		for (int c1 = 0; c1 < N; ++c1) {

			for (int r2 = r1+1; r2 < N; ++r2) {
				if (G[r1][c1] == '.' || G[r2][c1] == '.')
					continue;
				if (!(G[r1][c1] == '+' || G[r2][c1] == '+'))
					return false;
			}


			for (int c2 = c1+1; c2 < N; ++c2) {
				if (G[r1][c1] == '.' || G[r1][c2] == '.')
					continue;
				if (!(G[r1][c1] == '+' || G[r1][c2] == '+'))
					return false;
			}


			for (int d = 1; d < N; ++d) {
				if (r1+d < N && c1+d < N) {
					if (!(G[r1][c1] == '.' || G[r1+d][c1+d] == '.')) {
						if (!(G[r1][c1] == 'x' || G[r1+d][c1+d] == 'x')) {
							return false;
						}
					}
				}

				if (r1-d >= 0 && c1+d < N) {
					if (!(G[r1][c1] == '.' || G[r1-d][c1+d] == '.')) {
						if (!(G[r1][c1] == 'x' || G[r1-d][c1+d] == 'x'))
							return false;
					}
				}
			}
		}
	}

	return true;
}

int score(const vector<string> &G) {
	vector<int> sc(300);
	sc['+'] = sc['x'] = 1;
	sc['o'] = 2;
	int ans = 0;
	for (const auto &s : G) {
		for (char c : s) {
			ans += sc[c];
		}
	}
	return ans;
}

struct Searcher {
	vector<string> G, bestG;
	// vector<vector<string>> bestGs;
	int best;

	set<vector<string>> done;


	void place(int r, int c, char type) {
		char prevt = G[r][c];
		G[r][c] = type;
		search();
		G[r][c] = prevt;
	}

	void search() {
		if (!check(G))
			return;
		if (done.count(G))
			return;
		done.insert(G);
		const int N = G.size();
		int sc = score(G);
		if (sc > best) {
			best = sc;
			bestG = G;
		}
		for (int r = 0; r < N; ++r) {
			for (int c = 0; c < N; ++c) {
				if (G[r][c] == '.') {
					place(r,c,'+');
					place(r,c,'o');
					place(r,c,'x');
				}
				if (G[r][c] == '+' || G[r][c] == 'x') {
					place(r,c,'o');
				}
			}
		}
	}

	vector<string> run(const vector<string> &V) {
		G = V;
		best = -1;
		done.clear();
		search();
		return bestG;
	}
};


vector<string> solve_first_row(const vector<string> &G) {
	const int N = G.size();

	if (N == 1) {
		return {"o"};
	}
	
	auto ans = G;
	
	int o_col = -1, x_col = -1;
	for (int c = 0; c < N; ++c) {
		if (G[0][c] == 'o') {
			o_col = c;
		}
		if (G[0][c] == 'x') {
			x_col = c;
		}
	}

	if (o_col != -1) {
		for (int c = 0; c < N; ++c) {
			if (c == o_col)
				continue;
			ans[0][c] = '+';
		}
	} else if (x_col != -1) {
		for (int c = 0; c < N; ++c) {
			if (c == x_col) {
				o_col = c;
				ans[0][c] = 'o';
			}
			else
				ans[0][c] = '+';
		}
	} else {
		ans[0][0] = 'o';
		o_col = 0;
		for (int c = 1; c < N; ++c) {
			ans[0][c] = '+';
		}
	}



	for (int c = 1; c < N-1; ++c) {
		ans[N-1][c] = '+';
	}

	set<int> rows, cols;
	for (int i = 0; i < N; ++i) {
		rows.insert(i);
		cols.insert(i);
	}




	rows.erase(0);
	cols.erase(o_col);
	rows.erase(N-1);

	if (o_col > 0) {
		ans[N-1][0] = 'x';
		cols.erase(0);
	} else {
		ans[N-1][N-1] = 'x';
		cols.erase(N-1);
	}


	int todo = N-2;

	while (todo > 0) {
		assert(rows.size() && cols.size());
		int r = *rows.begin(), c = *cols.begin();
		rows.erase(r);
		cols.erase(c);
		ans[r][c] = 'x';
		--todo;
	}
	
	return ans;
}

void solve() {
	int N, M;
	cin >> N >> M;
	vector<string> G(N, string(N, '.'));
	for (int i = 0; i < M; ++i) {
		char c;
		int x, y;
		cin >> c >> x >> y;
		--x; --y;
		G[x][y] = c;
	}
	auto ans = solve_first_row(G);

	vector<tuple<char, int, int>> changes;

	for (int r = 0; r < N; ++r) {
		for (int c = 0; c < N; ++c) {
			if (ans[r][c] != G[r][c]) {
				changes.emplace_back(ans[r][c], r,c );
			}
		}
	}

	cout << score(ans) << " " << changes.size() << endl;
	for (const auto &c : changes) {
		cout << get<0>(c) << " " << get<1>(c)+1 << " " << get<2>(c)+1 << endl;
	}

}

void test() {
	default_random_engine re;
	string types = ".+ox";
	int N = 5;
	Searcher searcher;
	for (int tc = 0; tc < 100; ++tc) {
		vector<string> V(N, string(N, '.'));
		for (int c = 0; c < N; ++c) {
			V[0][c] = types[re()%4];
		}
		if (!check(V)) {
			--tc;
			continue;
		}
		cout << tc << endl;
		for (auto s : V) {
			cout << s << endl;
		}

		auto fr = solve_first_row(V);
		auto se = searcher.run(V);


		for (auto s : fr) {
			cout << s << endl;
		}
		cout << "----" << endl;
		assert(check(fr));

		for (auto s : se) {
			cout << s << endl;
		}
		cout << "----" << endl;
		assert(check(se));

		cout << score(se) << " " << score(fr) << endl;
		assert(score(se) == score(fr));

	}

}



int main() {
	// test();
	// return 0;
	int T;
	cin >> T;
	for (int tc = 0; tc < T; ++tc) {
		cout << "Case #" << (tc+1) << ": ";
		solve();
	}
}