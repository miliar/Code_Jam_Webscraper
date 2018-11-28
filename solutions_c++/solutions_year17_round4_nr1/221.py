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

const int MAX_N = 105;

int cnt[10], a[MAX_N], dp[MAX_N][MAX_N][MAX_N];

int main() {
#ifdef LOCAL    
	freopen(FNAME".in", "r", stdin);
	freopen(FNAME".out", "w", stdout); 
#endif    

	forn (i, MAX_N)
		forn (j, MAX_N)
			forn (g, MAX_N) {
				if (i > 0 || j > 0 || g > 0)
				 	dp[i][j][g] = 1;
			 	forn (x, 11)
			 		forn (y, 11)
			 			forn (z, 11)
			 				if ((x + 2 * y + 3 * z) % 4 == 0 && i >= x && j >= y && g >= z && x + y + z > 0) {
								dp[i][j][g] = max(dp[i][j][g], dp[i - x][j - y][g - z] + 1);
	                        	//if (i <= 10 && j <= 10 && g <= 10)
	                        	//	printf("%d %d %d %d %d %d %d \n", i, j, g, dp[i][j][g], x, y, z);
			 				}
			}

	int t;
	scanf("%d", &t);
	forn (tt, t) {
		forn (i, 5)
			cnt[i] = 0;
	 	int n, p;
	 	scanf("%d%d", &n, &p);
	 	forn (i, n) 
	 		scanf("%d", &a[i]), a[i] %= p;
	 	sort(a, a + n);
	 	int ans = 0;
	 	forn (i, n)
	 		cnt[a[i]]++;
	 	ans += cnt[0];
		if (p == 2) 
		 	ans += (cnt[1] + 1) / 2;
		else {
			if (p == 3) {
			 	ans += min(cnt[1], cnt[2]);
			 	ans += (max(cnt[1], cnt[2]) - min(cnt[1], cnt[2]) + 2) / 3; 
			} else {
				ans += dp[cnt[1]][cnt[2]][cnt[3]];
			}
		}
		printf("Case #%d: %d\n", tt + 1, ans);
	}

	return 0;
}