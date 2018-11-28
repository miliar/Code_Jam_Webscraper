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

void solve(){
	string s;
	int k;
	cin >> s >> k;
	vector<bool> flip(sz(s));
	bool cur = 0;
	int ans = 0;
	rep(i,0,sz(s)){
		if(i >= k) cur = cur ^ flip[i-k];
		if(i+k > sz(s)){
			if(cur != (s[i]=='-')){
				cout << "IMPOSSIBLE\n";
				return;
			}
		} else {
			ans += flip[i] = cur ^ (s[i]=='-');
			cur = cur ^ flip[i];
		}
	}
	cout << ans << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n;
	cin >> n;
	rep(t,1,n+1){
		cout << "Case #" << t << ": ";
		solve();
	}
}