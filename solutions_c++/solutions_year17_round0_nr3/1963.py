#include <iostream>
#include <map>

using namespace std;

map<pair<int64_t, int64_t>, pair<int64_t, int64_t> > mem;

pair<int64_t, int64_t> solve(int64_t N, int64_t K) {
	if (K == 0) return { 1ULL << 60, 1ULL << 60 };
	if (K == 1) return { (N - 1) / 2 + (N - 1) % 2, (N - 1) / 2 };

	if (mem.find({ N, K }) == mem.end()) {
		N--, K--;
		pair<int64_t, int64_t> l = solve(N / 2 + N % 2, K / 2 + K % 2),
					  		   r = solve(N / 2, K / 2);	
		N++, K++;
		mem[{N, K}] = { min(l.first, r.first), min(l.second, r.second) };
	}

	return mem[{ N, K }];
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		int64_t N, K;
		cin >> N >> K;
		pair<int64_t, int64_t> ans = solve(N, K);

		cout << "Case #" << t << ": " << ans.first << " " << ans.second << endl;
	}

	return 0;
}