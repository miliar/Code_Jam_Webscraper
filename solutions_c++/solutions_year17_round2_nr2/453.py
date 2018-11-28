#include <bits/stdc++.h>
  
using namespace std;
  
#define rep(i,n) REP(i,0,n)
#define REP(i,s,e) for(int i=(s); i<(int)(e); i++)
#define pb push_back
#define all(r) r.begin(),r.end()
#define rall(r) r.rbegin(),r.rend()
#define fi first
#define se second
  
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
 
const int INF = 1e9;
const ll MOD = 1e9 + 7;
double EPS = 1e-8;

int main(){
	int mCase;
	scanf("%d", &mCase);
	
	for(int Case = 1; Case <= mCase; Case++){
		string no = "IMPOSSIBLE";
		string ans;
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		if(o > b) ans = no;
		if(g > r) ans = no;
		if(v > y) ans = no;
		//cout << ans << endl;
		int R, Y, B;
		R = r - g;
		Y = y - v;
		B = b - o;
		int N = R + Y + B;
		//cout <<N << " " <<  R <<" " << Y << " " << B << endl;
		if(o == b && o != 0) {
			rep(i, o) ans += "OB";
			printf("Case #%d: ", Case);
			cout << (n == o + b ?ans : no)<< endl;
			continue;
		}
		if(g == r && g != 0) {
			rep(i, g) ans += "GR";
			printf("Case #%d: ", Case);
			cout << (n == g + r ?ans : no) << endl;
			continue;
		}
		if(v == y && v != 0) {
			rep(i, v) ans += "VY";
			printf("Case #%d: ", Case);
			cout << (n == v + y ?ans : no) << endl;
			continue;
		}
		if(R * 2 > N || Y * 2 > N || B * 2 > N) ans = no;
		if(ans == no) {
			printf("Case #%d: ", Case);
			cout << ans << endl;
			continue;
		}
		vector<pii> vp;
		string str = "RBY";
		vp.pb({R, 0});
		vp.pb({B, 1});
		vp.pb({Y, 2});
		sort(rall(vp));
		// rep(i, 3) {
		// 	cout << vp[i].fi <<" " << str[vp[i].se] << endl;
		// }
		rep(i, vp[1].fi) {
			ans += str[vp[0].se];
			ans += str[vp[1].se];
		}
		vp[0].fi -= vp[1].fi;
		rep(i, vp[0].fi) {
			ans += str[vp[0].se];
			ans += str[vp[2].se];
		} 
		vp[2].fi -= vp[0].fi;
		int idx = 1;
		rep(i, vp[2].fi) {
			ans = ans.substr(0, idx) + str[vp[2].se] + ans.substr(idx);
			idx += 2;
		}
		for(int i = ans.size()-1; i >= 0; i--) {
			if(ans[i] == 'R' && g > 0) {
				ans = ans.substr(0, i) + "RGR" + (i+1<ans.size()?ans.substr(i+1):"");
				g--;
			}
			else if(ans[i] == 'B' && o > 0) {
				ans = ans.substr(0, i) + "BOB" + (i+1<ans.size()?ans.substr(i+1):"");
				o--;
			}
			else if(ans[i] == 'Y' && v > 0){
				ans = ans.substr(0, i) + "YVY" + (i+1<ans.size()?ans.substr(i+1):"");
				v--;
			}
		}

		printf("Case #%d: ", Case);
		cout << ans << endl;
	}
}