#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <vector>
#include <list>
#include <set>
#include <map>

using namespace std;

int main(int argc, char *argv) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		int N, K;
		scanf("%d %d", &N, &K);

		vector<int> S(N + 1, 0);
		S[N] = 1;
		int s = N;
		int k = 0;
		for (int k = 0; k < K; k += S[s], s--) {
			int ls = (s - 1) - (s - 1) / 2;
			int rs = (s - 1) / 2;

			S[ls] += S[s];
			S[rs] += S[s];
		}

		s += 1;

		int ls = (s - 1) - (s - 1) / 2;
		int rs = (s - 1) / 2;
		printf("Case %d: %d %d\n", t + 1, ls, rs);
	}
}