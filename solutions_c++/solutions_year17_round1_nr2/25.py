#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>

void solveOne(int iTest) {
	int nI, nP;
	scanf("%d %d", &nI, &nP);
	std::vector<int> perServing(nI); 
	for (int i = 0; i < nI; i++) {
		scanf("%d", &perServing[i]);
	}
	std::vector<std::vector<int>> q(nI, std::vector<int>(nP));
	for (int i = 0; i < nI; i++) {
		for (int j = 0; j < nP; j++) {
			scanf("%d", &q[i][j]);
		}
		std::sort(q[i].begin(), q[i].end());
	}
	int nKits = 0;
	for (int nServ = 1; nServ <= 2000000;) {
		bool good = true;
		bool empty = false;
		for (int i = 0; i < nI; i++) {
			while (true) {
				if (q[i].empty()) {
					good = false;
					empty = true;
					break;
				}
				if (q[i][0] < (1LL * nServ * perServing[i] * 9 + 9) / 10) {
					q[i].erase(q[i].begin());
					continue;
				}
				good = (q[i][0] <= (1LL * nServ * perServing[i] * 11) / 10);
				break;
			}
			if (!good || empty) {
				break;
			}
		}
		if (empty) {
			break;
		}
		if (good) {
			nKits++;
			for (int i = 0; i < nI; i++) {
				q[i].erase(q[i].begin());
			}
		} else {
			nServ++;
		}
	}
	printf("Case #%d: %d\n", iTest, nKits);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		solveOne(i);
	}
	return 0;
}
