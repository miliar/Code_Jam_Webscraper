#include <bits/stdc++.h>
using namespace std;

long long t, n, k;

pair<long long, long long> solve(map<long long, long long> M, long long k) {
	map<long long, long long> N;
	while (!M.empty() && k > 0) {

		long long len = M.rbegin()->first, cnt = M.rbegin()->second;
		M.erase(len);

		long long L = (len - 1) / 2;
		long long R = (len - 1) / 2 + (len - 1) % 2;
		if (cnt >= k)
			return make_pair(R, L);
		k -= cnt;
		N[R] += cnt;
		N[L] += cnt;
	}
	return solve(N, k);
}

int main() {
	ios::sync_with_stdio(false);
	freopen("/home/ahmed/Desktop/few/C-large.in", "r", stdin);
	freopen("/home/ahmed/Desktop/few/C-large.out", "w", stdout);

	cin >> t; int id = 1;
	while (t--) {
		cin >> n >> k;
		map<long long, long long> M; M[n] = 1;
		pair<long long, long long> ans = solve(M, k);
		cout << "Case #" << id++ << ": "<< ans.first << " " << ans.second << endl;
	}


	return 0;
}
