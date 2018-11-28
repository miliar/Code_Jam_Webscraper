#include <bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define sz(x) (int)(x).size()
#define li long long
#define ld long double
#define x first
#define y second
#define pt pair<double, double>
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

const int N = 1000 + 13;

double d;
int n;
pt a[N];


bool read(){
	if(scanf("%lf%d", &d, &n) != 2)
		return 0;
	forn(i, n)
		scanf("%lf%lf", &a[i].x, &a[i].y);
	return 1;
}


void solve(){
	sort(a, a + n, greater<pt>());
	double t = (d - a[0].x) / a[0].y;
	fore(i, 1, n)
		t = max(t, (d - a[i].x) / a[i].y);
	printf("%.10f\n", d / t);
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