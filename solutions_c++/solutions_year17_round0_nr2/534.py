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
	vector<ll> v;
	int pre;
	rep(i,18) {
		if(i == 0) {
			rep(j,9)
				v.push_back(j+1);
			pre = 0;
		}
		else {
			int nex = v.size();
			for(int j = pre; j < nex; j++) {
				for(int k = v[j]%10; k <= 9; k++) {
					v.push_back(v[j]*10+k);
				}
			}
			pre = nex;
		}
	}
	sort(all(v));
	int T;
	cin >> T;
	rep(t,T) {
		ll N;
		cin >> N;
		cout << "Case #" << t+1 << ": ";
		cout << (*(upper_bound(v.begin(), v.end(), N)-1)) << endl;
	}
	return 0;
}
