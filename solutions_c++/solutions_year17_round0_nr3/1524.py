#include <bits/stdc++.h>

using namespace std;

priority_queue<int> S;

pair<int, int> solve(int n, int k) {
	while (!S.empty()) {
		S.pop();
	}
	S.push(n);
	
	int a, b;
	while (k-- > 0) {
		int len = S.top();
		S.pop();

		a = len / 2;
		b = (len - 1) / 2;
		S.push(a);
		S.push(b);
	}

	return { a, b };
}

map<long long, long long> L;
pair<long long, long long> solveLarge(long long n, long long k) {
	L.clear();
	L[n] = 1;

	long long a, b;
	while (k > 0) {
		long long len = L.rbegin()->first;
		long long cnt = L.rbegin()->second;
		L.erase(len);

		a = len / 2;
		b = (len - 1) / 2;
		L[a] += cnt;
		L[b] += cnt;

		k -= cnt;
	}

	return { a, b };
}

int main() {
	assert(freopen("C.in", "r", stdin));
	assert(freopen("C.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		long long N, K;
		cin >> N >> K;
		auto ans = solveLarge(N, K);
		cout << ans.first << ' ' << ans.second << endl;
		
		cerr << t << endl;
	}

	return 0;
}
