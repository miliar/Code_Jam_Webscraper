#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
#define getin(i,n,tab) REP(i,n) { cin >> tab[i]; }
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pii;
typedef pair<string, int> para;
const long double inf = 1e15 + 7;
const int MAXN = 1e6 + 7;



int main() {
	ios_base::sync_with_stdio(0);
	
	int t;
	cin >> t;
	
	long double d, n, a, b;
	vector<long double> k, s;
	long double res = inf;
	
	RI(q, t) {
		res = inf;
		
		cin >> d >> n;
		
		REP(i, n) {
			cin >> a >> b;
			k.push_back(d - a);
			s.push_back(b);
		}
		
		REP(i, k.size()) {
			res = min(res, d * s[i] / k[i]);
		}
		
		
		cout.precision(6);
		cout << fixed << "Case #" << q << ": " << res << endl;
		k.clear();
		s.clear();
	}
}