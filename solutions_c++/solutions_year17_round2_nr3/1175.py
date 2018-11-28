#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = (a); i < int(b); ++i)
#define rrep(i,b,a) for(int i = (b); i --> int(a);)
#define trav(i,v) for(auto&i:v)
#define all(c) (c).begin(), (c).end()
#define sz(c) int((c).size())
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
int main(){
	cin.sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	rep(t,1,T+1){
		cout << "Case #" << t << ": ";
		int N,Q;
		cin >> N >> Q;
		int E[110];
		double S[110];
		rep(i,0,N) cin >> E[i] >> S[i];
		int D[110][110];
		rep(i,0,N) rep(j,0,N) cin >> D[i][j];
		cin >> Q >> Q;
		vector<double> DP(N,1e18);
		DP[0] = 0;
		rep(i,0,N-1){
			int td = 0;
			rep(j,i+1,N){
				td += D[j-1][j];
				if(td > E[i]) break;
				DP[j] = min(DP[j],DP[i]+td/S[i]);
			}
		}
		cout.precision(10);
		cout << fixed << DP[N-1] << endl;
	}	
}