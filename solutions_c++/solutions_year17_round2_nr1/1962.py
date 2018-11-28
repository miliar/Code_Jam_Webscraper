#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

void solve() {
	double d;
	int n;
	cin >> d >> n;

	double maxt = 0;
	for (int i = 0; i < n; i++) {
		double k, s;
		cin >> k >> s;
		maxt = max(maxt, (d - k) / s);
	}

	printf("%0.7lf", d / maxt);
}

int main() {
	int test;
	cin >> test;
	for (int t = 1; t <= test; t++) {
		printf("Case #%d: ", t);
		// cout << "Case #" << t << ": ";
		solve();
		// cout << endl;
		printf("\n");
	}
}
