#include <bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	ios_base::sync_with_stdio(0);

	int dest, num, pos, spd;
	double maxtime;

	int T;
	cin >> T;
	for (int tt = 1; tt <= T; tt++) {
		maxtime = 0;
		cin >> dest >> num;
		for (int i = 0; i < num; i++) {
			cin >> pos >> spd;
			maxtime = max(maxtime, (double)(dest-pos)/spd);
			//cerr << "mt: " << maxtime << endl;
		}
		cout << fixed << setprecision(10);
		cout << "Case #" << tt << ": " << dest/maxtime << endl;
	}

	return 0;
}
