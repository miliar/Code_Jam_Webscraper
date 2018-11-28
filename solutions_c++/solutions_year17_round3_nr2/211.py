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

const int MAX = 1440, INF = 1e9;

int used[MAX + 5], dp[MAX + 5][MAX + 5][2][2];
pii a[MAX], b[MAX];

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    

	int t;
	scanf("%d", &t);
	forn (tt, t) {
	    int n, m;
	    scanf("%d%d", &n, &m);
	    forn (i, MAX + 1)
	    	used[i] = 0;
	    forn (i, n) {
	    	scanf("%d%d", &a[i].fs, &a[i].sc);
	    	forab (j, a[i].fs, a[i].sc)
	    		used[j] = 1;
	    }
	    forn (i, m) {
	    	scanf("%d%d", &b[i].fs, &b[i].sc);
	    	forab (j, b[i].fs, b[i].sc)
	    		used[j] = 2;
	    }
	    forn (tim, MAX + 1)
	    	forn (i, MAX + 1)
	    		forn (j, 2)
	    			forn (g, 2)
		    			dp[tim][i][j][g] = INF;
	    if (used[0] == 0)
	     	dp[1][0][1][1] = dp[1][1][0][0] = 0;
	    if (used[0] == 1)
	     	dp[1][1][0][0] = 0;
	    if (used[0] == 2)
	     	dp[1][0][1][1] = 0;
	    forab (tim, 2, MAX + 1) {
	     	forn (i, tim + 1) {
	     		forn (j, 2) {
		     		if (used[tim - 1] != 2 && i != 0)
		     			dp[tim][i][j][0] = min(dp[tim - 1][i - 1][j][0], dp[tim - 1][i - 1][j][1] + 1);
            	    if (used[tim - 1] != 1) 
		     			dp[tim][i][j][1] = min(dp[tim - 1][i][j][1], dp[tim - 1][i][j][0] + 1);
		     		//if (tim == 1399 && i == MAX / 2)
		     		//printf("d[%d][%d][%d][%d] = %d, %d\n", tim, i, j, 0, dp[tim][i][j][0], used[tim - 1]);
	        	}
	     	}
	    }
	    printf("Case #%d: %d\n", tt + 1, min(dp[MAX][MAX / 2][0][0], min(dp[MAX][MAX / 2][1][1], min(dp[MAX][MAX / 2][0][1] + 1, dp[MAX][MAX / 2][1][0] + 1))));
	}	

	return 0;
}