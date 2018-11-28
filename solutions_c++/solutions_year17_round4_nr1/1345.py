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

int n, p;
int a[N];


bool read(){
	if(scanf("%d%d", &n, &p) != 2)
		return 0;
	forn(i, n)
		scanf("%d", &a[i]);
	return 1;
}


int dp[101][101][101][101];
char used[101][101][101][101];
int dp3[101][101][101];
char used3[101][101][101];


int get(int a, int b, int c, int d){
	int &dr = dp[a][b][c][d];
	char &u = used[a][b][c][d];

	if (u)
		return dr;
	
	u = 1;
	dr = 0;
	
	if (a == 0 && b == 0 && c == 0 && d == 0)
		return dr;
	
	dr = 1;
	
	if (a)
		dr = max(dr, get(a - 1, b, c ,d) + 1);
	if (b && d)
		dr = max(dr, get(a, b - 1, c, d - 1) + 1);
	if (c > 1)
		dr = max(dr, get(a, b, c - 2, d) + 1);
	if (b > 1 && c)
		dr = max(dr, get(a, b - 2, c - 1, d) + 1);
	if (d > 1 && c)
		dr = max(dr, get(a, b, c - 1, d - 2) + 1);
	if (b > 3)
		dr = max(dr, get(a, b - 4, c, d) + 1);
	if (d > 3)
		dr = max(dr, get(a, b, c, d - 4) + 1);
	
	return dr;
}


int get(int a, int b, int c){
	int &dr = dp3[a][b][c];
	char &u = used3[a][b][c];

	if (u)
		return dr;
	
	u = 1;
	dr = 0;
	
	if (a == 0 && b == 0 && c == 0)
		return dr;
	
	dr = 1;
	
	if (a)
		dr = max(dr, get(a - 1, b, c) + 1);
	if (b && c)
		dr = max(dr, get(a, b - 1, c - 1) + 1);
	if (b > 2)
		dr = max(dr, get(a, b - 3, c) + 1);
	if (c > 2)
		dr = max(dr, get(a, b, c - 3) + 1);
	
	return dr;
}


void solve(){
	if (p == 2){
		int p1 = 0, p2 = 0;
		forn(i, n)
			if (a[i] % 2 == 0)
				++p1;
			else
				++p2;
		printf("%d\n", p1 + (p2 + 1) / 2);
	}
	else if (p == 3){
		int p1 = 0, p2 = 0, p3 = 0;
		forn(i, n)
			if (a[i] % 3 == 0)
				++p1;
			else if (a[i] % 3 == 1)
				++p2;
			else
				++p3;
		
		memset(dp3, 0, sizeof(dp3));
		memset(used3, 0, sizeof(used3));
		
		int ans = get(p1, p2, p3);
		printf("%d\n", ans);
	}
	else if (p == 4){
		int p1 = 0, p2 = 0, p3 = 0, p4 = 0;
		forn(i, n)
			if (a[i] % 4 == 0)
				++p1;
			else if (a[i] % 4 == 1)
				++p2;
			else if (a[i] % 4 == 2)
				++p3;
			else
				++p4;
		
		memset(dp, 0, sizeof(dp));
		memset(used, 0, sizeof(used));
		
		int ans = get(p1, p2, p3, p4);
		printf("%d\n", ans);
	}
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