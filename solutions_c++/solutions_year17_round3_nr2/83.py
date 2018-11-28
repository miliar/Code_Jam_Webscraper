#include <bits/stdc++.h>

using namespace std;

#define endl '\n'

typedef long long int64;
typedef pair<int,int> pii;
typedef vector<int> vi;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;
const int maxn = 100000 + 10;
const double pi = acos(-1);

int T[ 1440 ];
int DP[ 1440 ][ 721 ][2];

void solve(){
	int c, j;
	cin >> c >> j;

	// cout << endl;
	// cout << c << " " << j << endl;

	memset(T, 0, sizeof T);

	for (int i = 0; i < c; ++i){
		int a, b; cin >> a >> b;
		// cout << a << " " << b << endl;
		for (int d = a; d < b; ++d)
			T[d] = 1;
	}

	for (int i = 0; i < j; ++i){
		int a, b; cin >> a >> b;
		// cout << a << " " << b << endl;
		for (int d = a; d < b; ++d)
			T[d] = 2;
	}

	int answer = oo;

	if ( T[0] != 1 ){
		memset(DP, oo, sizeof DP);
		DP[0][1][0] = 0;

		for (int i = 1; i < 1440; ++i){
			bool cameron = T[ i ] != 1;
			bool jamie = T[ i ] != 2;
			for (int k = 1; k <= 720; ++k){
				if (cameron) DP[i][k][0] = min( DP[i - 1][k - 1][0], DP[i - 1][k - 1][1] + 1 );
				if (jamie)   DP[i][k][1] = min( DP[i - 1][k][1], DP[i - 1][k][0] + 1 );
			}
		}

		int cur = min(DP[1440 - 1][720][0], DP[1440 - 1][720][1] + 1);
		answer = min(cur, answer);
	}

	if (T[0] != 2){
		memset(DP, oo, sizeof DP);
		DP[0][0][1] = 0;

		for (int i = 1; i < 1440; ++i){
			bool cameron = T[i] != 1;
			bool jamie = T[i] != 2;

			for (int k = 0; k <= 720; ++k){
				if (cameron && k) DP[i][k][0] = min(DP[i - 1][k - 1][0], DP[i - 1][k - 1][1] + 1 );
				if (jamie)   DP[i][k][1] = min( DP[i - 1][k][1], (DP[i - 1][k][0] + 1) );
			}
		}

		int cur = min( DP[1440 - 1][720][1], DP[1440 - 1][720][0] + 1);
		answer = min(cur, answer);
	}
	cout << answer << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

#ifdef MARX
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
#endif

	int t; cin >> t;

	int tc = 1;

	while (t--){
		cout << "Case #" << tc++ << ": ";
		solve();
	}

	return 0;
}