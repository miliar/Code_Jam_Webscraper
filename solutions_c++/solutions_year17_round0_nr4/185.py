#include <bits/stdc++.h>

using namespace std;

struct BipartiteMatcher {
	vector<vector<int>> G;
	vector<int> L, R, Viz;

	BipartiteMatcher(int n, int m) :
		G(n), L(n, -1), R(m, -1), Viz(n) {}

	void AddEdge(int a, int b) {
		G[a].push_back(b);
	}

	bool Match(int node) {
		if(Viz[node]) 
			return false;
		Viz[node] = true;
	
		for(auto vec : G[node]) {
			if(R[vec] == -1 || Match(R[vec])) {
				L[node] = vec;
				R[vec] = node;
				return true;
			}
		}

		return false;
	}
	void Solve() {
		bool ok = true;
		while(ok) {
			ok = false;
			fill(Viz.begin(), Viz.end(), 0);
			for(int i = 0; i < L.size(); ++i)
				if(L[i] == -1)
					ok |= Match(i);
		}
	}
};

int main() {
	int t;
	cin >> t;
	for(int tt = 1; tt <= t; ++tt) {
		int n, q;
		cin >> n >> q;

		int score = 0, cnt = 0;
		vector<bool> BusyR(n), BusyC(n), 
			BusyD1(2 * n), BusyD2(2 * n);
		vector<vector<bool>> Exists(n, vector<bool>(n, false));
		
		while(q--) {
			char c; int i, j;
			cin >> c >> i >> j;
			--i; --j;

			if(c != '+') ++score, BusyR[i] = BusyC[j] = 1;
			if(c != 'x') ++score, BusyD1[i + j] = BusyD2[i - j + n] = 1;
			Exists[i][j] = true;
		}

		BipartiteMatcher HM(n, n), DM(2 * n, 2 * n);
		for(int i = 0; i < n; ++i)
		for(int j = 0; j < n; ++j) {
			if(!BusyR[i] && !BusyC[j])
				HM.AddEdge(i, j);
			if(!BusyD1[i + j] && !BusyD2[i - j + n])
				DM.AddEdge(i + j, i - j + n);
		}

		HM.Solve();
		DM.Solve();


		for(int i = 0; i < n; ++i)
		for(int j = 0; j < n; ++j) {
			bool ok = false;
			if(HM.L[i] == j)
				ok = true, ++score;
			if(DM.L[i + j] == i - j + n)
				ok = true, ++score;
			cnt += ok;
		}

		cout << "Case #" << tt << ": " << score << " " << cnt << '\n';
		for(int i = 0; i < n; ++i)
		for(int j = 0; j < n; ++j) {
			bool ok1 = false, ok2 = false;
			if(HM.L[i] == j)
				ok1 = true;
			if(DM.L[i + j] == i - j + n)
				ok2 = true;

			if(Exists[i][j] && (ok1 || ok2)) cout << "o " << i+1 << " " << j+1 << '\n';
			else if( ok1 &&  ok2) cout << "o " << i+1 << " " << j+1 << '\n';
			else if( ok1 && !ok2) cout << "x " << i+1 << " " << j+1 << '\n';
			else if(!ok1 &&  ok2) cout << "+ " << i+1 << " " << j+1 << '\n';
		}

	}
	return 0;
}