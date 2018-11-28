#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int D, N; cin >> D >> N;
		ld lastTime = 0;
		for (int i = 0; i < N; i++) {
			int K, S; cin >> K >> S;
			ld time = (D - K) / (ld) S;
			if (time > lastTime)
				lastTime = time;
		}
		cout << "Case #" << t << ": " << fixed << setprecision(10) << D / lastTime << endl;
	}
	return 0;
}