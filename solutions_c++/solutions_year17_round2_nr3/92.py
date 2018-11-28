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

int E[105], S[105];
ll D[105][105];
double T[105][105];

void solve(){
	int N, Q;
	cin >> N >> Q;
	rep(i,0,N){
		cin >> E[i] >> S[i];
	}
	rep(i,0,N)
		rep(j,0,N){
			T[i][j] = 1e18;
			cin >> D[i][j];
			if(D[i][j] == -1)
				D[i][j] = 1000000000000000LL;
		}
	rep(i,0,N)
	rep(j,0,N)
	rep(k,0,N){
		D[j][k] = min(D[j][k], D[j][i]+D[i][k]);
	}
	rep(i,0,N)
	rep(j,0,N){
		if(E[i] >= D[i][j]){
			T[i][j] = min(T[i][j], ((double)D[i][j])/S[i]);
		}
	}
	rep(i,0,N)
	rep(j,0,N)
	rep(k,0,N){
		T[j][k] = min(T[j][k], T[j][i]+T[i][k]);
	}
	while(Q--){
		int U, V;
		cin >> U >> V;
		--U;
		--V;
		cout << setprecision(9) << fixed << T[U][V] << " ";
	}
	cout << endl;
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
