#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <istream>
#include <ostream>

#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cassert>

using namespace std;

#define fi first
#define se second
#define mkp make_pair
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define rep(i,n) for(ll i=0; i < (n); ++i)
#define rrep(i,n) for(ll i=((n)-1); i >= 0; --i)

#define OPLT(T) bool operator<(const T & lop_, const T & rop_)
#define OPEQ(T) bool operator==(const T & lop_, const T & rop_)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

istream& operator>>(istream& istr, __float128& obj) { double d; istr >> d; obj = d; return istr; };
ostream& operator<<(ostream& ostr, __float128& obj) { ostr << static_cast<double>(obj); return ostr; };

int R, C;
vector<string> v;

void solve(pii xb, pii yb) {
	char c;
	int cnt = 0;
	vector<pii> div;
	for(int i = yb.fi; i < yb.se; i++) {
		for(int j = xb.fi; j < xb.se; j++) {
			if(v[i][j] != '?') {
				c = v[i][j];
				div.push_back(pii(i,j));
				cnt++;
			}
		}
	}
	assert(cnt > 0);
	if(cnt == 1) {
		for(int i = yb.fi; i < yb.se; i++)
			for(int j = xb.fi; j < xb.se; j++)
				v[i][j] = c;
	}
	else {
		if(div[0].fi != div[1].fi) {
			solve(xb,pii(yb.fi, div[1].fi));
			solve(xb,pii(div[1].fi, yb.se));
		}
		else {
			solve(pii(xb.fi, div[1].se), yb);
			solve(pii(div[1].se, xb.se), yb);
		}
	}
}

int main() {
	int T;
	cin >> T;
	rep(t,T) {
		cin >> R >> C;
		v.clear(); v.resize(R);
		rep(i,R)
			cin >> v[i];
		solve(pii(0,C), pii(0,R));
		cout << "Case #" << t+1 << ":" << endl;
		rep(i,R)
			cout << v[i] << endl;
	}
	return 0;
}
