#include <bits/stdc++.h>

using namespace std;

#define error(x) cout << #x << " = " << x << "\n"
#define sz(a) int(a.size())

typedef long long int64;
typedef pair<int64, int64> ii;

void solve(int64 N, int64 K) {
	vector<bool> occ(N+2, 0);
	occ[0] = occ[N+1] = 1;
	ii cur;

	for (int i = 0; i < K; i++) {
		int res = -1, max1 = -1, max2 = -1;
		for (int j = 0; j < N+2; j++) {
			if (occ[j]) continue;
			int Ls = -1, Rs = -1;
			for (int x = 1; j-x >= 0; x++)
				if (occ[j-x]) {
					Ls = x; break;
				}
			for (int x = 1; j+x <= N+1; x++)
				if (occ[j+x]) {
					Rs = x; break;
				}
			if (min(Ls, Rs) > max1 || (min(Ls, Rs) == max1 && max(Ls, Rs) > max2)) {
				res = j;
				max1 = min(Ls, Rs);
				max2 = max(Ls, Rs);
			}
		}
		cur = ii(max2, max1);
		occ[res] = 1;
		// cout << cur.first-1 << " " << cur.second-1 << "\n";
	}
	cout << cur.first-1 << " " << cur.second-1 << "\n";
}

ii nextState(ii cur) {
	ii res(cur.first/2, 0);
	if (cur.first-1-res.first != res.first) res.second = cur.first-1-res.first;
	else if (cur.second/2 != res.first) res.second = cur.second/2;
	else res.second = cur.second-1-cur.second/2;
	if (res.second > res.first) swap(res.first, res.second);
	return res;
}

void solveUlti(int64 N, int64 K) {
	ii cur(N/2, N-1-N/2);
	if (K == 1) {
		cout << cur.first << " " << cur.second << "\n";
		return;
	}
	int64 sum = N-1, sl = 2;
	K--;
	while (1) {
		// error(sum); error(sl); error(K);
		// cout << "---\n";
		if (K > sl) {
			K -= sl;
			sum -= sl;
			sl *= 2LL;
			cur = nextState(cur);
		}
		else {
			if (cur.first == cur.second) {
				cout << cur.first/2 << " " << cur.first-1-cur.first/2 << "\n";
				return; 
			}
			if (cur.first == 0) {
				cout << "0 0\n";
				return;
			}
			int64 x = sum - sl*cur.second;
			if (K <= x) {
				cout << cur.first/2 << " " << cur.first-1-cur.first/2 << "\n";
			}
			else {
				if (cur.second == 0)
					cout << "0 0\n";
				else
					cout << cur.second/2 << " " << cur.second-1-cur.second/2 << "\n";
			}
			return;
		}
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);
	int T; cin >> T;
	for (int te = 1; te <= T; te++) {
		int64 N, K; cin >> N >> K;
		cout << "Case #" << te << ": ";
		if (N <= 0) solve(N, K);
		else solveUlti(N, K);
	}

	return 0;
}