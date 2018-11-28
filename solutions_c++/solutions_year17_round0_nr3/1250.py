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
		ll n,k;
		cin>>n>>k;
		ll currN = n;
		ll l = 1;
		ll h = 0;
		ll ans;
		if(k == 1) ans = n;
		else{
			k-=2;
			while(currN>0){
				ll newN = 0;
				if(currN%2==0){
					newN = currN/2-1;
					l = l;
					h = h*2+l;
				}else{
					newN = currN/2;
					h = h;
					l = 2*l + h;
				}
				currN = newN;
				if(l+h<=k) k-=l+h;
				else{
					if(k<h) ans = currN+1;
					else ans = currN;
					break;
				}
			}
		}
		cout<<"Case #"<<Case++<<": ";
		if(ans%2==1) cout<<ans/2<<" "<<ans/2<<endl;
		else cout<<ans/2<<" "<<ans/2-1<<endl;
	}
}