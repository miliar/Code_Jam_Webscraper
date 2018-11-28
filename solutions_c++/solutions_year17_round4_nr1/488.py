#include <bits/stdc++.h>

#define FOR(i,b,e) for(int i=(b); i <= (e); ++i)
#define FORD(i,b,e) for(int i=(b); i >= (e); --i)
#define REP(i,n) for(int i=0; i < (n); ++i)
#define SIZE(c) (int) (c).size()
#define ALL(c) (c).begin(), (c).end()
#define PB push_back
#define MP make_pair
#define ST first
#define ND second
#define FWD(i,a,b) for (int i=(a); i<(b); ++i)
#define BCK(i,a,b) for (int i=(a); i>(b); --i)
#define PI 3.14159265358979311600
#define pb push_back
#define mp make_pair
#define st first
#define nd second

using namespace std;

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

typedef vector < int > VI;
typedef vector<ll> VL;

typedef long double K;

const int N = 105;

int f[5][N][N][N][4];

void precalc() {
	for (int p = 2; p <= 4; ++p) {
		REP(x, N) REP(y, N) REP(z, N) REP(left, p) {
			f[p][x][y][z][left] = N;
			if (!x && !y && !z) {
				f[p][x][y][z][left] = 0;
				continue;
			}
			int cost = (left > 0);
			if (x > 0) f[p][x][y][z][left] = min(f[p][x][y][z][left], f[p][x - 1][y][z][(p - (1 - left + p) % p) % p] + cost);
			if (y > 0) f[p][x][y][z][left] = min(f[p][x][y][z][left], f[p][x][y - 1][z][(p - (2 - left + p) % p) % p] + cost);
			if (z > 0) f[p][x][y][z][left] = min(f[p][x][y][z][left], f[p][x][y][z - 1][(p - (3 - left + p) % p) % p] + cost);
		}
	}
}

void solve() {
	int n, p;
	cin >> n >> p;
	int result = 0, cnt = 0;
	int c[] = {0, 0, 0};
	REP(i, n) {
		int x;
		cin >> x;
		if (x % p == 0) {
			++result;
		} else {
			++cnt;
			++c[x % p - 1];
		}
	}
	cout << result + cnt - f[p][c[0]][c[1]][c[2]][0] << '\n';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	precalc();

	int t;
	cin >> t;
	REP(i, t) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}