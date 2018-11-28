#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define li long long
#define ld long double
#define x first
#define y second
#define pt pair<int, int>
#define pll pair<li, li>
#define forn(i, t) for(int i = 0; i < (t); i++)
#define fore(i, f, t) for(int i = (f); i < (t); i++)
#define forr(i, f, t) for(int i = (f) - 1; i >= (t); i--)
#define all(x) (x).begin(), (x).end()
#define ins insert

using namespace std;


const int INF = 1e9;
const int MOD = 1e9 + 7;
const li INF64 = 1e18;
const ld EPS = 1e-7;

mt19937 myrand(time(NULL));

const int N = 100 + 7;
const int M = 720;

int n, m;
pt a[N], b[N];


bool read(){
	if(scanf("%d%d", &n, &m) != 2)
		return 0;
	forn(i, n)
		scanf("%d%d", &a[i].x, &a[i].y);
	forn(i, m)
		scanf("%d%d", &b[i].x, &b[i].y);
	return 1;
}


int dp[2][M + 7][M + 7];


void solve(){
	//sort(a, a + n);
	//sort(b, b + m);
	memset(dp, 127, sizeof(dp));
	dp[0][0][0] = dp[1][0][0] = 0;
	forn(i, M + 1){
		forn(j, M + 1){
			bool fll = false, flr = false;
			forn(l, n)
				//if (a[l].x == i + j && j + (a[l].y - a[l].x) <= M)
				//	dp[1][i][j + (a[l].y - a[l].x)] = min(dp[1][i][j + (a[l].y - a[l].x)], min(dp[0][i][j] + 1, dp[1][i][j]));
				if (i + j >= a[l].x && i + j < a[l].y){
					fll = true;
					break;
				}
			forn(r, m)
				//if (b[r].x == i + j && i + (b[r].y - b[r].x) <= M)
				//	dp[0][i + (b[r].y - b[r].x)][j] = min(dp[0][i][j], dp[1][i][j] + 1);
				if (i + j >= b[r].x && i + j < b[r].y){
					flr = true;
					break;
				}
			if (!fll)
				dp[0][i + 1][j] = min(dp[0][i + 1][j], min(dp[0][i][j], dp[1][i][j] + 1));
			if (!flr)
				dp[1][i][j + 1] = min(dp[1][i][j + 1], min(dp[0][i][j] + 1, dp[1][i][j]));
		}
	}
	/*forn(i, 30){
		forn(j, 30)
			printf("[%d %d] ", dp[0][j][i], dp[1][j][i]);
		printf("\n");
	}*/
	//printf("[%d %d] ", dp[0][M], dp[1][M]);
	if (dp[0][M][M] & 1) 
		dp[0][M][M]++;
	if (dp[1][M][M] & 1) 
		dp[1][M][M]++;
	printf("%d\n", min(dp[0][M][M], dp[1][M][M]));
}


int main(){
	#ifdef _DEBUG
		freopen("input.txt", "r", stdin);
	#endif
	int n;
	scanf("%d\n", &n);
	forn(i, n){
		read();
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}