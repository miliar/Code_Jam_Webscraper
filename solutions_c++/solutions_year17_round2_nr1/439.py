#include <bits/stdc++.h>

using namespace std;

#define REP(i, N) for (int (i) = 0; (i) < (N); ++(i))
#define READALL(c) for (auto &e : c) { cin >> e; }
#define PRINTALL(c) for (const auto &e : c) { cout << e << "\t"; } cout << "\n";

template <typename T>
using V = vector<T>;

int64_t D, N;
vector<int64_t> K, S;

typedef long double ld;

ld same_time(int64_t speed, int i) {
	return K[i]+S[i]/ld(speed);
}

void solve() {
	cin >> D >> N;
	K.resize(N);
	S = K;
	REP(i, N) {
		cin >> K[i] >> S[i];
	}
	ld ans = 0;
	ld lo = 0, hi = 1e20;
	for (int it = 0; it < 300; ++it) {
		ld mid = (lo+hi)/2;
		ld time_to_fin = D/mid;
		bool g = 1;
		REP(i, N) {
			ld t = (D-K[i])/ld(S[i]);//same_time(speed, i);
			if (t > time_to_fin) {
				g = 0;
				break;
			}
		}
		if (g) {
			lo = mid;
		} else {
			hi = mid;
		}
	}
	// for (ld speed = 1; speed < 150; speed += 0.1) {
	// 	ld time_to_fin = D/speed;
	// 	bool g = 1;
	// 	REP(i, N) {
	// 		ld t = (D-K[i])/ld(S[i]);//same_time(speed, i);
	// 		// cout << i << " " << speed << " " << t << " " << time_to_fin << endl;
	// 		if (t > time_to_fin) {
	// 			g = 0;
	// 			break;
	// 		}
	// 	}
	// 	if (g) {
	// 		ans = max(ans, speed);
	// 	}
		
	// }
	cout << fixed << setprecision(20);
	cout << lo << endl;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	int T;
	cin >> T;

	REP(tc, T) {
		cout << "Case #" << (tc+1) << ": ";
		solve();
	}
}