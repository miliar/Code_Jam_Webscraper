#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) for(int i=0; i<int(n); ++i)
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
typedef long long ll;


int TC;

int R, C;
string A[100];
void solve() {
	int N, P;
	cin >> N >> P;
	vector<int> G(N);
	vector<int> C(100);
	rep(i, N) {
		cin >> G[i];
		G[i] %= P;
		C[G[i]] += 1;
	}

	int g = C[0];
	int rem = N - C[0];
	if (P == 2) {
		g += C[1] / 2;
		rem -= C[1] / 2 * 2;
	} else if (P == 3) {
		int p = min(C[1], C[2]);
		int a = max(C[1], C[2]) - p;
		g += p + a / 3;
		rem -= p * 2 + a / 3 * 3;
	} else if (P == 4) {
		int p = min(C[1], C[3]);
		int a = (max(C[1], C[3]) - p);
		g += p;
		rem -= p * 2;
		int q = C[2] / 2;
		g += q;
		rem -= q * 2;
		
		if (C[2] % 2 == 0) {
			g += a / 4;
			rem -= a / 4 * 4;
		} else {
			a += 2;
			g += a / 4;
			rem = a % 4 != 0;
		}
	} else assert(false);
	int res = g + (rem > 0 ? 1 : 0);
	cout << res << endl;
}
int main() {
	int T; cin >> T;
	for(TC=1; TC<=T; TC++) {
		cout << "Case #" << TC << ": ";
		solve();
	}
}

