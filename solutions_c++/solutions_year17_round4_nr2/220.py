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

const int MAX_N = 1005;

int cntBuyers[MAX_N], cntAll[MAX_N];

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    

	int t;
	scanf("%d", &t);
	forn (tt, t) {
	    int n, c, m;
	    scanf("%d%d%d", &n, &c, &m);
	    forn (i, c)
	    	cntBuyers[i] = 0;
	    forn (i, n + 1)
	    	cntAll[i] = 0;
	    forn (i, m) {
	    	int b, p;
	    	scanf("%d%d", &p, &b);
	    	b--;
	    	cntAll[p]++;
	    	cntBuyers[b]++;
	    }
	    int lower = 0;
	    forn (i, c)
	    	lower = max(lower, cntBuyers[i]);
	    int curSum = 0;
	  	forab (i, 1, n + 1) {
	  		curSum += cntAll[i];
	  		lower = max(lower, (curSum + i - 1) / i);
		}	
		int promotions = 0;
		forab (i, 1, n + 1)
			promotions += max(0, cntAll[i] - lower);
		printf("Case #%d: %d %d\n", tt + 1, lower, promotions);			
	}	

	return 0;
}