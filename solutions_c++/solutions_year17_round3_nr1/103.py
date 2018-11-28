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

const double PI = acos(-1);

mt19937 myrand(time(NULL));

const int N = 1000 + 13;

int n, k;
pt a[N];


bool read(){
	if(scanf("%d%d", &n, &k) != 2)
		return 0;
	forn(i, n)
		scanf("%d%d", &a[i].x, &a[i].y);
	return 1;
}


bool comp(const pt &a, const pt &b){
	//return a.x * 1ll * a.x + a.x * 2ll * a.y > b.x * 1ll * b.x + b.x * 2ll * b.y;
	return a.x * 2ll * a.y > b.x * 2ll * b.y;
}


void solve(){
	sort(a, a + n, comp);
	li ans = 0;
	int r = 0;
	forn(i, k - 1){
		ans += a[i].x * 2ll * a[i].y;
		r = max(r, a[i].x);
	}
	li res = 0;
	fore(i, k - 1, n){
		li mr = max(r, a[i].x) * 1ll * max(r, a[i].x);
		res = max(res, ans + mr + a[i].x * 2ll * a[i].y);
	}
	printf("%.10f\n", res * PI);
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