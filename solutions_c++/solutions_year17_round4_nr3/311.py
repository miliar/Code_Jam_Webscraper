#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;

char M[80][80];
int ID[80][80];
vi comp[80][80];

struct satisfiability_twosat
{
	int n;
	vector<vector<int>> imp;

	satisfiability_twosat(int n) : n(n), imp(2 * n) {}

	void add_edge(int u, int v)
	{
		imp[u].push_back(v);
	}

	int neg(int u) { return (n << 1) - u - 1; }

	void implication(int u, int v)
	{
		add_edge(u, v);
		add_edge(neg(v), neg(u));
	}

	void add_or(int u, int v){
		// cout << "(" << u << " | " << v << " )" << endl;
		implication(neg(u), v);
	}

	vector<bool> solve()
	{
		int size = 2 * n;
		vector<int> S, B, I(size);

		function<void(int)> dfs = [&](int u)
		{
			B.push_back(I[u] = S.size());
			S.push_back(u);

			for (int v : imp[u])
				if (!I[v]) dfs(v);
				else while (I[v] < B.back()) B.pop_back();

			if (I[u] == B.back())
				for (B.pop_back(), ++size; I[u] < S.size(); S.pop_back())
					I[S.back()] = size;
		};

		for (int u = 0; u < 2 * n; ++u)
			if (!I[u]) dfs(u);

		vector<bool> values(n);

		for (int u = 0; u < n; ++u)
			if (I[u] == I[neg(u)]) return {};
			else values[u] = I[u] < I[neg(u)];

		return values;
	}
};

int r, c;
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

bool move(int x, int y, int d, int id){
	// cout << "begin: " << x << " " << y << " " << d << endl;
	while (true){
		// cout << x << " " << y << " " << d << endl;
		if (0 <= x && x < r && 0 <= y && y < c){
			if (M[x][y] == '.'){
				comp[x][y].push_back(id);
				x += dx[ d ];
				y += dy[ d ];
			}
			else if (M[x][y] == '#')
				return true;
			else if (M[x][y] == '|' || M[x][y] == '-')
				return false;
			else if (M[x][y] == '\\'){
				d ^= 1;
				x += dx[ d ];
				y += dy[ d ];
			}
			else if (M[x][y] == '/'){
				d = 3 - d;
				x += dx[ d ];
				y += dy[ d ];
			}
		}
		else
			return true;
	}
}

void solve(){
	cin >> r >> c;

	for (int i = 0; i < r; ++i)
		cin >> M[i];

	memset(ID, 0, sizeof ID);

	int t = 0;

	for (int i = 0; i < r; ++i){
		for (int j = 0; j < c; ++j){
			comp[i][j].clear();
			if (M[i][j] == '|' || M[i][j] == '-')
				ID[i][j] = t++;
		}
	}

	satisfiability_twosat g(t);

	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j){
			if (M[i][j] == '|' || M[i][j] == '-'){
				int id = ID[i][j];
				bool a = true, b = true;
				a &= move(i - 1, j, 0, id);
				a &= move(i + 1, j, 2, id);
				b &= move(i, j - 1, 1, g.neg(id));
				b &= move(i, j + 1, 3, g.neg(id));

				// cout << a << " " << b << " " << endl;

				if (!a) g.add_or(g.neg(id), g.neg(id));
				if (!b) g.add_or(id, id);
			}
		}

	for (int i = 0; i < r; ++i)
		for (int j = 0; j < c; ++j)
			if (M[i][j] == '.'){
				if (comp[i][j].empty() || comp[i][j].size() > 2){
				 	cout << "IMPOSSIBLE" << endl;
				 	return;
				}
				else if (comp[i][j].size() == 2){
					g.add_or(comp[i][j][0], comp[i][j][1]);
				}
				else{
					g.add_or(comp[i][j][0], comp[i][j][0]);
				}
			}

	auto answer = g.solve();

	if (answer.empty())
		cout << "IMPOSSIBLE" << endl;
	else{
		cout << "POSSIBLE" << endl;
		for (int i = 0; i < r; ++i){
			for (int j = 0; j < c; ++j){
				if (M[i][j] == '|' || M[i][j] == '-')
					cout << (answer[ ID[i][j] ] ? '|' : '-');
				else
					cout << M[i][j];
			}
			cout << endl;
		}
	}

}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int t; cin >> t;
	int tc = 1;

	while (t--){
		cout << "Case #" << tc++ << ": ";
		solve();
	}
	
}