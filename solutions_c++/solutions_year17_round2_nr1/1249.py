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
		int N;
		double D;
		cin >> D >> N;
		double A = 0;
		rep(i,0,N){
			double k,s;
			cin >> k >> s;
			A = max(A,(D-k)/s);
		}
		cout.precision(10);
		cout << "Case #" << t << ": " << fixed << D/A << endl;
	}
}