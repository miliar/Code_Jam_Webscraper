#include <bits/stdc++.h>
using namespace std;

#define FOR(i,a,b) for(int i=a;i<int(b);i++)
#define FIL(a,b) memset((a),(b),sizeof(a))
#define SZ(a) ((int)(a).size())
#define ALL(a) begin(a),end(a)
#define PB push_back
#define FI first
#define SE second
typedef long long LL;
typedef pair<int,int> PT;
typedef complex<double> PX;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<PT> VPT;
template<typename T> ostream& operator<<(ostream& s, vector<T>& v)
{ s << '{'; FOR(i,0,v.size()) s << (i ? "," : "") << v[i]; return s << '}'; }
template<typename S, typename T> ostream& operator<<(ostream &s, pair<S,T> const& p)
{ return s << '(' << p.first << ',' << p.second << ')'; }

int TC, Hd, Ad, Hk, Ak, B, D, ans;

void tryIt(int b, int d) {
	int hd = Hd, ad = Ad, hk = Hk, ak = Ak, ta = 0;
	FOR(i,0,d) {
		if (hd - (ak-D) <= 0) {
			hd = Hd - ak;
			ta++;
		}
		if (hd - (ak-D) <= 0) return;
		ak -= D;
		hd -= ak;
		ta++;
	}
	FOR(i,0,b) {
		if (hd - ak <= 0) {
			hd = Hd - ak;
			ta++;
		}
		if (hd - ak <= 0) return;
		ad += B;
		hd -= ak;
		ta++;
	}
	while (hk > 0) {
		if (hd - ak <= 0 && hk - ad > 0) {
			hd = Hd - ak;
			ta++;
			//printf("Cure\n");
		}
		if (hd - ak <= 0 && hk - ad > 0) return;
		hk -= ad;
		hd -= ak;
		ta++;
		//printf("Attack\n");
	}
	ans = min(ans, ta);
}

int main() {
	cin >> TC;
	FOR(tc,1,TC+1) {
		cin >> Hd >> Ad >> Hk >> Ak >> B >> D;
		ans = INT_MAX;
		FOR(b,0,101) FOR(d,0,101) tryIt(b, d);
		tryIt(0,0);
		cout << "Case #" << tc << ": ";
		if (ans == INT_MAX) cout << "IMPOSSIBLE"; else cout << ans;
		cout << endl;
	}
}
