#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int solve(int y, vector<int> P1, vector<int> P2) {
	int N = 1;
	if (!P1.empty() && P1.back() >= N) N = P1.back();
	if (!P2.empty() && P2.back() >= N) N = P2.back();
	vector<int> T(N, 0);
	for (auto& p : P1) T[p-1] ++;
	for (auto& p : P2) T[p-1] ++;
	int ret = 0;
	for (int i = N - 1; i >= 0; --i) {
		while (T[i] > y) {
			for (int j = i - 1; ; --j) {
				if (j < 0) 
					return -1;
				if (T[j] < y) {
					T[j] ++;
					T[i] --;
					ret++;
					++j;
					if (T[i] == y) break;
				}
			}
		}
	}
	return ret;
}

int main() {
	int T;
	cin >> T;
	for (int q = 1; q <= T; ++q) {
		int N, C, M;
		cin >> N >> C >> M;
		vector<int> P(M), B(M);
		vector<int> P1, P2;
		for (int i = 0; i < M; ++i) {
			cin >> P[i] >> B[i];
			if (B[i] == 1) P1.push_back(P[i]);
			else P2.push_back(P[i]);
		}
		
		sort(P1.begin(), P1.end());
		sort(P2.begin(), P2.end());
		int y = 0, z = 0;
		y = max(P1.size(), P2.size());
		while ((z = solve(y, P1, P2)) == -1) ++y;

		cout << "Case #" << q << ": " << y << " " << z << endl;
	}
	return 0;
}