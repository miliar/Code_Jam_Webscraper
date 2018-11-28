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
		ll n; cin>>n;
		vi d;
		while(n>0){
			d.push_back(n%10);
			n /= 10;
		}
		int nines = 0;
		rep(i,0,d.size()-1){
			if(d[i]<d[i+1]){
				nines = i + 1;
				--d[i+1];
				d[i] = 9;
			}
		}
		while(d[d.size()-1]==0) d.pop_back();
		cout<<"Case #"<<Case++<<": ";
		for(int i = d.size()-1;i>=nines;--i) cout<<d[i];
		rep(i,0,nines) cout<<9;
		cout<<endl;
	}
}