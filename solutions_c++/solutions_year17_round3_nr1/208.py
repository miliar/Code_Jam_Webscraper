#include <bits/stdc++.h> 

using namespace std;
 
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define fst first
#define snd second
#define sz(x) (int) ((x).size()) 
#define forn(i, n) for (int i = 0; (i) < (n); ++i)
#define fornr(i, n) for (int i = (n) - 1; (i) >= 0; --i)
#define forab(i, a, b) for (int i = (a); (i) < (b); ++i)
#define forba(i, a, b) for (int i = (b) - 1; (i) >= (a); --i)
#define forit(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(), (c).end() 

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) static_cast<void>(0)   
#endif

#ifdef _WIN32
	#define I64 "%I64d"
#else
	#define I64 "%lld"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef unsigned int uint;
typedef vector <int> vi;
typedef pair <int, int> pii;

#define FNAME ""

const double PI = 3.1415926535897932384626433832795;

const int MAX_N = 1e5 + 5;

pii a[MAX_N];
vector<ll> v;

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    

	int t;
	scanf("%d", &t);
	forn (tt, t) {
	 	int n, k;
	 	scanf("%d%d", &n, &k);
	 	forn (i, n)
	 		scanf("%d%d", &a[i].fs, &a[i].sc);
		ll maxx = 0;
	 	forn (i, n) {
	 	 	ll ans = a[i].fs * 1ll * a[i].fs + 2 * a[i].fs * 1ll * a[i].sc;
	 	 	v.clear();
	 	 	forn (j, n)
	 	 		if (j != i && a[j].fs <= a[i].fs)
	 	 			v.pb(2 * a[j].fs * 1ll * a[j].sc);
			if (sz(v) < k - 1)
				continue;
			sort(all(v));
			reverse(all(v));
			forn (i, k - 1)
				ans += v[i];
			maxx = max(maxx, ans);
	 	}
	 	printf("Case #%d: %.20f\n", tt + 1, maxx * PI);
	}

	return 0;
}