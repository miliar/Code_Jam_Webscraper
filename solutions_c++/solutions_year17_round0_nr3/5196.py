
//Karol Kaszuba

#include <bits/stdc++.h>

using namespace std;
#define int long long

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef double D;
typedef long double LD;
typedef vector<PII> VII;
typedef unordered_set<int> USI;
typedef unordered_set<LL> USLL;

#define FOR(i,x,y) for(auto i=(x);i<=(y);++i)
#define REP(i,x) FOR(i,0,(x)-1)
#define FORD(i,x,y) for(auto i=(x);i>=(y);--i)
#define VAR(i,c) __typeof(c) i=(c)
#define FORE(i,c) for(VAR(i,(c).begin());i!=(c).end();++i)
#define SIZE(c) (int)((c).size())
#define ALL(c) (c).begin(),(c).end()
#define PB push_back
#define EB emplace_back
#define IN insert
#define ER erase
#define MP make_pair
#define ST first
#define ND second
#define IOSYNC ios_base::sync_with_stdio(0)
#define FREOPEN(f) freopen(f, "r", stdin),freopen(f, "w", stdout)

/*
PII jebaj_easy(int n, int k) {
	
}
*/

PII jebaj(int n, int k) {
	
	if (k == 1) {
		return {n / 2, (n - 1) / 2};
	}
	if (n % 2 == 1) {
		return jebaj((n - 1) / 2, k / 2);
	} else {
		k--;
		if (k % 2 == 1) {
			return jebaj(n / 2, (k + 1) / 2);
		} else {
			return jebaj(n / 2 - 1, k / 2);
		}
	}

}

PII solve() {
	int n, k;
	cin >> n >> k;
	return jebaj(n, k);
}

#undef int
int main() {
#define int long long
	IOSYNC;
	int t;
	cin >> t;
	FOR(i, 1, t) {
		auto x = solve();
		cout << "Case #" << i << ": " << x.ST << " " << x.ND << "\n";
	}
	return 0;
}
