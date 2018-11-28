#include <bits/stdc++.h>
#include <iomanip>
using namespace std;

int main() {

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		double D = 0, N = 0, K[1010] = { 0 }, Ans = 0, S[1010] = { 0 };
		cin >> D >> N;
		for (int i = 0; i < N; i++)
			cin >> K[i] >> S[i];

		for (int i = 0; i < N; i++)
			Ans = max(Ans, (D - K[i]) / S[i]);

		cout << "Case #" << t + 1 << ": ";
		Ans = D / Ans;
		cout << fixed;
		cout << setprecision(6);
		cout << Ans;
		cout << endl;
	}
}
