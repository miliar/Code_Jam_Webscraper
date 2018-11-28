#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cassert>

using namespace std;

int main() {
	int nTests;
	cin >> nTests;
	for (int test = 1; test <= nTests; ++test) {
		int N, P;
		cin >> N >> P;
		vector<int> A(N);
		for (int i = 0; i < N; ++i) {
			cin >> A[i];
		}
		vector<vector<pair<int, int> > > T(N);
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j) {
				int tmp;
				cin >> tmp;
				pair<int, int> p(ceil(tmp/(1.1 * A[i])), floor(tmp/(0.9 * A[i])));
				if (p.first <= p.second) {
					T[i].push_back(p);
				} else {
					//assert(false);
					//cout << "failed at "<< i << " " << j << endl;
				}
			}
			sort(T[i].begin(), T[i].end());
			//cout << "printing T[" << i << "] :";
			//for (int j = 0; j < T[i].size(); ++j) {
				//cout << "(" << T[i][j].first << ", " << T[i][j].second << ") ";
			//}
			//cout << endl;
		}
		int ans = 0;
		vector<int> pos(N, 0);
		while (true) {
			bool done = false;
			for (int i = 0; i < N; ++i) {
				if (pos[i] == T[i].size()) {
					done = true;
				}
			}
			if (done) {
				break;
			}
			int min_R = T[0][pos[0]].second;
			int max_L = T[0][pos[0]].first;
			for (int i = 1; i < N; ++i) {
				min_R = min(min_R, T[i][pos[i]].second);
				max_L = max(max_L, T[i][pos[i]].first);
			}
			if (min_R >= max_L) {
				++ans;
				for (int i = 0; i < N; ++i) {
					++pos[i];
				}
			} else {
				for (int i = 0; i < N; ++i) {
					if (T[i][pos[i]].second < max_L) {
						++pos[i];
					}
				}
			}
			/*int min_L = T[0][pos[0]].first;
			int max_L = T[0][pos[0]].first;
			for (int i = 1; i < N; ++i) {
				min_L = min(min_L, T[i][pos[i]].first);
				max_L = max(max_L, T[i][pos[i]].first);
			}
			if (min_L == max_L) {
				++ans;
				for (int i = 0; i < N; ++i) {
					++pos[i];
				}
			} else {
				for (int i = 0; i < N; ++i) {
					if (max_L > T[i][pos[i]].second) {
						++pos[i];
					} else {
						T[i][pos[i]].first = max_L;
					}
				}
			}*/
		}
		cout << "Case #" << test << ": " << ans << endl;
		//return 0;
	}
	return 0;
}
