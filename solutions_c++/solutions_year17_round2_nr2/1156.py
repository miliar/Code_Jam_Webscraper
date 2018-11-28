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
		int N;
		cin >> N;
		string 	Cs = "ROYGBV";
		vector<pair<int,char>> C(6);
		rep(i,0,6){
			int k;
			cin >> k;
			C[i] = {k,i};
		}
		sort(C.rbegin(), C.rend());
		if(2*C[0].first > N){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		vector<string> G(C[0].first);
		int i = 0;
		while(N > 0) trav(s,G){
			cerr << N << endl;
			if(--N < 0) break;
			while(i < 6 && !C[i].first) ++i;
			if(i == 6) break;
			--C[i].first;
			s += Cs[C[i].second];
		}
		trav(s,G) if(s.size() == 1){
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		trav(i,G) cout << i;
		cout << endl;	
	}
}