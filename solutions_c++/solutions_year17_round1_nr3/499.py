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

int t, hd, ad, hk, ak, b, d;

class state {
	public:
		int hd;
		int ad;
		int hk;
		int ak;
		state(int j, int k, int l, int m) : hd(j), ad(k), hk(l), ak(m) {}
		void print() {
			cout<<hd<<" "<<ad<<" "<<hk<<" "<<ak<<endl;
		}

};

struct Class1Compare
{
   bool operator() (const state& l, const state& r) const
   {
       if (l.hd == r.hd) {
		   if (l.ad == r.ad) {
			   if (l.hk == r.hk) {
				   return l.ak < r.ak;
			   } else return l.hk < r.hk;
		   } else return l.ad < r.ad;
	   } else return l.hd < r.hd;
   }
};

map<state, int, Class1Compare> used;

int solve() {
	state st = state(hd, ad, hk, ak);
	queue<state> Q;
	while (!Q.empty()) Q.pop();
	used[st] = 1;
	Q.push(st);

	while (!Q.empty()) {
		st = Q.front(); Q.pop();
		//st.print();
		int odl = used[st];

		if (st.hd <= 0) {}
		else {
			// my attack
			state st2 = state(st.hd - st.ak, st.ad, st.hk - st.ad, st.ak);
			if (st2.hk <= 0)
				return odl + 1;
			if (st2.hd > 0 && used[st2] == 0) {
				Q.push(st2);
				used[st2] = odl + 1;
			}

			// debuff
			int newAtk = st.ak - d;
			st2 = state(st.hd - newAtk, st.ad, st.hk, max(newAtk, 0));
			if (st2.hd > 0 && used[st2] == 0) {
				Q.push(st2);
				used[st2] = odl + 1;
			}

			// buff
			st2 = state(st.hd - st.ak, st.ad + b, st.hk, st.ak);
			if (st2.hd > 0 && st2.ad <= st2.hk && used[st2] == 0) {
				Q.push(st2);
				used[st2] = odl + 1;
			}

			//cure
			st2 = state(hd - st.ak, st.ad, st.hk, st.ak);
			//cout<<"st2 ";
			//st2.print();
			//cout<<used[st2]<<endl;
			if (st2.hd > 0 && used[st2] == 0) {
				Q.push(st2);
				used[st2] = odl + 1;
			}
		}
	}
	return -1;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin>>t;
	RI(x, t) {
		cin>>hd>>ad>>hk>>ak>>b>>d;
		int ans = solve();
		cout<<"Case #"<<x<<": ";
		if (ans == -1) cout<<"IMPOSSIBLE\n";
		else
			cout<<ans - 1 << endl;
		used.clear();
	}
	return 0;
}
