#include <bits\stdc++.h>

using namespace std;

#define N int(1e5+5)

inline void solve();

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
//#ifndef ONLINE_JUDGE 
//	freopen("A-small-attempt0.in", "rt", stdin);
//	freopen("output.txt", "wt", stdout);
//	int t;
//	cin >> t;
//	while (t--) {
//		clock_t time = clock();
//		solve();
//		printf("                    %f\n\n", (clock() - time) / (double)CLOCKS_PER_SEC);
//	}
//#endif 
//#ifdef ONLINE_JUDGE
	solve();
//#endif 
	return 0;
}

typedef long long ll;
#define int ll

void solve() {
	int t, n, d, k, s;
	cin >> t;
	for (int test = 1; test <= t; test++) {
		cin >> d >> n;
		double time = 0;
		for (int i = 0; i < n; i++) {
			cin >> k >> s;
			time = max(time, double(d - k) / s);
		}
		cout << "Case #" << test << ": " << setprecision(8) << fixed << d / time << endl;
	}

}