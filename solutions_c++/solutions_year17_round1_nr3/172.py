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

struct state {
	int hd, ad, hk, ak;
};

int my_time = 0;
int t[N][N][N][N];
int ds[N][N][N][N];

void solve() {
	++my_time;
	int hd, ad, hk, ak, b, d;
	cin >> hd >> ad >> hk >> ak >> b >> d;
	queue<state> q;
	q.push({hd, ad, hk, ak});
	t[hd][ad][hk][ak] = my_time;
	ds[hd][ad][hk][ak] = 0;
	int start = hd;
	while (!q.empty()) {
		auto cur = q.front();
		q.pop();

		hd = cur.hd;
		ad = cur.ad;
		hk = cur.hk;
		ak = cur.ak;

		if (cur.hd <= 0) {
			continue;
		}
		if (cur.hk <= 0) {
			cout << ds[hd][ad][hk][ak] << '\n';
			return;
		}
		int nhd, nad, nhk, nak;

		// Attack
		nad = ad;
		nak = ak;
		nhk = max(0, hk - ad);
		nhd = !nhk ? hd : max(0, hd - ak);

		if (t[nhd][nad][nhk][nak] != my_time) {
			t[nhd][nad][nhk][nak] = my_time;
			ds[nhd][nad][nhk][nak] = ds[hd][ad][hk][ak] + 1;
			q.push({nhd, nad, nhk, nak});
		}

		// Buff
		nad = ad + b;
		nak = ak;
		nhk = hk;
		nhd = !nhk ? hd : max(0, hd - ak);

		if (t[nhd][nad][nhk][nak] != my_time) {
			t[nhd][nad][nhk][nak] = my_time;
			ds[nhd][nad][nhk][nak] = ds[hd][ad][hk][ak] + 1;
			q.push({nhd, nad, nhk, nak});
		}

		// Cure
		nad = ad;
		nak = ak;
		nhk = hk;
		nhd = !nhk ? start : max(0, start - ak);

		if (t[nhd][nad][nhk][nak] != my_time) {
			t[nhd][nad][nhk][nak] = my_time;
			ds[nhd][nad][nhk][nak] = ds[hd][ad][hk][ak] + 1;
			q.push({nhd, nad, nhk, nak});
		}

		// Debuff
		nad = ad;
		nak = max(0, ak - d);
		nhk = hk;
		nhd = !nhk ? hd : max(0, hd - nak);

		if (t[nhd][nad][nhk][nak] != my_time) {
			t[nhd][nad][nhk][nak] = my_time;
			ds[nhd][nad][nhk][nak] = ds[hd][ad][hk][ak] + 1;
			q.push({nhd, nad, nhk, nak});
		}


	}
	cout << "IMPOSSIBLE\n";
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);

	int t;
	cin >> t;
	REP(i, t) {
		cerr << i << endl;
		cout << "Case #" << i + 1 << ": ";
		solve();
	}

	return 0;
}