#include <bits/stdc++.h>

using namespace std;

#define fr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define rp(a,b) fr(a,0,b)
#define fre(a,b) for(int a = adj[b]; ~a; a = ant[a])
#define cl(a,b) memset((a), (b), sizeof(a))
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define sc3(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)

#define iter(a) __typeof((a).begin())
#define fore(a,b) for(iter(b) a = (b).begin(); a != (b).end(); ++a)

#define st first
#define nd second
#define mp make_pair
#define pb push_back

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector< vi > vii;

const ll oo = 0x3f3f3f3f3f3f3f3fll;

ll hd, ad, hk, ak, b, d;

ll heal(ll i, ll c) {
	ll r = 0, h = hd, akk = ak;
	int cnt = 0;
	
	bool fm = 1;
	//db(i _ c);
	while (i--) {
		if (cnt == 1000000) return oo;
		cnt++;
		
		ll lak = akk;
		akk = max(0ll, akk - d);
		//db(h _ akk _ fm);
		
		if (h <= akk) {
			if (fm) return oo;
			h = hd;
			r++;
			fm = 1;
			i++;
			akk = lak;
		} else fm = 0;
		h -= akk;
	}
	
	cnt = 0;
	//puts("");
	while (c--) {
		if (cnt == 1000000) return oo;
		cnt++;
		
		//db(h _ akk _ fm);
		
		if (h <= akk && c > 0) {
			if (fm) return oo;
			h = hd;
			r++;
			fm = 1;
			c++;
		} else fm = 0;
		h -= akk;
	}
	return r;
}

ll pd[1009];

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		scanf("%lld%lld", &hd, &ad);
		scanf("%lld%lld", &hk, &ak);
		scanf("%lld%lld", &b, &d);
		
		ll l1 = 0;
		ll h1 = (b == 0)? 0: (max(0ll, hk - ad) + b - 1ll)/b;
		fr(i, l1, h1+1) {
			ll na = ad + ll(i)*b;
			pd[i] = i + (hk + na - 1ll)/na;
			//db(i _ pd[i]);
		}
		//db(l1 _ h1);
		
		ll low = 0;
		ll hi = (d == 0)? 0: (ak+d-1)/d;
		//db(low _ hi);
		
		ll ans = oo;
		fr(i, low, hi+1) {
			fr(j, l1, h1+1) {
				ll op = i;
				ll c = pd[j];
				
				ans = min(ans, op + c + heal(i, c));
			}
		}
		
		printf("Case #%d: ", cn++);
		if (ans == oo) puts("IMPOSSIBLE");
		else printf("%lld\n", ans);
	}
	return 0;
}




































