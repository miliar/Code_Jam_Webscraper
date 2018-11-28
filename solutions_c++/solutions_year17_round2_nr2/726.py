#include <bits/stdc++.h>

#define f(_i, _n) for (auto _i = 0; _i < _n; _i++)
#define F(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define fr(_i, _k, _n) for (auto _i = _k; _i < _n; _i++)
#define r(_t, _n)     _t _n;     cin >> _n;
#define ra(_type, _name, _len)_type _name[_len]; f(_i, _len)    cin >> _name[_len];
#define mp make_pair
#define re return
#define takedown re 0;
#define fi first
#define se second
#define in(_name) freopen(_name, "r", stdin);
#define out(_name) freopen(_name, "w", stdout);
#define pb push_back
#define fill(_a, _n) memset(_a, _n, sizeof(_a))
#define all(_v) _v.begin(), _v.end()
#define deb cout << "  DEBUG "

using namespace std;
typedef pair<int,int> pii;
typedef long long ll;

void solve(int i){
	int n;
	int R, G, Y, O, B, V;
    cin >> n >> R >> O >> Y >> G >> B >> V;
    int r = R, y = Y, b = B;
    if(2 * max({R, Y, B}) > R+Y+B){
		cout << "Case #" << i << ": " << "IMPOSSIBLE" << '\n';
		re;
    }
    string aa;
    int nn = R+Y+B;
    f(i, nn) aa+=' ';
    string ans = aa;
    int fi, se, th;
    char cfi, cse, cth;
    pair<int, char> p[3] = {{R, 'R'}, {Y, 'Y'}, {B, 'B'}};
    sort(p, p+3);
    fi = p[2].fi;
    se = p[1].fi;
    th = p[0].fi;
    cfi = p[2].se;
    cse = p[1].se;
    cth = p[0].se;
    for(int i = 0; i < nn; i+=2) {
		if(fi){
			fi--;
			ans[i]=cfi;
		}
		else if(se){
			se--;
			ans[i]=cse;
		}
		else{
			th--;
			ans[i]=cth;
		}
    }
    for(int i = 1; i < nn; i+=2) {
		if(fi){
			fi--;
			ans[i]=cfi;
		}
		else if(se){
			se--;
			ans[i]=cse;
		}
		else{
			th--;
			ans[i]=cth;
		}
    }
//    if(ans[0] == ans[ans.size()-1]){
//		deb << n << ' ' << r << ' ' << y << ' ' << b << endl;
//		deb << ans << endl;
//		re;
//    }
//    f(i, n-1){
//		if(ans[i] == ans[i+1]){
//			deb << n << ' ' << r << ' ' << y << ' ' << b << endl;
//			deb << ans << endl;
//			re;
//		}
//    }
    cout << "Case #" << i << ": " << ans << '\n';
}

int main(){
	in("B-small-attempt2.in");
	out("out.txt");
	int t;
	cin >> t;
	f(i, t) solve(i+1);
}
