#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <utility>
#include <cstring>
using namespace std;

int t;

int main()
{
	scanf("%d", &t);
	for (int ti = 0; ti < t; ++ti) {
		int N, P;
		scanf("%d%d", &N, &P);
		vector<int> R(N);
		for (int i = 0; i < N; ++i) {
			scanf("%d", &R[i]);
		}
		vector<vector<int>> Q(N, vector<int>(P));
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < P; ++j) {
				scanf("%d", &Q[i][j]);
			}
			sort(Q[i].begin(), Q[i].end());
		}
		int count = 0;
		while (true) {
			bool flag = false;
			vector<int> W(N);
			for (int i = 0; i < N; ++i) {
				if (Q[i].empty()) {
					flag = true;
					break;
				}
				W[i] = Q[i].back();
			}
			if (flag) {
				break;
			}
			vector<int> A(N), B(N);
			for (int i = 0; i < N; ++i) {
				A[i] = (10 * W[i] + 11 * R[i] - 1) / (11 * R[i]);
				B[i] = (10 * W[i]) / (9 * R[i]);
			}
			auto ita = max_element(A.begin(), A.end());
			auto itb = min_element(B.begin(), B.end());
			if (*ita <= *itb) {
				++count;
				for (int i = 0; i < N; ++i) {
					Q[i].pop_back();
				}
				continue;
			} else {
				Q[ita - A.begin()].pop_back();
			}
		}
		printf("Case #%d: %d\n", ti+1, count);
	}
	return 0;
}

/* vim: set ts=4 sw=4 noet: */
