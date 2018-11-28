#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<ll, ll> pll;

const ll oo = 0x3f3f3f3f3f3f3f3f;
const double eps = 1e-9;

#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define FORD(i,a,b) for (ll i = ll(b)-1; i >= (a); i--)

#define sz(c) ll((c).size())
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define xx first
#define yy second
#define has(c, i) ((c).find(i) != (c).end())
#define DBGDO(X) ({ if(1) cerr << "DBGDO: " << (#X) << " = " << (X) << endl; })

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(nullptr);

	ll T;
	cin >> T;
	FOR(i, 0, T){
		cout << "Case #" << i+1 << ": ";

		string s;
		ll num;
		cin >> s;
		cin >> num;

		ll c = 0;

		FOR(i, 0, sz(s)-num+1){
			if(s[i] == '+') continue;
			FOR(j, 0, num)
				s[i+j] = s[i+j] == '+' ? '-' : '+';
			c++;
		}

		bool b = true;
		FOR(i, 0, sz(s)){
			if(s[i] != '+'){
				b = false;
				break;
			}
		}

		if(b){
			cout << c << endl;
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
