#include <bits/stdc++.h>
using namespace std;

int N; // # seats
int C; // # customers
int M; // # tickets

int total[3];
int cnt[3][1005];

int best1; // min # rides
int best2; // min # promos to achieve ans1

void solve() {
	best1 = max(total[1], total[2]);
	best2 = 0;
	for (int j = 1; j <= N; j++) {
		
		//
		int a = cnt[1][j]; // # 1's p1 has
		int b = total[1] - a; // # non-1's
		int c = cnt[2][j];
		int d = total[2] - c;
		
		//cout << "j= " << j << endl;
		//cout << a << " " << b << " " << c << " " << d << endl;
		
		int rem1 = max(0, a-d);
		int rem2 = max(0, c-b);
		
		if (rem1 > 0 && rem2 > 0) {
			// we've got a bastard
			if (j == 1) {
				best1 = a+c;
				best2 = 0;
			} else {
				best1 = d+b + max(rem1, rem2);
				best2 = min(rem1, rem2);
			}
		}
	}
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N >> C >> M;
		
		total[1] = 0;
		total[2] = 0;
		for (int i = 1; i <= N; i++) {
			cnt[1][i] = 0;
			cnt[2][i] = 0;
		}
	
		for (int i = 0; i < M; i++) {
			int p, b;
			cin >> p >> b;
			if (C == 2) {
				cnt[b][p]++;
				total[b]++;
			}
		}
		
		if (C > 2) {
			cout << "Case #" << icase << ": skipping, C = " << C << endl;
			continue;
		}
		assert(C == 2);
		
		solve();
		
		cout << "Case #" << icase << ": " << best1 << " " << best2 << endl;
	}
	return 0;
}
