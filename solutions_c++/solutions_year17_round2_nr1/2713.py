#include <bits/stdc++.h>
#define ull unsigned long long
#define PB push_back
#define MOD 1000000007
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		int D; int N; cin >> D >> N;
		int * K = new int[N];
		int * S = new int[N];
		double mx = -1;
		for (int j = 0; j < N; j++) {
			cin >> K[j] >> S[j];
			mx = max(mx, ((double) (D - K[j]) / S[j]));
		}

		double ans = ((double)D) / mx;

		cout << "Case #" << (i+1) << ": " << fixed << setprecision(6) << ans << "\n"; 
		delete [] K;
		delete [] S;
	}
	return 0;
}
