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

const int MAX_N = 100;
const double EPS = 1e-4;

double a[MAX_N], d[MAX_N][MAX_N];
double c;

void clear(int n, int k) {
	c = 1;
}

void check(int l, int r, int k) {
    forab (i, l, r)
	    c *= a[i - 1];
}

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    
	int t;
	scanf("%d", &t);
	forn (tt, t) {
	 	int n, k;
	 	double u;
	 	scanf("%d%d%lf", &n, &k, &u);
	 	forn (i, n)
	 		scanf("%lf", &a[i]);
	 	sort(a, a + n);
	 	a[n] = 1;
	 	forn (i, n) {
	 	 	if (u >= (a[i + 1] - a[i]) * (i + 1)) {
	 	 	 	u -= (a[i + 1] - a[i]) * (i + 1);
	 	 	 	forn (j, i + 1)
	 	 	 		a[j] = a[i + 1];	 	 	 	
	 	 	} else {
				c = u / (i + 1);
	 	 	  	forn (j, i + 1)
	 	 	  		a[j] += c;
	 	 	  	break;
	 	 	}
	 	}
	 	double ans = 1;
	 	forn (i, n)
	 		ans *= a[i];
	 	printf("Case #%d: %.20f\n", tt + 1, ans);
	}
    //double time1 = clock() * 1. / CLOCKS_PER_SEC;
	//cout << time1 << endl;
	return 0;
}