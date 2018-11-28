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

int solve(){
	int n, p;
	cin >> n >> p;
	vi cnt(p);
	rep(_,0,n){
		int g;
		cin >> g;
		++cnt[g%p];
	}
	int ans = 0;
	ans += cnt[0];
	cnt[0] = 0;
	if(p==2){
		ans += cnt[1]/2;
		cnt[1] %= 2;
	} else if(p==3){
		int d = min(cnt[1], cnt[2]);
		ans += d;
		cnt[1] -= d, cnt[2] -= d;
		ans += cnt[1]/3;
		cnt[1] %= 3;
		ans += cnt[2]/3;
		cnt[2] %= 3;
	}
	trav(x, cnt) if(x) ++ans;

	return ans;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	int n;
	cin >> n;
	rep(t,1,n+1){
		cout << "Case #" << t << ": " << solve() << endl;
	}
}