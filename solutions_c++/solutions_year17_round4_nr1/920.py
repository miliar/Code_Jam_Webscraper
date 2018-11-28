#include"stdio.h"
#include"stdlib.h"
#include"math.h"
#include"string.h"
#include"set"
#include"map"
#include"queue"
#include"algorithm"
#define fi first
#define se second
#define IT iterator
#define INF 1000000007
#define INFL 4000000000000000007LL
#define MOD 1000000007LL
double const EPS = 1e-9;
double const PI  = acos(-1);
double const EXP = exp(1);
using namespace std;
typedef long long 		LL;
typedef pair<int, int>	II;
typedef vector<II>		VII;
typedef vector<int>		VI;
typedef set<int>		SI;
int Test_Cases, N, P, G[5], x;
int main() {
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);
	freopen("A-large.txt", "w", stdout);
	scanf("%d", &Test_Cases);
	for (int test = 1; test <= Test_Cases; test++) {
		for (int i = 0; i < 5; i++) G[i] = 0;
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; i++) {
			scanf("%d", &x);
			G[x % P]++;
		}
		int Ans = G[0];
		if (P == 2) 
			Ans += (G[1] + 1) / 2;
		else if (P == 3) {
			int mn = min(G[1], G[2]);
			int mx = max(G[1], G[2]);
			Ans += mn;
			Ans += (mx - mn + 2) / 3;
		}
		else {
			int mn = min(G[1], G[3]);
			int mx = max(G[1], G[3]);
			Ans += mn + (G[2] / 2);
			mx -= mn;
			G[2] %= 2;
			if (G[2] == 1) {
				Ans ++;
				mx = max(0, mx-2);
			}
			Ans += (mx + 3) / 4;
		}	
		printf("Case #%d: %d\n", test, Ans);
	}
}
	// memset(memo, -1, sizeof memo);
	// memset(arr, 0, sizeof arr);
	
	// ans = a ? b : c;						// to simplify: if (a) ans = b; else ans = c;
	// ans += val;							// to simplify: ans = ans + val;
	// index = (index + 1) % n;				// index++; if (index >= n) index = 0;
	// index = (index + n - 1) % n;			// index--; if (index < 0) index = n - 1;
	// int ans = (int)((double)d + 0.5);	// for rounding to nearest integer
	// ans = min(ans, new_computation);		// min / max shortcut;
