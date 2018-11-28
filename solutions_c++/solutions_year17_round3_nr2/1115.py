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
		int N,M;
		cin >> N >> M;
		vi A(N),B(N),C(M),D(M);
		rep(i,0,N) cin >> A[i] >> B[i];
		rep(i,0,M) cin >> C[i] >> D[i];
		sort(all(A));
		sort(all(B));
		sort(all(C));
		sort(all(D));
		if(N == 1 || M == 1) cout << 2 << endl;
		if(N == 2) cout << (min((A[0]-B[1]+24*60)%(24*60), A[1]-B[0])+B[0]-A[0]+B[1]-A[1] > 720 ? 4 : 2) << endl;
		if(M == 2) cout << (min((C[0]-D[1]+24*60)%(24*60), C[1]-D[0])+D[0]-C[0]+D[1]-C[1] > 720 ? 4 : 2) << endl;
	}
}