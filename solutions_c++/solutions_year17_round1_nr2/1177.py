#include <bits/stdc++.h>
using namespace std;


int N, P;
int R[64], Q[64][64];
int p[64];


int gao(int q, int r, int &ll, int &rr) {
	ll = (q / 1.1 / r) + 10;
	rr = (q / 0.9 / r) - 10;
	float eps = 1e-4;
	while (ll * r * 1.1 > q + eps) ll -= 1;
	if (ll * r * 1.1 + eps < q) ll += 1;
	while (rr * r * 0.9 + eps < q) rr += 1;
	if (rr * r * 0.9 > q + eps) rr -= 1;
}

int solve() {
	cin >> N >> P;
	for (int i = 0; i < N; i++)
		cin >> R[i];
	for (int i = 0; i < N; i++)
		for (int j = 0; j < P; j++)
			cin >> Q[i][j];
	for (int i = 0; i < P; i++)
		p[i] = i;
	int ans = 0;
	if (N == 1) {
		for (int i = 0; i < P; i++) {
			int l1, r1;
			gao(Q[0][i], R[0], l1, r1);
			//cout << l1 << ' ' << r1 << endl;
			if (l1 <= r1)
				ans += 1;
		}
		return ans;
	}
    do {
		int sum = 0;
		for (int i = 0; i < P; i++) {
			int l1, r1, l2, r2;
			gao(Q[0][i], R[0], l1, r1);
			gao(Q[1][p[i]], R[1], l2, r2);
			//cout << l1 << ' ' << r1 << endl;
			//cout << l2 << ' ' << r2 << endl;
			if (l1 > r1 || l2 > r2) continue;
			if (r2 < l1 || r1 < l2) continue;
			sum += 1;
		}
		ans = max(ans, sum);
	}while (next_permutation(p, p + P));
	return ans;
}

int main() {
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cout << "Case #" << i << ": ";
		cout << solve() << endl;
	}
	return 0;
}

