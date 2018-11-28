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
		ll N, P;
		cin >> N >> P;
		vector<ll> R(N);
		rep(i,N) cin >> R[i];
		vector<vector<ll> > Q(N,vector<ll>(P));
		rep(i,N) {
			rep(j,P) cin >> Q[i][j];
			sort(Q[i].rbegin(), Q[i].rend());
		}
		ll res = 0;
		bool flg = true;
		for(ll i = 1; flg; i++) {
			bool rm = true;
			while(rm) {
				for(ll j = 0; j < N; j++) {
					while(Q[j].size() && Q[j].back() * 10 < 9 * R[j] * i)
						Q[j].pop_back();
					if(!(Q[j].size()
							&& 9 * R[j] * i <= Q[j].back() * 10
							&& Q[j].back() * 10 <= 11 * R[j] * i)) {
						rm = false;
					}
				}

				if(rm) {
					res++;
					rep(j,Q.size())
						Q[j].pop_back();
				}
			}
			rep(j,N) if(Q[j].size() == 0) flg = false;
		}
		cout << "Case #" << t+1 << ": " << res << endl;
	}
	return 0;
}
