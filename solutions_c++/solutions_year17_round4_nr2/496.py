#include<bits/stdc++.h>
using namespace std;


void solve() {
	int N, C, M;
	int x[1024], y[1024];
	cin >> N >> C >> M;
	map<int, int> u, v;
	for(int i = 0, x, y; i < M; ++i) {
		cin >> x >> y;
		++u[x];
		++v[y];
	}
	int l = 0, r = M;
	for(auto & p : v)
		l = max(l, p.second - 1);
	static int uu[1024];
	for(;l + 1 < r;) {
		int m = l + r >> 1;
		fill_n(uu + 1, N, m);
		bool bad = false;
		for(auto&p : u) {
			int s = p.first, c = p.second;
			for(int t; s >= 1 && c > 0; --s, c -= t) {
				t = min(uu[s], c);
				uu[s] -= t;
			}
			if(c) {bad = true; break;}
		}
		if(bad) l = m; else r = m;
	}

	fill_n(uu + 1, N, r);
	int t = M;
	for(auto&p : u) t -= min(r, p.second);
	cout << r << " " << t << endl;
	
}

int main() {
	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
	}
}
