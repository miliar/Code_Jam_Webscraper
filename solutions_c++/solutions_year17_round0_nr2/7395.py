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

bool isSpecial(const string& s) {
	for (char c : s) {
		if (c == '0') {
			return true;
		}
		if (c != '1') {
			return false;
		}
	}
	return false;
}


int main() {
	ios_base::sync_with_stdio(false);
	
	int T;
	cin >> T;
	FOR(cas, 1, T) {
		cout << "Case #" << cas << ": ";
		
		string in;
		cin >> in;

		if (isSpecial(in)) {
			REP(_, SIZE(in) - 1) cout << 9;
			cout << endl;
			continue;
		}

		vector<char> res;

		REP(i, SIZE(in)) {
			res.pb(in[i]);
			if (i < SIZE(in) - 1 && in[i] > in[i + 1]) {
				bool dec = false;
				for (char& c : res) {
					if (c == in[i]) {
						if (!dec) {
							--c;
							dec = true;
						} else {
							c = '9';
						}
					}
				}
				break;
			}
		}
		for (char c : res) cout << c;
		REP(_, SIZE(in) - SIZE(res)) {
			cout << 9;
		}
		cout << endl;
	}	

	return 0;
}
