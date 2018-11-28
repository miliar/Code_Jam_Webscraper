#include <bits/stdc++.h>

using namespace std;

#define MAXN 105
#define MAXP 5

int N, P;
int A[MAXN];
int f[MAXP];

int solve4() {
	int ret = f[0];

	ret += f[2] / 2;
	f[2] %= 2;

	int cnt = min(f[1], f[3]);
	ret += cnt;
	f[1] -= cnt;
	f[3] -= cnt;

	if (f[1] > 0) {
		assert(f[3] == 0);
		ret += f[1] / 4;
		f[1] %= 4;
		if (f[2] > 0 && f[1] >= 2) {
			f[2]--;
			f[1] -= 2;
			ret++;
		}
		if (f[2] > 0 || f[1] > 0) {
			ret++;
		}
	} else if (f[3] > 0) {
		assert(f[1] == 0);
		ret += f[3] / 4;
		f[3] %= 4;
		if (f[2] > 0 && f[3] >= 2) {
			f[2]--;
			f[3] -= 2;
			ret++;
		}
		if (f[2] > 0 || f[3] > 0) {
			ret++;
		}
	} else {
		if (f[2] > 0) {
			ret++;
		}
	}

	return ret;
}

int solve() {
	memset(f, 0, sizeof(f));
	for (int i = 0; i < N; i++) {
		int rem = A[i] % P;
		f[rem]++;
	}

	int ret = 0;
	if (P == 2) {
		ret += f[0];
		ret += (f[1] + 1) / 2;
	} else if (P == 3) {
		ret += f[0];
		int cnt = min(f[1], f[2]);
		ret += cnt;
		f[1] -= cnt;
		f[2] -= cnt;
		
		ret += f[1] / 3;
		f[1] %= 3;
		if (f[1] > 0) {
			ret++;
		}

		ret += f[2] / 3;
		f[2] %= 3;
		if (f[2] > 0) {
			ret++;
		}
	} else {
		ret = solve4();
	}

	return ret;
}

int main() {
	assert(freopen("A.in", "r", stdin));
	assert(freopen("A.out", "w", stdout));
	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		cin >> N >> P;
		for (int i = 0; i < N; i++) {
			cin >> A[i];
		}

		int ans = solve();
		cout << ans << endl;
		
		cerr << t << endl;
	}

	return 0;
}
