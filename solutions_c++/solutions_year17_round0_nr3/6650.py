#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) for (int i=0; i<a; i++)
#define FORd(i,a,b) for (int i = (b)-1; i >= a; i--)
#define F0Rd(i,a) for (int i = (a)-1; i >= 0; i--)

#define mp make_pair
#define pb push_back
#define f first
#define s second
#define lb lower_bound
#define ub upper_bound

const int MOD = 1000000007;
double PI = 4*atan(1);

pair<ll,ll> get(ll N, ll K) {
	map<ll,ll> tm;
	tm[N] = 1;
	while (K) {
		auto x = *tm.rbegin();
		ll y1 = (x.f-1)/2, y2 = x.f/2;
		if (x.s >= K) return {y2,y1};
		if (y1 > 0) tm[y1] += x.s;
		if (y2 > 0) tm[y2] += x.s;
		K -= x.s;
		tm.erase(x.f);
	}
	return {0,0};
}

int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	ios_base::sync_with_stdio(0);cin.tie(0);
	int T; cin >> T;
	F0R(i,T) {
		cout << "Case #" << (i+1) << ": ";
		ll N,K; cin >> N >> K;
		auto z = get(N,K);
		cout << z.f << " " << z.s << "\n";
	}
}
