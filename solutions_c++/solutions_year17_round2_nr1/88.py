#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = (a); i < int(b); ++i)
#define rrep(i, a, b) for(int i = (a) - 1; i >= int(b); --i)
#define trav(it, v) for(typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it)
#define all(v) (v).begin(), (v).end()
#define what_is(x) cerr << #x << " is " << x << endl;
#define sz(x) (int)(x).size()

typedef double fl;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;

double K[10005], S[10005];

void solve(){
	double lo=0, hi=1e18;
	int D, N;
	cin >> D >> N;
	rep(i,0,N)
		cin >> K[i] >> S[i];
	rep(it,0,100){
		double v = (lo+hi)/2;
		bool ok=1;
		double t = D/v;
		rep(i,0,N){
			double pos = K[i] + S[i] * t;
			if(pos < D)
				ok = 0;
		}
		if(ok)
			lo = v;
		else
			hi = v;
	}
	cout << setprecision(9) << fixed << hi << endl;
}

int main(){
	ios::sync_with_stdio(0);
	int T;
	cin >> T;
	for(int i=1; i <= T; ++i){
		cout << "Case #" << i << ": ";
		solve();
	}
}
