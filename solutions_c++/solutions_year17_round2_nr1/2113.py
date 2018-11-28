#include <bits/stdc++.h>

using namespace std;

#define rep(i, a, b) for(int i = a; i < int(b); ++i)
#define trav(a, v) for(auto& a : v)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define D(x) cerr << #x << " = " << x << endl

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
    cin.sync_with_stdio(false);
	int t; cin>>t;
	int Case = 1;
	while(t--) {
		double d;
		int n;
		cin>>d>>n;
		double ans = 9999999999999999;
		rep(i,0,n){
			int k,s;
			cin>>k>>s;
			double time = (d-k)/s;
			double maxSpeed = d/time;
			ans = min(ans,maxSpeed);
		}
		cout<<"Case #"<<Case++<<": "<<fixed<<setprecision(10)<<ans<<endl;
	}
}