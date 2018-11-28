#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 100;
const int MAX_P = 100;

int N, P;
int R[MAX_N];
int Q[MAX_N][MAX_P];

int iter[MAX_N];

int ans;

void solve() {
	for (int s = 1; s <= 1000000; s++) {
		//cout << s << endl;
		// walk iters
		bool ok = true;
		for (int i = 0; i < N; i++) {
			bool ok1 = false;
			while (1) {
				//if (s % 1000 == 0) cout << s << " " << i << " " << iter[i] << endl;
				if (iter[i] == P) {
					break;
				}
				
				int j = iter[i];
				int t0 = (10*Q[i][j] + 11*R[i] - 1) / (11*R[i]);
				int t1 = (10*Q[i][j]) / (9*R[i]);
				if (s < t0) {
					break;
				}
				if (t0 <= s && s <= t1) {
					ok1 = true;
					break;
				}
				iter[i]++;
			}
			if (!ok1) {
				ok = false;
			}
		}
		if (ok) {
			ans++;
			s--;
			for (int i = 0; i < N; i++) {
				iter[i]++;
			}
			
			
		}
	}
}

bool dfs(int ingr, int s0, int s1) {
	cout << "ingr, s0, s1: " << ingr << " " << s0 << " " << s1 << endl;
	
	//assert(s0 <= s1);
	//if (s1 < s0) {
		//return false;
	//}
	if (ingr == N) {
		ans++;
		return true;
	}
	
	for (int j = iter[ingr]; j < P; j++) {
		//int t0 = (90*Q[ingr][j] + 100*R[ingr] - 1) / (100*R[ingr]);
		//int t1 = (110*Q[ingr][j]) / (100*R[ingr]);
		
		int t0 = (10*Q[ingr][j] + 11*R[ingr] - 1) / (11*R[ingr]);
		int t1 = (10*Q[ingr][j]) / (9*R[ingr]);
		
		if (t0 > s1) {
			return false;
		}
		iter[ingr]++;
		
		if (t1 < s0) {
			//iter[ingr]++;
			continue;
		}
		
		//cout << "    j, t0, t1: " << j << " " << t0 << " " << t1 << endl;
		dfs(ingr+1, max(t0, s0), min(t1, s1));
		
		//if (!dfs(ingr+1, max(t0, s0), min(t1, s1))) {
			//if (ingr > 0) {
				//return false;
			//}
		//}
	}
	return true;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N >> P;
		for (int i = 0; i < N; i++) {
			cin >> R[i];
		}
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < P; j++) {
				cin >> Q[i][j];
			}
			sort(Q[i], Q[i] + P);
		}
		
		cout << "Case #" << icase << ": ";
		
		memset(iter, 0, sizeof iter);
		ans = 0;
		//int inf = 10000000;
		//dfs(0, 1, inf);
		
		solve();
		cout << ans << endl;
	}
	return 0;
}
