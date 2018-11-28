#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string problemName = "D";
string smallFileName = problemName + "-small-attempt0";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

template <int N, int M>
struct Graph {
	const int INF = 1000000000;
	struct Edge {
		int w, cap, next;
		Edge(int iw = -1, int icap = 0, int inext = -1) : w(iw), cap(icap), next(inext) {}
	};
	int first[N], d[N], st[N], cur[N], sz, n, m, s, t;
	Edge E[2 * M];
	void init(int in) {
		n = in; m = 0;
		REP(i, n) first[i] = -1;
	}
	inline void add(int q, int w, int cap) {
		E[m] = Edge(w, cap, first[q]); first[q] = m++;
		E[m] = Edge(q, 0, first[w]);  first[w] = m++;
	}
	bool bfs()
	{
		REP(i, n) d[i] = -1;
		sz = 1; st[0] = t; d[t] = 0;
		for (int cr = 0; cr < sz; ++cr)
		{
			int x = st[cr];
			for (int e = first[x]; e > -1; e = E[e].next)
				if (E[e ^ 1].cap && d[E[e].w] == -1)
				{
					d[E[e].w] = d[x] + 1;
					st[sz++] = E[e].w;
				}
		}
		return d[s] > -1;
	}
	int dfs(int x, int flow)
	{
		if (x == t) return flow;
		for (int & e = cur[x]; e > -1; e = E[e].next) {
			if (E[e].cap && d[E[e].w] == d[x] - 1)
			{
				int v = dfs(E[e].w, min(flow, E[e].cap));
				if (v)
				{
					E[e].cap -= v;
					E[e ^ 1].cap += v;
					return v;
				}
			}
		}
		return 0;
	}

	ll max_flow(int is, int it) {
		s = is; t = it;
		ll res = 0;
		while (bfs()) {
			REP(i, n) cur[i] = first[i];
			while (1)
			{
				int val = dfs(s, INF);
				if (!val) break;
				res += val;
			}
		}
		return res;
	}
};

const int N = 100;

Graph<500, 250000> g;

int n;

int solve(int py[N][N], int px[N][N], int cy, int cx, bool v[N][N]) {
//	cout << "PASS" << endl;
	g.init(cy + cx + 2);
	int s = cy + cx;
	int t = cy + cx + 1;
	vector<int> cnty(cy, 1);
	vector<int> cntx(cx, 1);
	REP(i, n) {
		REP(j, n) if (v[i][j]) {
			cnty[py[i][j]]--;
			cntx[px[i][j]]--;
		} else {
			g.add(py[i][j], px[i][j] + cy, 1);
			//cout << py[i][j] << ' ' << px[i][j] + cy << endl;
		}
	}
	REP(i, cy)
		if (cnty[i]) {
			g.add(s, i, 1);
			//cout << s << ' ' << i << endl;
		}
	REP(i, cx)
		if (cntx[i]) {
			g.add(i + cy, t, 1);
			//cout << i + cy << ' ' << t << endl;
		}
	ll ans = g.max_flow(s, t);
	FOR(i, cy, cy + cx) {
		for (int e = g.first[i]; e > -1; e = g.E[e].next) {
			if (g.E[e].w < cy && g.E[e].cap) {
				int to = i - cy;
				int from = g.E[e].w;
				//cout << "Add " << from << ' ' << to << endl;
				REP(yy, n) {
					REP(xx, n) {
						if (py[yy][xx] == from && px[yy][xx] == to) {
							v[yy][xx] = true;
							//cout << "Actual add" << yy << ' ' << xx << endl;
						}
					}
				}
			}
		}
	}
	return ans;
}

bool marked[2][N][N];
bool markedmod[2][N][N];
int py[N][N];
int px[N][N];

int main() {
	freopen(inputFileName.data(), "r", stdin);
	freopen(outputFileName.data(), "w", stdout);
	int T;
	cin >> T;
	REP(test, T) {
		int k;
		cin >> n >> k;
		memset(marked, 0, sizeof(marked));
		int ans = 0;
		REP(i, k) {
			char c;
			int y, x;
			cin >> c >> y >> x;
			--y, --x;
			if (c == 'x' || c == 'o') {
				marked[0][y][x] = true;
				ans++;
			}
			if (c == '+' || c == 'o') {
				marked[1][y][x] = true;
				ans++;
			}
		}
		memcpy(markedmod, marked, sizeof(marked));
		REP(i, n) {
			REP(j, n) {
				py[i][j] = i;
				px[i][j] = j;
			}
		}
		ans += solve(py, px, n, n, markedmod[0]);
		REP(i, n) {
			REP(j, n) {
				py[i][j] = i-j+n-1;
				px[i][j] = i+j;
			}
		}
		ans += solve(py, px, 2*n-1, 2*n-1, markedmod[1]);
		cout << "Case #" << (test + 1) << ": ";
		int mod = 0;
		REP(i, n) {
			REP(j, n) {
				if (marked[0][i][j] != markedmod[0][i][j] || marked[1][i][j] != markedmod[1][i][j])
					++mod;
			}
		}
		cout << ans << ' ' << mod << endl;
		REP(i, n) {
			REP(j, n) {
				if (marked[0][i][j] != markedmod[0][i][j] || marked[1][i][j] != markedmod[1][i][j]) {
					char c;
					if (markedmod[0][i][j] && markedmod[1][i][j]) {
						c = 'o';
					}
					else if (markedmod[0][i][j]) {
						c = 'x';
					}
					else c = '+';
					cout << c << ' ' << (i + 1) << ' ' << (j + 1) << endl;
				}
			}
		}
	}
	return 0;
}
