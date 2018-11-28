#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int i = a; i < (b); ++i)
#define rrep(i,a,b) for(int i = b; i --> (a);)
#define all(v) v.begin(),v.end()
#define trav(x,v) for(auto &x : v)
#define sz(v) (int)(v).size()
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long double ld;

void solve(){
	int d,n;
	cin >> d >> n;
	ld t = 0;
	rep(_,0,n){
		ld k,s;
		cin >> k >> s;
		t = max(t, (d-k)/s);
	}
	cout << d/t << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	cout.precision(8);
	
	int n;
	cin >> n;

	rep(i,1,n+1){
		cout << "Case #" << i << ": ";
		solve();
	}
}