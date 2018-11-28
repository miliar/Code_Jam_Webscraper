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

int n, m;
pt a[N];
pt q[N];
int g[N][N];


bool read(){
	if(scanf("%d%d", &n, &m) != 2)
		return 0;
	forn(i, n)
		scanf("%d%d", &a[i].x, &a[i].y);
	forn(i, n)
		forn(j, n)
			scanf("%d", &g[i][j]);
	forn(i, m){
		scanf("%d%d", &q[i].x, &q[i].y);
		--q[i].x;
	}
	return 1;
}


ld dp[N];
li pr[N];


void solve(){
	pr[0] = 0;
	fore(i, 1, n)
		pr[i] = pr[i - 1] + g[i - 1][i];
	forn(_, m){
		int l = q[_].x, r = q[_].y;
		fore(i, l + 1, r)
			dp[i] = INF64;
		dp[l] = 0;
		fore(i, l + 1, r){
			fore(j, l, i){
				li dist = pr[i] - pr[j];
				if (a[j].x >= dist)
					dp[i] = min(dp[i], dp[j] + dist * 1.0 / a[j].y);
			}
		}
		printf("%.10f ", double(dp[r - 1]));
	}
	printf("\n");
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