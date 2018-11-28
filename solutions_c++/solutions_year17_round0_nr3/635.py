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

const int oo = 0x3f3f3f3f;

ll n, k;
ll c0, c1;

int main() {
	int t, cn = 1; sc(t);
	while (t--) {
		scanf("%lld%lld", &n, &k);
		c0 = 1ll; c1 = 0ll;
		
		while (k > c0+c1) {
			k -= c0+c1;
			
			ll c00, c11;
			if (n%2ll == 0) {
				c00 = c0;
				c11 = c0+c1+c1;
			} else {
				c00 = c0+c0+c1;
				c11 = c1;
			}
			
			c0 = c00;
			c1 = c11;
			n = (n-1ll)/2ll;
		}
		
		ll last = (k <= c1)? n+1ll: n;
		
		printf("Case #%d: ", cn++);
		printf("%lld %lld\n", last/2ll, (last-1ll)/2ll);
	}
	return 0;
}




































