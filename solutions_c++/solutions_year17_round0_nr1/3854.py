#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
using namespace std;

int T, C=1, S, K;
string P;

bool flip(int i) {
	if (i < K-1) {
		return false;
	}
	for (int j = i-(K-1); j <= i; j++) {
		if (P[j] == '+') {
			P[j] = '-';
		} else {
			P[j] = '+';
		}
	}
	return true;
}

int main2() {
	int nflips = 0;
	for (int i = S - 1; i >= 0; i--) {
		if (P[i] == '-') {
			if (!flip(i)) {
				return -1;
			}
			nflips++;
		}
	}
	return nflips;
}

int main(void) {
	scanf("%d", &T);
	while (T--) {
		cin >> P >> K;
		S = P.size();
		int res = main2();
		if (res == -1) {
			printf("Case #%d: IMPOSSIBLE\n", C++);
		} else {
			printf("Case #%d: %d\n", C++, res);
		}
	}
	return 0;
}