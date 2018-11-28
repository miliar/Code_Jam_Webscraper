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
		ll K, N;
		cin >> N >> K;
		map<ll,ll> mp;
		mp[N] = 1;
		ll y, z;
		while(1) {
			ll mx;
			ll num;
			mx  = (mp.rbegin())->fi;
			num = mp[mx];
			if(K <= num) {
				y = (mx-1)/2 + (mx-1)%2;
				z = (mx-1)/2;
				break;
			}
			else {
				mp.erase(mp.find(mx));
				mp[(mx-1)/2] += num;
				mp[(mx-1)/2 + (mx-1)%2] += num;
				K -= num;
			}
		}
		cout << "Case #" << t+1 << ": " << y << " " << z << endl;
	}
	return 0;
}
