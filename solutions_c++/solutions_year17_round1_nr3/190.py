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

const ll INF = 1e10;

int main() {
	int T;
	cin >> T;
	rep(t,T) {
		ll H_dragon, A_dragon, H_knight, A_knight;
		ll B, D;
		cin >> H_dragon >> A_dragon >> H_knight >> A_knight >> B >> D;
		ll res = INF;
		rep(i,101) {
			rep(j,101) {
				ll Hd, Ad, Hk, Ak;
				ll Buff = 0, Debuff = 0;
				Hd = H_dragon;
				Ad = A_dragon;
				Hk = H_knight;
				Ak = A_knight;
				rep(k,300) {
					// Dragon
					if(Debuff < i) {
						if(Hd - (Ak-D) <= 0) {
							Hd = H_dragon;
						}
						else {
							// Debuff
							Ak = max(Ak-D, 0ll);
							Debuff++;
						}
					}
					else if(Buff < j) {
						if(Hd - Ak <= 0) {
							Hd = H_dragon;
						}
						else {
							// Buff
							Ad = Ad + B;
							Buff++;
						}
					}
					else {
						if(Hd-Ak <= 0 && Hk-Ad > 0) {
							Hd = H_dragon;
						}
						else {
							Hk = max(Hk-Ad, 0ll);
						}
					}

					if(Hk <= 0) {
						res = min(res, k+1);
						break;
					}

					// Knight
					Hd = max(Hd-Ak, 0ll);
				}
			}
		}
		if(res < INF)
			cout << "Case #" << t+1 << ": " << res << endl;
		else
			cout << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}
