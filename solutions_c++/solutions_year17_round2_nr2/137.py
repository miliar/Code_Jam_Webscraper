#include <bits/stdc++.h>

using namespace std;

const string imp = "IMPOSSIBLE";

char col[] = "ROYGBV";

int cnt[6];

void main2() {
	memset(cnt, 0, sizeof cnt);
	int n;
	cin >> n;
	cin >> cnt[0] >> cnt[1] >> cnt[2] >> cnt[3] >> cnt[4] >> cnt[5];
	for (int i = 0; i < 6; i+=2) if (cnt[i] <= cnt[(i+3)%6] && cnt[(i+3)%6] > 0) {
		if (cnt[i] == cnt[(i+3)%6] && cnt[i] + cnt[(i+3)%6] == n) {
			for (int j = 0; j < n/2; j++)
				cout << col[i] << col[(i+3)%6];
			cout << endl;
			return;
		}
		cout << imp << endl;
		return;
	}
	for (int i = 0; i < 6; i+=2)
		cnt[i] -= cnt[(i+3)%6];
	if (max(cnt[0], max(cnt[2], cnt[4])) * 2 > cnt[0] + cnt[2] + cnt[4]) {
		cout << imp << endl;
		return;
	}
	int max_c = 0;
	if (cnt[2] > cnt[max_c]) max_c = 2;
	if (cnt[4] > cnt[max_c]) max_c = 4;
	int N = cnt[0] + cnt[2] + cnt[4];
	vector<int>q(N, -1);
	int pnt = 0;
	for (int i = 0; i < 6; i += 2) {
		int j = (max_c + i) % 6;
		while (cnt[j] > 0) {
			if (q[pnt] != -1)
				pnt = (pnt + 1) % N;
			q[pnt] = j;
			cnt[j]--;
			pnt = (pnt + 2) % N;
		}
	}
	for (int i = 0; i < (int)q.size(); i++) {
		assert(q[i] != -1);
		assert(q[i] != q[(i+1)%N]);
		cout << col[q[i]];
		int opp = (q[i]+3)%6;
		while (cnt[opp] > 0) {
			cout << col[opp] << col[q[i]];
			cnt[opp]--;
		}
	}
	cout << endl;
}

int main() {
	int t; cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
