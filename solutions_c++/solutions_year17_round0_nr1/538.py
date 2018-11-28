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

int main() {
	int T;
	cin >> T;
	rep(t,T) {
		string s;
		int k;
		int res = 0;
		cin >> s >> k;
		rep(i,s.size()+1 -k) {
			if(s[i] == '-') {
				res++;
				rep(j,k) {
					s[i+j] = '+' + '-' - s[i+j];
				}
			}
		}
		bool flg = true;
		rep(i,k) {
			if(s[s.size()-1 -i] == '-') flg = false;
		}
		cout << "Case #" << t+1 << ": ";
		if(flg)
			cout << res << endl;
		else
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
