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


int main() {
	ios_base::sync_with_stdio(false);
	
	int T;
	cin >> T;
	FOR(cas, 1, T) {
		cout << "Case #" << cas << ": ";
		string in;
		int k;
		cin >> in >> k;
		int n = SIZE(in);
		vector<bool> pancake(n);
		REP(i, n) pancake[i] = in[i] == '+';
		bool ok = true;
		int res = 0;
		REP(i, n) {
			if (!pancake[i]) {
				if (i + k > n) {
					ok = false;
				} else {
					res++;
					FOR(j, i, i + k - 1) pancake[j] = !pancake[j];
				}
			}
		}
		if (ok) {
			cout << res << endl;
		} else {
			cout << "IMPOSSIBLE\n";
		}
	}	

	return 0;
}
