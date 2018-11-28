#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

struct Laser {
	bool hor, done;
	int cnter;
};

struct Empty {
	int lvh[2];
	bool done;
};

vector<Laser> lasers;
vector<Empty> emptys;
const int R = 55;
int numbers[R][R];
int r, c;
vector<string> f;

bool go(int i, int j, int di, int dj, vector<pair<int, bool>> &res) {
	while (true) {
		i += di;
		j += dj;
		if (i < 0 || i >= r) return true;
		if (j < 0 || j >= c) return true;
		char ch = f.at(i).at(j);
		if (ch == '.') {
			res.emplace_back(numbers[i][j], di == 0);
		} else if (ch == '-' || ch == '|') {
			return false;
		} else if (ch == '/') {
			swap(di, dj);
			di = -di;
			dj = -dj;
		} else if (ch == '\\') {
			swap(di, dj);
		} else {
			assert(ch == '#');
			return true;
		}
	}
}

void fail() {
	cout << "IMPOSSIBLE\n";
}


vector<vector<int>> impl, rimpl;
vector<char> used;
vector<int> order, comp;

void dfs1(int v) {
	used[v] = true;
	for (size_t i=0; i < impl[v].size(); ++i) {
		int to = impl[v][i];
		if (!used[to])
			dfs1(to);
	}
	order.emplace_back(v);
}

void dfs2(int v, int cl) {
	comp[v] = cl;
	for (size_t i = 0; i < rimpl[v].size(); ++i) {
		int to = rimpl[v][i];
		if (comp[to] == -1)
			dfs2(to, cl);
	}
}

bool findsolution() {
	impl.clear();
	rimpl.clear();
	order.clear();
	comp.clear();
	emptys.erase(remove_if(all(emptys), [](const Empty &e) {return e.done;}), end(emptys));
	int cnter = 0;
	for (auto &laser: lasers) {
		if (!laser.done)
			laser.cnter = cnter++;
	}
	impl.resize(2 * cnter);
	bool skip = true;
	for (const auto &e: emptys) {
		if (skip) { skip = false; continue; }
		if (!e.lvh[0]) {
			if (!e.lvh[1])
				return false;
			else {
				int z = e.lvh[1] > 0 ? 2 * lasers.at(e.lvh[1]).cnter + 1 : 2 * lasers.at(-e.lvh[1]).cnter;
				// 0 || z
				impl[0^1].emplace_back(z);
				impl[z^1].emplace_back(0);
				// 1 || z
				impl[1^1].emplace_back(z);
				impl[z^1].emplace_back(1);
			}
		} else {
			int z = e.lvh[0] > 0 ? 2 * lasers.at(e.lvh[0]).cnter + 1 : 2 * lasers.at(-e.lvh[0]).cnter;
			if (!e.lvh[1]) {
				// 0 || z
				impl[0^1].emplace_back(z);
				impl[z^1].emplace_back(0);
				// 1 || z
				impl[1^1].emplace_back(z);
				impl[z^1].emplace_back(1);
			} else {
				int y = e.lvh[1] > 0 ? 2 * lasers.at(e.lvh[1]).cnter + 1 : 2 * lasers.at(-e.lvh[1]).cnter;
				// y || z
				impl[y^1].emplace_back(z);
				impl[z^1].emplace_back(y);
			}
		}
	}
	rimpl.resize(impl.size());
	E(cnter, impl.size());
	for (size_t i = 0; i < impl.size(); ++i) {
		for (size_t j = 0; j < impl[i].size(); ++j) {
			E(i, "->", impl[i][j]);
			rimpl[impl[i][j]].emplace_back(i);
		}
	}
	used.assign(impl.size(), false);
	for (size_t i = 0; i < impl.size(); ++i)
		if (!used[i])
			dfs1(i);
	comp.assign(impl.size(), -1);
	for (int i=0, j=0; i < int(impl.size()); ++i) {
		int v = order[int(impl.size()) - i - 1];
		if (comp[v] == -1)
			dfs2(v, j++);
	}

	for (int i = 0; i < int(impl.size()); ++i) {
		if (comp[i] == comp[i^1])
			return false;
	}
	for (auto &laser: lasers) if (!laser.done) {
		cnter = 2 * laser.cnter;
		laser.hor = (comp.at(cnter) < comp.at(cnter + 1));
	}
	return true;
}

void solve() {
	cin >> r >> c;
	f.resize(r);
	for (auto &q: f) {
		cin >> q;
		assert(int(q.size()) == c);
	}
	lasers.resize(1);
	emptys.resize(1);
	for (int i = 0; i < r; ++i) {
		for (int j = 0; j < c; ++j) {
			numbers[i][j] = 0;
			char ch = f[i][j];
			if (ch == '.') {
				numbers[i][j] = int(emptys.size());
				emptys.emplace_back(Empty{{0, 0}, false});
			} else if (ch == '-' || ch == '|') {
				numbers[i][j] = int(lasers.size());
				lasers.emplace_back(Laser{false, false, 0});
			} else {
				assert(ch == '\\' || ch == '/' || ch == '#');
			}
		}
	}
	for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) if (f[i][j] == '-' || f[i][j] == '|') {
		vector<pair<int, bool>> ver, hor;
		bool okv = go(i, j, -1, 0, ver);
		okv = okv && go(i, j, 1, 0, ver);
		bool okh = go(i, j, 0, -1, hor);
		okh = okh && go(i, j, 0, 1, hor);
		Laser &laser = lasers.at(numbers[i][j]);
		if (!okv) {
			if (!okh) {
				return fail();
			} else {
				laser.hor = true;
				laser.done = true;
				for (const auto &q: hor)
					emptys[q.first].done = true;
			}
		} else {
			if (!okh) {
				laser.hor = false;
				laser.done = true;
				for (const auto &q: ver)
					emptys[q.first].done = true;
			} else {
				for (const auto &q: hor) {
					assert(emptys[q.first].lvh[int(q.second)] == 0);
					emptys[q.first].lvh[int(q.second)] = numbers[i][j];
				}
				for (const auto &q: ver) {
					assert(emptys[q.first].lvh[int(q.second)] == 0);
					emptys[q.first].lvh[int(q.second)] = -numbers[i][j];
				}
			}
		}
	}
	for (const auto &l: lasers) { E(l.hor, l.done); }
	for (const auto &e: emptys) { E(e.lvh[0], e.lvh[1], e.done); }
	if (!findsolution())
		return fail();
	cout << "POSSIBLE\n";
	for (int i = 0; i < r; ++i) for (int j = 0;j < c; ++j) if (f[i][j] == '-' || f[i][j] == '|') {
		f.at(i).at(j) = lasers.at(numbers[i][j]).hor ? '-' : '|';
	}
	for (const auto &q: f)
		cout << q << '\n';
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}
