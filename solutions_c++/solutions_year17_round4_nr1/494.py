#include <bits/stdc++.h>
using namespace std;

void code() {
	int N, P;
	cin >> N >> P;

	int total = 0;
	vector<int> G(N);
	vector<int> S(P, 0);
	for(int i = 0; i < N; i++) {
		cin >> G[i];
		S[G[i] % P]++;
	}
	total += S[0];
	if (P == 2) {
		total += (S[1]+1) / 2;
	} else if (P == 3) {
		int nm = min(S[1], S[2]);
		total += nm;
		S[1] -= nm;
		S[2] -= nm;
		total += (S[1]+2) / 3;
		total += (S[2]+2) / 3;
	} else {
		int nm = min(S[1], S[3]);
		total += nm;
		S[1] -= nm;
		S[3] -= nm;

		int nm2 = S[2] / 2;
		total += nm2;
		S[2] -= nm2 * 2;

		if (S[2]) {
			if (S[1] >= 2) {
				S[2]--;
				S[1] -= 2;
				total++;
			}
			if (S[3] >= 2) {
				S[2]--;
				S[3] -= 2;
				total++;
			}
		}


		int nm3 = S[1] / 4;
		total += nm3;
		S[1] -= nm3 * 4;
		int nm4 = S[3] / 4;
		total += nm4;
		S[3] -= nm4 * 4;

		if (S[1] || S[2] || S[3]) total++;
	}

	printf("%d", total);
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		code();
		printf("\n");
	}
}
