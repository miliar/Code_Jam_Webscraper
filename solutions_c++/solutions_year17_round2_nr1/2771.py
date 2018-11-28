#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int cases; cin >> cases;
	for (int cc = 0; cc < cases; ++cc) {
		cout << "Case #" << cc + 1 << ":";

		long double D; cin >> D;
		int N; cin >> N;

		long double V;
		bool first = true;

		for (int i = 0; i < N; ++i) {
		  long double K, S; cin >> K >> S;
		  long double curV = D * S / (D - K); // don't worry about / 0, K < D

		  if (first || curV < V)
		    first = false, V = curV;
		}

		cout << fixed << setprecision(15) << " " << V << "\n";
	}
	return 0;
}
