#include <iostream>
#include <set>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int q = 1; q <= T; ++q) {
		long long N, K;
		cin >> N >> K;
		multiset<long long> S;
		S.insert(N);
		long long v = 0;
		for (int i = 0; i < K; ++i) {
			auto it = S.end();
			--it;
			v = *it;
			--v;
			S.erase(it);
			S.insert(v / 2);
			S.insert(v - v / 2);
		}
		cout << "Case #" << q << ": " << (v - v / 2) << " " << (v / 2) << endl;
	}
	return 0;
}