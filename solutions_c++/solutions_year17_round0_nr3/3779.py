#define FNAME ""

#undef __STRICT_ANSI__

#include <bits/stdc++.h> 

using namespace std;

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define fst first
#define snd second
#define sz(x) (int)((x).size()) 
#define forn(i,n) for (int i = 0; (i) < (n); ++i)
#define fornr(i,n) for (int i = (int)(n) - 1; (i) >= 0; --i)
#define forab(i,a,b) for (int i = (a); (i) < (b); ++i)
#define forba(i,a,b) for (int i = (int)(b) - 1; (i) >= (a); --i)
#define forit(it,c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define all(c) (c).begin(),(c).end()

#ifdef LOCAL
	#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#else
	#define eprintf(...) static_cast<void>(0)   
#endif

#ifdef _WIN32
	#define I64 "%I64d"
	#define U64 "%I64u"
#else
	#define I64 "%lld"
	#define U64 "%llu"
#endif

typedef long long ll;
typedef unsigned long long ull;
typedef double dbl;
typedef long double ld;
typedef unsigned int uint;
typedef vector <int> vi;
typedef pair <int, int> pii;

map<ll, ll> cnt;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	forab(q, 1, t + 1) {
		cnt.clear();
		ll n, k;
		cin >> n >> k;
		cnt[n] = 1;
		auto it = cnt.find(n);
		while(1) {
			ll len = it->fst;
			ll num = it->snd;
			if (num < k) {
				k -= num;
				ll l = (len - 1) / 2;
				cnt[l] += num;
				cnt[len - 1 - l] += num;
			} else {
				ll l = (len - 1) / 2;
				ll r = len - 1 - l;
				cout << "Case #" << q << ": " << r << " " << l << '\n';
				break;
			}
			it--;
		}
	}
	return 0;
}
