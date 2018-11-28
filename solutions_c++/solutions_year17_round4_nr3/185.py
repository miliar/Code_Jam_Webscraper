#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;

typedef vector<vector<int>> Graph;
class SCC
{
  public:
    vector<int> Solve(const Graph& g)
	{
		int n = g.size();

		_di = 0;
		_scc_count = 0;
		_scc_ids = vector<int>(n);
		_discovers = vector<int>(n, -1);
		_is_in_stack = vector<bool>(n);

	    for (int u = 0; u < n; ++u) {
	        if (_discovers[u] == -1) {
	            Solve(g, u);
	        }
	    }
	    return _scc_ids;
	}
	int Solve(const Graph& g, int u) {
	    int low = _discovers[u] = _di++;
		_stack.push(u);
		_is_in_stack[u] = true;
		for (int v : g[u]) {
	        if (_discovers[v] == -1) {
	            low = min(low, Solve(g, v));
	        } else if (_is_in_stack[v]) {
	            low = min(low, _discovers[v]);
	        }
	    }
	    if (low == _discovers[u]) {
	        while (true) {
	            int v = _stack.top();
				_stack.pop();
				_is_in_stack[v] = false;
				_scc_ids[v] = _scc_count;
	            if (u == v) {
	                break;
	            }
	        }
	        ++_scc_count;
	    }
	    return low;
	}

	int _di;
	int _scc_count;
	vector<int> _scc_ids;
	vector<int> _discovers;
	vector<bool> _is_in_stack;
    stack<int> _stack;
};

class TwoSAT
{
public:
	TwoSAT(int n) : g(2*(n+1)) {}

	void UorV(int u, int v)
	{
	    NotUtoV(u, v);
	    NotUtoV(v, u);
	}

	void UtoV(int u, int v)
	{
	    g[2*u].push_back(2*v);
	}

	void NotUtoV(int u, int v)
	{
	    g[2*u+1].push_back(2*v);
	}

	void UtoNotV(int u, int v)
	{
	    g[2*u].push_back(2*v+1);
	}

	void NotUtoNotV(int u, int v)
	{
	    g[2*u+1].push_back(2*v+1);
	}

	// Solve 2-SAT problem.
	vector<bool> Solve()
	{
	    // Find SCC of given graph.
	    SCC scc;
	    vector<int> sccId = scc.Solve(g);

	    // number of variables.
	    int n = g.size() / 2;

	    // if a variable and its complement are in the same component,
	    // than there is no solution.
	    for (int i = 0; i < 2*n; i += 2) {
	        if (sccId[i] == sccId[i+1]) {
	            return vector<bool>();
	        }
	    }
	    // Topological order of the SCC.
	    vector<pair<int, int> > torder;
	    for (int i = 0; i < 2*n; ++i) {
	        torder.push_back(make_pair(sccId[i], i));
	    }
	    // Topological order is inverse of scc id.
	    sort(torder.rbegin(), torder.rend());

	    // Assign
	    vector<bool> res(n);
	    vector<bool> visit(n ,false);
	    for (int i = 0; i < 2*n; ++i) {
	        int u = torder[i].second;
	        int v = u / 2;
	        bool is = u % 2;
	        if (visit[v]) {
	            continue;
	        }
	        res[v] = is;
	        visit[v] = true;
	    }
	    return res;
	}
private:
    Graph g;
};


int R, C;
char A[51][51];
char B[51][51];
int P[51][51];


bool solve(int p) {
	TwoSAT ts(p);
	for (int y = 0; y < R; ++y) {
		for (int x = 0; x < C; ++x) {
			if (A[y][x] != '#') {
				vector<int> h, v;
				for (int xx = x - 1; xx >= 0 && A[y][xx] != '#'; --xx) {
					if (P[y][xx] > 0) {
						h.push_back(P[y][xx]);
					}
				}
				for (int xx = x + 1; xx < C && A[y][xx] != '#'; ++xx) {
					if (P[y][xx] > 0) {
						h.push_back(P[y][xx]);
					}
				}
				for (int yy = y - 1; yy >= 0 && A[yy][x] != '#'; --yy) {
					if (P[yy][x] > 0) {
						v.push_back(P[yy][x]);
					}
				}
				for (int yy = y + 1; yy < R && A[yy][x] != '#'; ++yy) {
					if (P[yy][x] > 0) {
						v.push_back(P[yy][x]);
					}
				}
				if (A[y][x] == '.') {
					if (h.size() + v.size() == 0) return false;
					if (h.size() > 1 && v.size() > 1) return false;
					if (h.size() == 0 && v.size() > 1) return false;
					if (v.size() == 0 && h.size() > 1) return false;
					if (h.size() > 1) {
						for (int p : h) ts.UtoNotV(p, p);
						ts.UtoNotV(v[0], v[0]);
					}
					else if (v.size() > 1) {
						for (int p : v) ts.NotUtoV(p, p);
						ts.NotUtoV(h[0], h[0]);
					}
					else if (h.size() == 1 && v.size() == 1) {
						ts.NotUtoNotV(h[0], v[0]);
						ts.UtoV(v[0], h[0]);
					}
					else if (h.size() == 1) {
						ts.NotUtoV(h[0], h[0]);
					} else {
						ts.UtoNotV(v[0], v[0]);
					}
				} else {
					if (h.size() > 0 && v.size() > 0) return false;
					if (h.size() > 0) {
						for (int p: h) ts.UtoNotV(p, p);
						ts.UtoNotV(P[y][x], P[y][x]);
					}
					else if (v.size() > 0) {
						for (int p: v) ts.NotUtoV(p, p);
						ts.NotUtoV(P[y][x], P[y][x]);
					}
				}
			}
		}
	}
	vector<bool> res = ts.Solve();
	if (res.size() == 0) return false;
	else {
		for (int y = 0; y < R; ++y) {
			for (int x = 0; x < C; ++x) {
				if (P[y][x] > 0) {
					if (res[P[y][x]]) {
						B[y][x] = '-';
					} else {
						B[y][x] = '|';
					}
				} else {
					B[y][x] = A[y][x];
				}
			}
		}
	}
	return true;
}

int main() {
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; ++tc) {
		memset(P, 0, sizeof(P));
		memset(B, 0, sizeof(B));
		scanf("%d%d", &R, &C);
		int p = 0;
		for (int y = 0; y < R; ++y) {
			scanf("%s", A[y]);
			for (int x = 0; x < C; ++x) {
				if (A[y][x] == '|' || A[y][x] == '-') {
					P[y][x] = ++p;
				}
			}
		}
		bool res = solve(p);
		printf("Case #%d: %s\n", tc, res ? "POSSIBLE" : "IMPOSSIBLE");
		if (res) {
			for (int y = 0; y < R; ++y) {
				printf("%s\n", B[y]);
			}
		}
	}
	return 0;
}

