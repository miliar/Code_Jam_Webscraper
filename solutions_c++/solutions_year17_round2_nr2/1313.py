#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(int i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (int) w.size()
#define getin(i,n,tab) REP(i,n) { cin >> tab[i]; }
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pii;
typedef pair<string, int> para;
const int inf = 1e9 + 7;
const int MAXN = 1e6 + 7;

string ryb_ans(int a, int b, int c) {
	string result = "";
	if (a > 0) {
		a--;
		result += "R";
	} else if (b > 0) {
		b--;
		result += "Y";
	} else {
		c--;
		result += "B";
	}
	
	bool whoops = false;
	while (a > 0 || b > 0 || c > 0) {
		if (result[result.size() - 1] == 'R') {
			if (b >= c && b > 0) {
				b--;
				result += "Y";
			} else if (c > 0) {
				c--;
				result += "B";
			} else {
				whoops = true;
				break;
			}
		} else if (result[result.size() - 1] == 'Y') {
			if (a >= c && a > 0) {
				a--;
				result += "R";
			} else if (c > 0) {
				c--;
				result += "B";
			} else {
				whoops = true;
				break;
			}
		} else {
			if (a >= b && a > 0) {
				a--;
				result += "R";
			} else if (b > 0) {
				b--;
				result += "Y";
			} else {
				whoops = true;
				break;
			}
		}
	}
	
	for (int i = 1; i < result.size(); i++) {
		if (result[i] == result[i - 1]) {
			whoops = true;
		}
	}
	
	if (whoops) {
		return "lul";
	}
	
	return result;
}

int main() {
	ios_base::sync_with_stdio(0);
	
	int t, n;
	cin >> t;
	int r, o, y, g, b, v;
	string tmp1, tmp2, tmp3, tmp_ans, res;
	bool wow1, wow2, wow3;
	
	RI(q, t) {
		cin >> n >> r >> o >> y >> g >> b >> v;
		
		if (r == 0 && o == 0 && g == 0 && b == 0) {
			if (y == v) {
				res = "";
				for (int i = 0; i < y; i++) {
					res += "YV";
				}
				cout << "Case #" << q << ": " << res << endl;
			} else {
				cout << "Case #" << q << ": IMPOSSIBLE" << endl;
			}
			continue;
		}
		
		if (r == 0 && y == 0 && g == 0 && v == 0) {
			if (o == b) {
				res = "";
				for (int i = 0; i < b; i++) {
					res += "BO";
				}
				cout << "Case #" << q << ": " << res << endl;
			} else {
				cout << "Case #" << q << ": IMPOSSIBLE" << endl;
			}
			continue;
		}
		
		if (y == 0 && o == 0 && v == 0 && b == 0) {
			if (r == g) {
				res = "";
				for (int i = 0; i < r; i++) {
					res += "RG";
				}
				cout << "Case #" << q << ": " << res << endl;
			} else {
				cout << "Case #" << q << ": IMPOSSIBLE" << endl;
			}
			continue;
		}
		
		if ((o >= b && o != 0) || (g >= r && g != 0) || (v >= y && v != 0)) {
			cout << "Case #" << q << ": IMPOSSIBLE" << endl;
			continue;
		}
		
		b -= o;
		r -= g;
		y -= v;
		
		tmp_ans = ryb_ans(r, y, b);
		
		if (tmp_ans == "lul") {
			cout << "Case #" << q << ": IMPOSSIBLE" << endl;
			continue;
		}
		tmp1 = "R";
		tmp2 = "Y";
		tmp3 = "B";
		
		REP(i, g) {
			tmp1 += "GR";
		}
		
		REP(i, v) {
			tmp2 += "VY";
		}
		
		REP(i, o) {
			tmp3 += "OB";
		}
		
		wow1 = false;
		wow2 = false;
		wow3 = false;
		res = "";
		for (int i = 0; i < tmp_ans.size(); i++) {
			if (tmp_ans[i] == 'R') {
				if (wow1) {
					res += "R";
				} else {
					res += tmp1;
				}
			} else if (tmp_ans[i] == 'Y') {
				if (wow2) {
					res += "Y";
				} else {
					res += tmp2;
				}
			} else {
				if (wow3) {
					res += "B";
				} else {
					res += tmp3;
				}
			}
		}
		
		if (res[0] == res[res.size() - 1]) {
			cout << "Case #" << q << ": IMPOSSIBLE" << endl;
			continue;
		}
		
		cout << "Case #" << q << ": " << res << endl;
	}
}