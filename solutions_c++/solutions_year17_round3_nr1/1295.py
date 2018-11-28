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
		int N,K;
		cin >> N >> K;
		vector<pair<double,double>> C(N);
		trav(i,C) cin >> i.first >> i.second;
		double ans = 0;
		sort(all(C));
		multiset<double> S;
		rep(i,0,K-1) S.insert(2*M_PI*C[i].first*C[i].second);
		rep(i,K-1,N){
			double sum = C[i].first*C[i].first*M_PI + 2*M_PI*C[i].first*C[i].second;
			int c = 0;
			auto it = S.end();
			while(++c < K)
				sum += *(--it);
			S.insert(2*M_PI*C[i].first*C[i].second);
			ans = max(ans,sum);
		}
		cout.precision(10);
		cout << "Case #" << t << ": " << fixed << ans << endl;
	}
}