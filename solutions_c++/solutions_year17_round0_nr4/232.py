#include <bits/stdc++.h>
using namespace std;

class BipartiteGraph {
    public:
    bool visited[222];
    int with[222], flow[222][222], m, n;
    void reset(int _m,int _n) {
        m = _m; n = _n;
        memset(with, -1, sizeof with);
        memset(flow, 0, sizeof flow);
    }
    void addEdge(int a, int b) {
        flow[a][b] = 1;
    }

    bool match(int x) {
        for (int j = 0; j < n; j++){
        	if(flow[x][j] == 1 && !visited[j]){
	            visited[j] = 1;
	            if (with[j] == -1 || match(with[j])) {
	                with[j] = x;
	                return true;
	            }
        	}
        }
        return false;
    }

    int countMCBM() {
        int ans = 0;
        memset(with, -1, sizeof with);
        for (int i = 0; i < m; i++) {
            memset(visited, false, sizeof visited);
            if(match(i)) ++ans;
        }
        return ans;
    }
};

BipartiteGraph graphX, graphP;

int n, m;
int X[222][222], P[222][222];

void solve() {
	scanf("%d%d", &n, &m);
	graphX.reset(n, n); // two X cannot be on same row or column
	graphP.reset(2*n-1, 2*n-1); // two + cannot be on same diagonal
	memset(X, 0, sizeof X);
	memset(P, 0, sizeof P);
	for (int i = 0; i < m; i++) {
		char s[6]; int r, c;
		scanf("%s%d%d", s, &r, &c);
		r--; c--;
		if (s[0] == '+' || s[0] == 'o') {
			// block other, except itself
			for (int j = 0; j < 222; j++) {
				P[r+c][j] = -1;
				P[j][r-c+n-1] = -1;
			}
			// occupy diagonal
			P[r+c][r-c+n-1] = 1;
		}
		if (s[0] == 'x' || s[0] == 'o') {
			// block other, except itself
			for (int j = 0; j < 222; j++) {
				X[r][j] = -1;
				X[j][c] = -1;
			}
			// occupy row and column
			X[r][c] = 1;
		}
	}
	// add to graph
	for (int r = 0; r < n; r++)
		for (int c = 0; c < n; c++) {
			if (X[r][c] != -1) {
				graphX.addEdge(r, c);
			}
			if (P[r+c][r-c+n-1] != -1) {
				graphP.addEdge(r+c, r-c+n-1);
			}
		}
	// calculate
	int res = graphX.countMCBM() + graphP.countMCBM();
	vector<pair<int, pair<int, int> > > editted;
	for (int r = 0; r < n; r++)
		for (int c = 0; c < n; c++) {
			int x = (graphX.with[c] == r), p = (graphP.with[r-c+n-1] == r+c);
			int xx = (X[r][c] == 1), pp = (P[r+c][r-c+n-1] == 1);
			if (x != xx || p != pp) {
				editted.push_back(make_pair(x+p*2, make_pair(r, c)));
			}
		}
	printf("%d %d\n", res, int(editted.size()));
	for (auto item: editted) {
		printf("%c %d %d\n", ".x+o"[item.first], item.second.first+1, item.second.second+1);
	}
}

int main() {
	freopen("D.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		solve();
	}
}