#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(ll i = (a); i <= (b); ++i)
#define FORD(i,a,b) for(ll i = (a); i >= (b); --i)
#define RI(i,n) FOR(i,1,(n))
#define REP(i,n) FOR(i,0,(n)-1)
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
#define mp make_pair
#define pb push_back
#define st first
#define nd second
#define sz(w) (ll) w.size()
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pii;
typedef pair<pii, ll> para;
const ll inf = 1e9 + 7;
const ll maxN = 1e6 + 5;

ll t, cnt[5];

void solve(ll n, ll k) {
	if (n == k) {
		cout<<"0 0\n";
		return;
	}

	ll pot = 1;

	ll a = n, b = 0;
	cnt[0] = 1; cnt[1] = 0;
	while (pot < k) {
		ll newA = 0, newB = 0;
		newA = a / 2;
		cnt[2] = cnt[0];
		if (a - newA - 1 != newA && newA != 1) {
			cnt[3] = cnt[0];
			newB = a - newA - 1;
		} else {
			if (a != 2)
				cnt[2] += cnt[0];
		}

		if (b > 1) {
			if (b % 2 == 0) {
				if (b != 2) {
					newB = b - (b / 2) - 1;
					cnt[3] += cnt[1];
				}
				cnt[2] += cnt[1];
			} else {
				cnt[3] += cnt[1] * 2;
			}
		} else {
			cnt[2] += cnt[1];
			if (a != n && b != 0)
				k++;
		}

		a = newA;
		b = newB;
		cnt[0] = cnt[2];
		cnt[1] = cnt[3];
		cnt[2] = cnt[3] = 0;
		//cout<<a<<" "<<b<<" "<<cnt[0]<<" "<<cnt[1]<<" "<<k<<" "<<pot<<endl;
		k -= pot;
		pot *= 2;
	}
	//cout<<a<<" "<<b<<" "<<cnt[0]<<" "<<cnt[1]<<" "<<k<<endl;
	if (k > cnt[0]) a = b;
	cout<<a / 2<<" "<<max(0LL, a - (a/2) - 1)<<endl;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin>>t;
	RI(x, t) {
		ll n, k;
		cin>>n>>k;
		cout<<"Case #"<<x<<": ";
		solve(n, k);
	}
	return 0;
}
