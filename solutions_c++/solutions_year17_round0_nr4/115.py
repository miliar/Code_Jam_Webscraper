#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <queue>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define maxN 100

struct Data {
	char a;
	int r, c;
	bool operator <(const Data &o) const {
		return r < o.r || r == o.r && c < o.c;
	}
};

int row[maxN], col[maxN], d1[2 * maxN], d2[2 * maxN], l[2*maxN], r[2*maxN], v[2*maxN];
char mat[maxN][maxN];
vi edges[2*maxN];

bool dfs(int n) {
	if (v[n]) return false;
	v[n] = true;
	FOR(i, 0, edges[n].size()) {
		int next = edges[n][i];
		if (r[next] == -1 || dfs(r[next])) {
			r[next] = n;
			l[n] = next;
			return true;
		}
	}
	return false;
}

int main() {
	int T, caso = 1, N, M, a, b;
	char c;
	cin >> T;
	while (T--) {
		cin >> N >> M;
		FOR(i, 0, N) FOR(j, 0, N) mat[i][j] = '.';
		FOR(i, 0, N) row[i] = col[i] = 0;
		FOR(i, 0, 2 * N) d1[i] = d2[i] = 0, r[i] = l[i] = -1;
		FOR(i, 0, 2 * N) edges[i].clear();
		int mans = 0;
		FOR(i, 0, M) {
			cin >> c >> a >> b;
			a--, b--;
			mat[a][b] = c;
			if (c == 'o' || c=='x') {
				row[a] = 1, col[b] = 1;
				mans++;
			}
			if (c == '+' || c=='o') {
				d1[a + b] = d2[N + a - b] = 1;
				mans++;
			}
		}
		vector<Data> ans;
		FOR(i, 0, N) {
			FOR(j, 0, N) {
				if (!d1[i + j] && !d2[N + i - j]) {
					edges[i + j].pb(N + i - j);
				}
			}
		}
		FOR(i, 0, 2*N) {
			memset(v, 0, sizeof(v));
			if (l[i]==-1 && dfs(i)) mans++;
		}
		FOR(i, 0, 2*N) {
			if (~l[i]) {
				int a = (l[i] + i - N) / 2;
				mat[a][i - a] = mat[a][i - a] == '.' ? '+' : 'o';
				ans.push_back(Data{ mat[a][i - a], a + 1, i - a + 1 });
			}
		}
		FOR(i, 0, N) {
			FOR(j, 0, N) {
				if (!row[i] && !col[j]) {
					mans++;
					row[i] = col[j] = 1;
					ans.push_back(Data{ mat[i][j]=='.'?'x':'o', i + 1, j + 1 });
				}
			}
		}
		sort(ans.begin(), ans.end());
		vector<Data> rans;
		FOR(i, 0, ans.size()) {
			if (i&&ans[i - 1].r == ans[i].r && ans[i - 1].c == ans[i].c) {
				rans[rans.size() - 1].a = 'o';
			}
			else rans.push_back(ans[i]);
		}
		cout << "Case #" << caso++ << ": " << mans << " " << rans.size() << endl;
		FOR(i, 0, rans.size()) {
			cout << rans[i].a << " " << rans[i].r << " " << rans[i].c << endl;
		}
	}
	return 0;
}
