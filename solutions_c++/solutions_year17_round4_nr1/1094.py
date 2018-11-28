#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mk make_pair
#define fi first
#define se second

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);

const int N = 101;
int ct[5];
int dp[N][N][N][4];
int n, p;

int go (int a, int b, int c, int old) {
	if (!a and !b and !c)	return 0;

	int &r = dp[a][b][c][old];
	if (r != -1)
		return r;

	int A = 0, B = 0, C = 0;


	if (a) {
		A = go (a - 1, b, c, (old + 1)%p);
	}
	if (b) {
		B = go (a, b - 1, c, (old + 2)%p);
	}
	if (c) {
		C = go (a, b, c - 1, (old + 3)%p);
	}

	if (!old) {
		A ++;
		B ++;
		C ++;
	}

	return r = max (A, max (B, C));
}

int main (void) {
	ios_base::sync_with_stdio(false);

	int T;	cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> n >> p;
		memset (ct, 0, sizeof ct);
		memset (dp, -1, sizeof dp);
		for (int i = 0; i < n; i++) {
			int g;	cin >> g;
			ct[g%p]++;
		}

		cout << "Case #" << t << ": ";
		cout << go(ct[1], ct[2], ct[3], 0) + ct[0] << endl;
	}

	return 0;
}
